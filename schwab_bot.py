import asyncio
import logging
import os
import time
import uuid
from datetime import datetime, timezone, timedelta
import pandas as pd
import pandas_ta as ta
from supabase import create_client, Client
import aiohttp
import json
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('/bot/trading.log')
    ]
)
logger = logging.getLogger(__name__)

# Schwab API Configuration
SCHWAB_TRADER_API = "https://api.schwabapi.com/trader/v1"
SCHWAB_MARKET_API = "https://api.schwabapi.com/marketdata/v1"
SCHWAB_USERNAME = os.getenv("SCHWAB_USERNAME")
SCHWAB_PASSWORD = os.getenv("SCHWAB_PASSWORD")
SCHWAB_TRADER_TOKEN = os.getenv("SCHWAB_TRADER_TOKEN")
SCHWAB_MARKET_TOKEN = os.getenv("SCHWAB_MARKET_TOKEN")

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Trading parameters
SYMBOLS = ["AAPL", "MSFT", "GOOGL"]  # Stocks to monitor
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
POSITION_SIZE = 100  # Number of shares per trade

class SchwabAPI:
    def __init__(self):
        self.trader_session = aiohttp.ClientSession()
        self.market_session = aiohttp.ClientSession()
        self.trader_token = SCHWAB_TRADER_TOKEN
        self.market_token = SCHWAB_MARKET_TOKEN
        self.account_numbers = {}  # Map of plain text to encrypted account numbers
        
    def _get_correlation_id(self) -> str:
        """Generate a unique correlation ID for Schwab API requests"""
        return str(uuid.uuid4())
        
    async def connect(self):
        """Initialize connection and get account numbers"""
        try:
            headers = {
                "Authorization": f"Bearer {self.trader_token}",
                "Accept": "application/json",
                "Schwab-Client-CorrelId": self._get_correlation_id()
            }
            
            async with self.trader_session.get(
                f"{SCHWAB_TRADER_API}/accounts/accountNumbers",
                headers=headers
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    self.account_numbers = {
                        item["accountNumber"]: item["hashValue"] 
                        for item in data
                    }
                    logger.info(f"Successfully connected to Schwab API. Found {len(self.account_numbers)} accounts.")
                elif response.status == 401:
                    error = await response.json()
                    raise Exception(f"Authentication failed: {error.get('message', 'Unknown error')}")
                elif response.status == 403:
                    error = await response.json()
                    raise Exception(f"Access forbidden: {error.get('message', 'Unknown error')}")
                else:
                    error = await response.text()
                    raise Exception(f"Failed to get account numbers: {error}")
                    
        except Exception as e:
            logger.error(f"Failed to connect to Schwab API: {e}")
            raise

    async def disconnect(self):
        """Close the sessions"""
        await self.trader_session.close()
        await self.market_session.close()

    async def get_historical_data(self, symbol: str, period_type: str = "day", period: int = 10,
                                frequency_type: str = "minute", frequency: int = 5,
                                start_date: Optional[int] = None, end_date: Optional[int] = None,
                                need_extended_hours: bool = False) -> pd.DataFrame:
        """
        Get historical price data for a symbol using Schwab's price history API.
        
        Args:
            symbol: The stock symbol to get data for
            period_type: The type of period ('day', 'month', 'year', 'ytd')
            period: Number of periods to get data for (depends on period_type)
            frequency_type: The type of frequency ('minute', 'daily', 'weekly', 'monthly')
            frequency: The frequency value (depends on frequency_type)
            start_date: Optional start date in UNIX milliseconds
            end_date: Optional end date in UNIX milliseconds
            need_extended_hours: Whether to include extended hours data
            
        Returns:
            DataFrame with columns: datetime, open, high, low, close, volume
        """
        params = {
            "symbol": symbol,
            "periodType": period_type,
            "period": period,
            "frequencyType": frequency_type,
            "frequency": frequency,
            "needExtendedHoursData": need_extended_hours
        }
        
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
            
        headers = {
            "Accept": "*/*",
            "Schwab-Client-CorrelId": self._get_correlation_id(),
            "Authorization": f"Bearer {self.market_token}"
        }
        
        try:
            async with self.market_session.get(
                f"{SCHWAB_MARKET_API}/pricehistory",
                params=params,
                headers=headers
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("empty", True):
                        logging.warning(f"No price history data found for {symbol}")
                        return pd.DataFrame()
                        
                    candles = data.get("candles", [])
                    if not candles:
                        logging.warning(f"No candles found in price history for {symbol}")
                        return pd.DataFrame()
                        
                    df = pd.DataFrame(candles)
                    # Convert datetime from UNIX milliseconds to pandas datetime
                    df["datetime"] = pd.to_datetime(df["datetime"], unit="ms")
                    # Ensure columns are in the right order
                    df = df[["datetime", "open", "high", "low", "close", "volume"]]
                    return df
                    
                elif response.status == 401:
                    logging.error("Unauthorized access to price history API. Check market data token.")
                    raise Exception("Unauthorized access to price history API")
                elif response.status == 404:
                    logging.error(f"Symbol {symbol} not found")
                    return pd.DataFrame()
                else:
                    error_text = await response.text()
                    logging.error(f"Failed to get price history. Status: {response.status}, Error: {error_text}")
                    raise Exception(f"Failed to get price history: {error_text}")
                    
        except aiohttp.ClientError as e:
            logging.error(f"Network error while getting price history: {str(e)}")
            raise Exception(f"Network error while getting price history: {str(e)}")
        except Exception as e:
            logging.error(f"Unexpected error while getting price history: {str(e)}")
            raise Exception(f"Unexpected error while getting price history: {str(e)}")

    async def get_quote(self, symbol: str) -> Dict:
        """Get current quote using Market Data API
        
        Args:
            symbol: The stock symbol to get a quote for
            
        Returns:
            Dict containing quote data with the following structure:
            {
                'last_price': float,
                'bid_price': float,
                'ask_price': float,
                'volume': int,
                'mark': float,
                'mark_change': float,
                'mark_percent_change': float,
                'security_status': str,
                'asset_type': str,
                'description': str,
                'exchange': str
            }
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.market_token}",
                "Accept": "application/json",
                "Schwab-Client-CorrelId": self._get_correlation_id()
            }
            
            params = {
                "fields": "quote,reference"  # Get both quote and reference data
            }
            
            async with self.market_session.get(
                f"{SCHWAB_MARKET_API}/{symbol}/quotes",
                headers=headers,
                params=params
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if symbol not in data:
                        logger.warning(f"No quote data found for {symbol}")
                        return {}
                        
                    symbol_data = data[symbol]
                    quote_data = symbol_data.get('quote', {})
                    ref_data = symbol_data.get('reference', {})
                    
                    # Extract and normalize the data
                    return {
                        'last_price': quote_data.get('lastPrice', 0.0),
                        'bid_price': quote_data.get('bidPrice', 0.0),
                        'ask_price': quote_data.get('askPrice', 0.0),
                        'volume': quote_data.get('totalVolume', 0),
                        'mark': quote_data.get('mark', 0.0),
                        'mark_change': quote_data.get('markChange', 0.0),
                        'mark_percent_change': quote_data.get('markPercentChange', 0.0),
                        'security_status': quote_data.get('securityStatus', 'Unknown'),
                        'asset_type': symbol_data.get('assetMainType', 'Unknown'),
                        'description': ref_data.get('description', ''),
                        'exchange': ref_data.get('exchangeName', ''),
                        'is_shortable': ref_data.get('isShortable', False),
                        'is_hard_to_borrow': ref_data.get('isHardToBorrow', False),
                        'htb_rate': ref_data.get('htbRate', 0.0)
                    }
                elif response.status == 404:
                    logger.warning(f"Symbol {symbol} not found")
                    return {}
                else:
                    error = await response.text()
                    error_json = await response.json()
                    logger.error(f"Quote request failed with status {response.status}: {error_json.get('message', error)}")
                    if 'errors' in error_json:
                        logger.error(f"Error details: {error_json['errors']}")
                    raise Exception(f"Failed to get quote: {error}")
                    
        except Exception as e:
            logger.error(f"Error getting quote for {symbol}: {e}")
            return {}

    async def get_account_positions(self, account_number: str) -> List[Dict]:
        """Get current positions using Trader API"""
        try:
            headers = {
                "Authorization": f"Bearer {self.trader_token}",
                "Accept": "application/json",
                "Schwab-Client-CorrelId": self._get_correlation_id()
            }
            
            encrypted_account = self.account_numbers.get(account_number)
            if not encrypted_account:
                raise ValueError(f"No encrypted value found for account {account_number}")
                
            async with self.trader_session.get(
                f"{SCHWAB_TRADER_API}/accounts/{encrypted_account}",
                params={"fields": "positions"},
                headers=headers
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("securitiesAccount", {}).get("positions", [])
                else:
                    error = await response.text()
                    raise Exception(f"Failed to get positions: {error}")
                    
        except Exception as e:
            logger.error(f"Error getting positions for account {account_number}: {e}")
            return []

    async def place_order(self, account_number: str, symbol: str, action: str, quantity: int) -> Optional[int]:
        """Place a market order using Trader API
        
        Returns:
            Optional[int]: The order ID if successful, None if failed
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.trader_token}",
                "Accept": "*/*",
                "Content-Type": "application/json",
                "Schwab-Client-CorrelId": self._get_correlation_id()
            }
            
            encrypted_account = self.account_numbers.get(account_number)
            if not encrypted_account:
                raise ValueError(f"No encrypted value found for account {account_number}")
            
            # Get current quote first
            quote = await self.get_quote(symbol)
            if not quote:
                raise Exception(f"Could not get quote for {symbol}")
            
            order_data = {
                "session": "NORMAL",
                "duration": "DAY",
                "orderType": "MARKET",
                "complexOrderStrategyType": "NONE",
                "orderStrategyType": "SINGLE",
                "orderLegCollection": [
                    {
                        "orderLegType": "EQUITY",
                        "instrument": {
                            "symbol": symbol,
                            "type": "EQUITY"
                        },
                        "instruction": action,
                        "quantity": quantity,
                        "quantityType": "SHARES",
                        "positionEffect": "OPENING" if action == "BUY" else "CLOSING"
                    }
                ],
                "taxLotMethod": "FIFO"
            }
            
            async with self.trader_session.post(
                f"{SCHWAB_TRADER_API}/accounts/{encrypted_account}/orders",
                headers=headers,
                json=order_data
            ) as response:
                if response.status == 201:
                    # Get order ID from Location header
                    order_url = response.headers.get('Location')
                    logger.info(f"Successfully placed {action} order for {quantity} shares of {symbol}")
                    if order_url:
                        logger.info(f"Order URL: {order_url}")
                        # Extract order ID from URL
                        order_id = int(order_url.split('/')[-1])
                        return order_id
                    return None
                else:
                    error = await response.text()
                    error_json = await response.json()
                    logger.error(f"Order placement failed with status {response.status}: {error_json.get('message', error)}")
                    if 'errors' in error_json:
                        logger.error(f"Error details: {error_json['errors']}")
                    raise Exception(f"Failed to place order: {error}")
                    
        except Exception as e:
            logger.error(f"Error placing order: {e}")
            return None

    async def cancel_order(self, account_number: str, order_id: int) -> bool:
        """Cancel an order using Trader API
        
        Args:
            account_number: The account number
            order_id: The ID of the order to cancel
            
        Returns:
            bool: True if cancelled successfully, False otherwise
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.trader_token}",
                "Accept": "*/*",
                "Schwab-Client-CorrelId": self._get_correlation_id()
            }
            
            encrypted_account = self.account_numbers.get(account_number)
            if not encrypted_account:
                raise ValueError(f"No encrypted value found for account {account_number}")
                
            async with self.trader_session.delete(
                f"{SCHWAB_TRADER_API}/accounts/{encrypted_account}/orders/{order_id}",
                headers=headers
            ) as response:
                if response.status == 200:
                    logger.info(f"Successfully cancelled order {order_id}")
                    return True
                elif response.status == 404:
                    error_json = await response.json()
                    logger.warning(f"Order {order_id} not found: {error_json.get('message')}")
                    return False
                else:
                    error = await response.text()
                    error_json = await response.json()
                    logger.error(f"Order cancellation failed with status {response.status}: {error_json.get('message', error)}")
                    if 'errors' in error_json:
                        logger.error(f"Error details: {error_json['errors']}")
                    raise Exception(f"Failed to cancel order: {error}")
                    
        except Exception as e:
            logger.error(f"Error cancelling order: {e}")
            return False

    async def get_orders(self, account_number: str, from_date: datetime = None, to_date: datetime = None, status: str = None) -> List[Dict]:
        """Get order history using Trader API
        
        Args:
            account_number: The account number to get orders for
            from_date: Start date for order history (defaults to 30 days ago)
            to_date: End date for order history (defaults to now)
            status: Filter by order status (e.g. 'FILLED')
            
        Returns:
            List of orders matching the criteria
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.trader_token}",
                "Accept": "application/json",
                "Schwab-Client-CorrelId": self._get_correlation_id()
            }
            
            encrypted_account = self.account_numbers.get(account_number)
            if not encrypted_account:
                raise ValueError(f"No encrypted value found for account {account_number}")
            
            # Default to last 30 days if dates not specified
            if not from_date:
                from_date = datetime.now(timezone.utc) - timedelta(days=30)
            if not to_date:
                to_date = datetime.now(timezone.utc)
                
            params = {
                "fromEnteredTime": from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "toEnteredTime": to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            }
            
            if status:
                params["status"] = status
                
            async with self.trader_session.get(
                f"{SCHWAB_TRADER_API}/accounts/{encrypted_account}/orders",
                headers=headers,
                params=params
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Retrieved {len(data)} orders for account {account_number}")
                    return data
                else:
                    error = await response.text()
                    raise Exception(f"Failed to get orders: {error}")
                    
        except Exception as e:
            logger.error(f"Error getting orders for account {account_number}: {e}")
            return []

class RSITradingBot:
    def __init__(self):
        self.schwab = SchwabAPI()
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.positions = {}
        self.account_number = os.getenv("SCHWAB_ACCOUNT_NUMBER")
        self.pending_orders = {}  # Track pending orders by symbol

    def calculate_rsi_from_df(self, df: pd.DataFrame) -> pd.Series:
        """Calculate RSI from a DataFrame containing OHLCV data"""
        # Calculate price changes
        df['price_change'] = df['close'].diff()
        
        # Calculate gains (positive changes) and losses (negative changes)
        df['gain'] = df['price_change'].apply(lambda x: x if x > 0 else 0)
        df['loss'] = df['price_change'].apply(lambda x: abs(x) if x < 0 else 0)
        
        # Calculate average gains and losses over RSI_PERIOD
        avg_gain = df['gain'].rolling(window=RSI_PERIOD).mean()
        avg_loss = df['loss'].rolling(window=RSI_PERIOD).mean()
        
        # Calculate RS and RSI
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    async def calculate_rsi(self, symbol: str) -> float:
        """Calculate RSI for a symbol using historical data"""
        try:
            # Get historical data for RSI calculation (14 days of 5-min data)
            end_date = int(datetime.now().timestamp() * 1000)  # Convert to milliseconds
            start_date = int((datetime.now() - timedelta(days=14)).timestamp() * 1000)
            
            df = await self.schwab.get_historical_data(
                symbol=symbol,
                period_type="day",
                period=14,
                frequency_type="minute",
                frequency=5,
                start_date=start_date,
                end_date=end_date
            )
            
            if df.empty:
                logging.warning(f"No data available to calculate RSI for {symbol}")
                return 50.0  # Return neutral RSI if no data
                
            rsi = self.calculate_rsi_from_df(df)
            current_rsi = rsi.iloc[-1]
            logging.info(f"Calculated RSI for {symbol}: {current_rsi:.2f}")
            return current_rsi
            
        except Exception as e:
            logging.error(f"Error calculating RSI for {symbol}: {str(e)}")
            return 50.0  # Return neutral RSI on error

    async def log_trade(self, symbol: str, action: str, rsi_value: float):
        """Log trade to Supabase"""
        try:
            self.supabase.table('trades').insert({
                'symbol': symbol,
                'action': action,
                'rsi': float(rsi_value),
                'timestamp': datetime.now(timezone.utc).isoformat()
            }).execute()
            logger.info(f"Trade logged: {symbol} {action} RSI={rsi_value}")
        except Exception as e:
            logger.error(f"Failed to log trade: {e}")

    async def check_market_hours(self) -> bool:
        """Check if market is currently open"""
        now = datetime.now(timezone.utc)
        if now.weekday() >= 5:  # Weekend
            return False
        ny_time = now.replace(tzinfo=timezone.utc).astimezone(timezone.utc)
        market_open = ny_time.replace(hour=13, minute=30, second=0)  # 9:30 AM ET
        market_close = ny_time.replace(hour=20, minute=0, second=0)  # 4:00 PM ET
        return market_open <= ny_time <= market_close

    async def update_positions(self):
        """Update current positions from Schwab"""
        positions = await self.schwab.get_account_positions(self.account_number)
        self.positions = {
            pos['instrument']['symbol']: pos['longQuantity']
            for pos in positions
            if pos.get('longQuantity', 0) > 0
        }

    async def process_symbol(self, symbol: str):
        """Process a single symbol for trading signals"""
        try:
            # Get current positions first
            await self.update_positions()
            
            # Calculate RSI using the new method
            current_rsi = await self.calculate_rsi(symbol)
            logger.info(f"{symbol} RSI: {current_rsi}")
            
            current_position = self.positions.get(symbol, 0)
            
            # Cancel any existing pending orders for this symbol
            if symbol in self.pending_orders:
                order_id = self.pending_orders[symbol]
                if await self.schwab.cancel_order(self.account_number, order_id):
                    del self.pending_orders[symbol]
            
            if current_rsi <= RSI_OVERSOLD and current_position == 0:
                # Buy signal
                order_id = await self.schwab.place_order(
                    self.account_number,
                    symbol,
                    'BUY',
                    POSITION_SIZE
                )
                if order_id:
                    self.pending_orders[symbol] = order_id
                    await self.log_trade(symbol, 'BUY', current_rsi)
                    logger.info(f"Bought {POSITION_SIZE} shares of {symbol}")
            
            elif current_rsi >= RSI_OVERBOUGHT and current_position > 0:
                # Sell signal
                order_id = await self.schwab.place_order(
                    self.account_number,
                    symbol,
                    'SELL',
                    current_position
                )
                if order_id:
                    self.pending_orders[symbol] = order_id
                    await self.log_trade(symbol, 'SELL', current_rsi)
                    logger.info(f"Sold {current_position} shares of {symbol}")

        except Exception as e:
            logger.error(f"Error processing {symbol}: {e}")

    async def run(self):
        """Main bot loop"""
        try:
            await self.schwab.connect()
            
            while True:
                if await self.check_market_hours():
                    logger.info("Market is open, processing symbols...")
                    await asyncio.gather(*(self.process_symbol(symbol) for symbol in SYMBOLS))
                else:
                    logger.info("Market is closed")
                
                await asyncio.sleep(60)  # Wait 1 minute before next check
                
        except Exception as e:
            logger.error(f"Bot error: {e}")
        finally:
            await self.schwab.disconnect()

    async def get_filled_orders(self, days_back: int = 30) -> List[Dict]:
        """Get filled orders for analysis"""
        from_date = datetime.now(timezone.utc) - timedelta(days=days_back)
        return await self.schwab.get_orders(
            self.account_number,
            from_date=from_date,
            status="FILLED"
        )

if __name__ == "__main__":
    bot = RSITradingBot()
    asyncio.run(bot.run()) 