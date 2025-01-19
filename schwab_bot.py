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
from dotenv import load_dotenv
import sys
import requests  # <-- NEW: used for token exchange example

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=os.environ.get("LOG_LEVEL", "INFO"),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('/home/trading/bot/logs/trading.log')
        ]
    )
    return logging.getLogger(__name__)

# Initialize logger first
logger = setup_logging()

# Load environment variables
logger.info("Loading environment variables...")
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
logger.info(f"Looking for .env file at: {env_path}")

if os.path.exists(env_path):
    logger.info("Found .env file")
    load_dotenv(env_path)
    logger.info("Environment variables loaded from .env file")
else:
    logger.warning("No .env file found")

# Global variables for configuration
env_vars = {}
keys_to_load = [
    "SUPABASE_URL",
    "SUPABASE_KEY",
    "SCHWAB_TRADER_TOKEN",
    "SCHWAB_MARKET_TOKEN",
    "SCHWAB_ACCOUNT_NUMBER",
    "SYMBOLS",
    "RSI_PERIOD",
    "RSI_OVERBOUGHT",
    "RSI_OVERSOLD",
    "POSITION_SIZE",
    # NEW KEYS BELOW
    "SCHWAB_CLIENT_ID",
    "SCHWAB_CLIENT_SECRET",
    "SCHWAB_REDIRECT_URI",
    "SCHWAB_AUTH_CODE",
    "SCHWAB_REFRESH_TOKEN"
]

for key in keys_to_load:
    value = os.environ.get(key)
    # For security, don't log sensitive tokens
    if key in ["SUPABASE_KEY", "SCHWAB_TRADER_TOKEN", "SCHWAB_MARKET_TOKEN",
               "SCHWAB_CLIENT_ID", "SCHWAB_CLIENT_SECRET", "SCHWAB_AUTH_CODE", "SCHWAB_REFRESH_TOKEN"]:
        logger.info(f"Loaded {key}: {'***' if value else 'None'}")
    else:
        logger.info(f"Loaded {key}: {value}")

    env_vars[key] = value

# Basic checks
if not env_vars.get("SUPABASE_URL"):
    logger.error("SUPABASE_URL is missing")
if not env_vars.get("SUPABASE_KEY"):
    logger.error("SUPABASE_KEY is missing")

# Initialize API URLs
SCHWAB_TRADER_API = "https://api.schwabapi.com/trader/v1"
SCHWAB_MARKET_API = "https://api.schwabapi.com/marketdata/v1"


# --------------------------------------------------------
# NEW SECTION: Helpers for OAuth2 token fetching/refresh
# --------------------------------------------------------
def fetch_schwab_access_token(auth_code: str, client_id: str, client_secret: str, redirect_uri: str) -> Dict[str, str]:
    """
    Exchange the given auth_code for an access_token and refresh_token from Schwab.
    """
    logger.info("Fetching new Schwab access token using authorization code...")
    token_url = "https://api.schwabapi.com/v1/oauth/token"

    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        token_data = response.json()
        logger.info("Successfully obtained Schwab tokens via authorization code.")
        return token_data  # includes access_token, refresh_token, expires_in, etc.
    else:
        logger.error(f"Failed to fetch tokens. Status {response.status_code}: {response.text}")
        raise ValueError("Could not obtain Schwab tokens from auth code")

def refresh_schwab_access_token(refresh_token: str, client_id: str, client_secret: str) -> Dict[str, str]:
    """
    Use the provided refresh_token to get a new access_token (and possibly new refresh_token).
    """
    logger.info("Refreshing Schwab access token using refresh token...")
    token_url = "https://api.schwabapi.com/v1/oauth/token"

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        token_data = response.json()
        logger.info("Successfully refreshed Schwab tokens.")
        return token_data
    else:
        logger.error(f"Failed to refresh tokens. Status {response.status_code}: {response.text}")
        raise ValueError("Could not refresh Schwab tokens")

def ensure_schwab_tokens(env_vars: Dict[str, str]) -> Dict[str, str]:
    """
    If SCHWAB_TRADER_TOKEN/MARKET_TOKEN are missing or empty, tries to:
      1) use SCHWAB_AUTH_CODE to do a new token exchange, or
      2) use SCHWAB_REFRESH_TOKEN to do a token refresh.
    Returns updated env_vars with the new tokens if successful.
    """
    trader_token = env_vars.get("SCHWAB_TRADER_TOKEN")
    market_token = env_vars.get("SCHWAB_MARKET_TOKEN")

    if trader_token and market_token:
        logger.info("SCHWAB_TRADER_TOKEN and SCHWAB_MARKET_TOKEN already provided. Skipping OAuth fetch/refresh.")
        return env_vars

    client_id = env_vars.get("SCHWAB_CLIENT_ID")
    client_secret = env_vars.get("SCHWAB_CLIENT_SECRET")
    redirect_uri = env_vars.get("SCHWAB_REDIRECT_URI")
    auth_code = env_vars.get("SCHWAB_AUTH_CODE")
    refresh_token = env_vars.get("SCHWAB_REFRESH_TOKEN")

    # Basic check
    if not client_id or not client_secret:
        logger.warning("No client_id/client_secret found. Cannot fetch or refresh tokens automatically.")
        return env_vars  # Let the user proceed with placeholders or handle externally

    # Try refresh first if we have a refresh token
    if refresh_token:
        try:
            token_data = refresh_schwab_access_token(refresh_token, client_id, client_secret)
            new_access = token_data.get("access_token")
            new_refresh = token_data.get("refresh_token")  # might be the same or new
            if new_access:
                env_vars["SCHWAB_TRADER_TOKEN"] = new_access
                env_vars["SCHWAB_MARKET_TOKEN"] = new_access
                env_vars["SCHWAB_REFRESH_TOKEN"] = new_refresh if new_refresh else refresh_token
                logger.info("Updated SCHWAB_TRADER_TOKEN and SCHWAB_MARKET_TOKEN from refresh token.")
                return env_vars
        except Exception as e:
            logger.error(f"Refresh token attempt failed: {e}")
            # fallback to trying auth_code

    # If we have an auth_code, try exchanging it for tokens
    if auth_code:
        try:
            token_data = fetch_schwab_access_token(auth_code, client_id, client_secret, redirect_uri)
            new_access = token_data.get("access_token")
            new_refresh = token_data.get("refresh_token")
            if new_access:
                env_vars["SCHWAB_TRADER_TOKEN"] = new_access
                env_vars["SCHWAB_MARKET_TOKEN"] = new_access
                if new_refresh:
                    env_vars["SCHWAB_REFRESH_TOKEN"] = new_refresh
                logger.info("Updated SCHWAB_TRADER_TOKEN and SCHWAB_MARKET_TOKEN from auth code.")
                return env_vars
        except Exception as e:
            logger.error(f"Auth code token exchange failed: {e}")

    # If we got here, we couldn't fetch or refresh tokens automatically
    logger.warning("Could not fetch/refresh Schwab tokens automatically. Check logs for details.")
    return env_vars

# --------------------------------------------------------
# END OAuth2 HELPERS
# --------------------------------------------------------


class SchwabAPI:
    def __init__(self, trader_token, market_token):
        self.trader_token = trader_token
        self.market_token = market_token
        self.trader_session = None
        self.market_session = None
        if not self.trader_token or not self.market_token:
            raise ValueError("Schwab API tokens are missing")
        self.account_numbers = {}
        
    async def connect(self):
        """Initialize API sessions"""
        logger.info("Initializing Schwab API sessions...")
        
        # Create sessions
        timeout = aiohttp.ClientTimeout(total=30)
        
        # Create sessions
        self.trader_session = aiohttp.ClientSession(timeout=timeout)
        self.market_session = aiohttp.ClientSession(timeout=timeout)
        
        # Get account numbers
        try:
            headers = {
                "Authorization": f"Bearer {self.trader_token}",
                "Accept": "application/json",
                "Schwab-Client-CorrelId": self._get_correlation_id()
            }
            
            async with self.trader_session.get(
                f"https://api.schwabapi.com/trader/v1/accounts/accountNumbers",
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
                    raise Exception(f"Authentication failed (401): {error.get('message', 'Unknown error')}")
                elif response.status == 403:
                    error = await response.json()
                    raise Exception(f"Access forbidden (403): {error.get('message', 'Unknown error')}")
                else:
                    error = await response.text()
                    raise Exception(f"Failed to get account numbers: {error}")
        except Exception as e:
            logger.error(f"Failed to connect to Schwab API: {e}")
            await self.disconnect()  # Clean up sessions on error
            raise

    async def disconnect(self):
        """Close API sessions"""
        logger.info("Closing Schwab API sessions...")
        if self.trader_session:
            await self.trader_session.close()
            self.trader_session = None
        if self.market_session:
            await self.market_session.close()
            self.market_session = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    def _get_correlation_id(self) -> str:
        """Generate a unique correlation ID for Schwab API requests"""
        return str(uuid.uuid4())
        
    async def get_historical_data(self, symbol: str, period_type: str = "day", period: int = 10,
                                frequency_type: str = "minute", frequency: int = 5,
                                start_date: Optional[int] = None, end_date: Optional[int] = None,
                                need_extended_hours: bool = False) -> pd.DataFrame:
        """
        Get historical price data for a symbol using Schwab's price history API.
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
                "https://api.schwabapi.com/marketdata/v1/pricehistory",
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
        """Get current quote using Market Data API."""
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
                f"https://api.schwabapi.com/marketdata/v1/{symbol}/quotes",
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
                    try:
                        error_json = await response.json()
                        logger.error(f"Quote request failed with status {response.status}: "
                                     f"{error_json.get('message', error)}")
                        if 'errors' in error_json:
                            logger.error(f"Error details: {error_json['errors']}")
                    except:
                        logger.error(f"Quote request failed with status {response.status}. Response text: {error}")
                    raise Exception(f"Failed to get quote: {error}")
                    
        except Exception as e:
            logger.error(f"Error getting quote for {symbol}: {e}")
            return {}

    async def get_account_positions(self, account_number: str) -> List[Dict]:
        """Get current positions using Trader API."""
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
                f"https://api.schwabapi.com/trader/v1/accounts/{encrypted_account}",
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
        """Place a market order using Trader API."""
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
                f"https://api.schwabapi.com/trader/v1/accounts/{encrypted_account}/orders",
                headers=headers,
                json=order_data
            ) as response:
                if response.status == 201:
                    order_url = response.headers.get('Location')
                    logger.info(f"Successfully placed {action} order for {quantity} shares of {symbol}")
                    if order_url:
                        logger.info(f"Order URL: {order_url}")
                        order_id = int(order_url.split('/')[-1])
                        return order_id
                    return None
                else:
                    error = await response.text()
                    try:
                        error_json = await response.json()
                        logger.error(f"Order placement failed with status {response.status}: "
                                     f"{error_json.get('message', error)}")
                        if 'errors' in error_json:
                            logger.error(f"Error details: {error_json['errors']}")
                    except:
                        logger.error(f"Order placement failed with status {response.status}. Response text: {error}")
                    raise Exception(f"Failed to place order: {error}")
                    
        except Exception as e:
            logger.error(f"Error placing order: {e}")
            return None

    async def cancel_order(self, account_number: str, order_id: int) -> bool:
        """Cancel an order using Trader API."""
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
                f"https://api.schwabapi.com/trader/v1/accounts/{encrypted_account}/orders/{order_id}",
                headers=headers
            ) as response:
                if response.status == 200:
                    logger.info(f"Successfully cancelled order {order_id}")
                    return True
                elif response.status == 404:
                    try:
                        error_json = await response.json()
                        logger.warning(f"Order {order_id} not found: {error_json.get('message')}")
                    except:
                        logger.warning("Order not found (404). No JSON response.")
                    return False
                else:
                    error = await response.text()
                    try:
                        error_json = await response.json()
                        logger.error(f"Order cancellation failed with status {response.status}: "
                                     f"{error_json.get('message', error)}")
                        if 'errors' in error_json:
                            logger.error(f"Error details: {error_json['errors']}")
                    except:
                        logger.error(f"Order cancellation failed with status {response.status}. Response text: {error}")
                    raise Exception(f"Failed to cancel order: {error}")
                    
        except Exception as e:
            logger.error(f"Error cancelling order: {e}")
            return False

    async def get_orders(self, account_number: str, from_date: datetime = None, to_date: datetime = None, status: str = None) -> List[Dict]:
        """Get order history using Trader API."""
        try:
            headers = {
                "Authorization": f"Bearer {self.trader_token}",
                "Accept": "application/json",
                "Schwab-Client-CorrelId": self._get_correlation_id()
            }
            
            encrypted_account = self.account_numbers.get(account_number)
            if not encrypted_account:
                raise ValueError(f"No encrypted value found for account {account_number}")
            
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
                f"https://api.schwabapi.com/trader/v1/accounts/{encrypted_account}/orders",
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
        """Initialize the RSI trading bot."""
        logger.info("Initializing RSI Trading Bot...")

        # NEW STEP: Attempt to fetch or refresh Schwab tokens if missing
        updated_env = ensure_schwab_tokens(env_vars)

        # Now pull final tokens from updated_env
        supabase_url = updated_env["SUPABASE_URL"]
        supabase_key = updated_env["SUPABASE_KEY"]
        
        if not supabase_url or not supabase_key:
            logger.error("Supabase credentials are missing")
            raise ValueError("Supabase credentials are missing")
        
        # Create Supabase client
        try:
            logger.info(f"Initializing Supabase connection to {supabase_url}")
            self.supabase = create_client(supabase_url=supabase_url, supabase_key=supabase_key)
            logger.info("Successfully connected to Supabase")
        except Exception as e:
            logger.error(f"Failed to initialize Supabase client: {e}")
            raise
        
        # Schwab credentials
        self.trader_token = updated_env["SCHWAB_TRADER_TOKEN"]
        self.market_token = updated_env["SCHWAB_MARKET_TOKEN"]
        self.account_number = updated_env["SCHWAB_ACCOUNT_NUMBER"]
        
        if not self.trader_token or not self.market_token:
            raise ValueError("Schwab API tokens are missing")
        if not self.account_number:
            raise ValueError("Schwab account number is missing")
        
        # Initialize API client
        self.api = SchwabAPI(self.trader_token, self.market_token)
        
        # Trading parameters
        self.symbols = json.loads(updated_env["SYMBOLS"]) if updated_env["SYMBOLS"] else ["BITI"]
        self.rsi_period = int(updated_env["RSI_PERIOD"]) if updated_env["RSI_PERIOD"] else 14
        self.rsi_overbought = float(updated_env["RSI_OVERBOUGHT"]) if updated_env["RSI_OVERBOUGHT"] else 70.0
        self.rsi_oversold = float(updated_env["RSI_OVERSOLD"]) if updated_env["RSI_OVERSOLD"] else 30.0
        self.position_size = float(updated_env["POSITION_SIZE"]) if updated_env["POSITION_SIZE"] else 100
        
        self.pending_orders = {}  # symbol -> order_id
        self.positions = {}

    def calculate_rsi_from_df(self, df: pd.DataFrame) -> pd.Series:
        """Calculate RSI from a DataFrame containing OHLCV data."""
        df['price_change'] = df['close'].diff()
        df['gain'] = df['price_change'].apply(lambda x: x if x > 0 else 0)
        df['loss'] = df['price_change'].apply(lambda x: abs(x) if x < 0 else 0)
        
        avg_gain = df['gain'].rolling(window=self.rsi_period).mean()
        avg_loss = df['loss'].rolling(window=self.rsi_period).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    async def calculate_rsi(self, symbol: str) -> float:
        """Calculate RSI for a symbol using historical data."""
        try:
            end_date = int(datetime.now().timestamp() * 1000)  # ms
            start_date = int((datetime.now() - timedelta(days=14)).timestamp() * 1000)
            
            df = await self.api.get_historical_data(
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
                return 50.0
                
            rsi = self.calculate_rsi_from_df(df)
            current_rsi = rsi.iloc[-1]
            logging.info(f"Calculated RSI for {symbol}: {current_rsi:.2f}")
            return current_rsi
            
        except Exception as e:
            logging.error(f"Error calculating RSI for {symbol}: {str(e)}")
            return 50.0

    async def log_trade(self, symbol: str, action: str, rsi_value: float):
        """Log a trade to Supabase."""
        try:
            self.supabase.table('trades').insert({
                'symbol': symbol,
                'action': action,
                'rsi': float(rsi_value),
                'timestamp': datetime.now(timezone.utc).isoformat()
            }).execute()
            logger.info(f"Trade logged: {symbol} {action} at RSI {rsi_value}")
        except Exception as e:
            logger.error(f"Failed to log trade: {e}")

    async def log_performance(self, symbol: str, closing_price: float, rsi_value: float, position_size: float, pnl: float):
        """Log performance metrics to Supabase."""
        try:
            self.supabase.table('performance_metrics').insert({
                'symbol': symbol,
                'date': datetime.now(timezone.utc).date().isoformat(),
                'closing_price': float(closing_price),
                'rsi_value': float(rsi_value),
                'position_size': float(position_size),
                'pnl': float(pnl),
                'created_at': datetime.now(timezone.utc).isoformat()
            }).execute()
            logger.info(f"Performance logged: {symbol} price={closing_price} rsi={rsi_value} pnl={pnl}")
        except Exception as e:
            logger.error(f"Failed to log performance: {e}")

    async def check_market_hours(self) -> bool:
        """Check if market is currently open (roughly 9:30am-4pm ET)."""
        now = datetime.now(timezone.utc)
        if now.weekday() >= 5:
            return False
        ny_time = now.astimezone(timezone.utc)  # or use a real US/Eastern
        market_open = ny_time.replace(hour=13, minute=30, second=0)
        market_close = ny_time.replace(hour=20, minute=0, second=0)
        return market_open <= ny_time <= market_close

    async def update_positions(self):
        """Update current positions from Schwab."""
        positions = await self.api.get_account_positions(self.account_number)
        self.positions = {
            pos['instrument']['symbol']: pos['longQuantity']
            for pos in positions
            if pos.get('longQuantity', 0) > 0
        }

    async def process_symbol(self, symbol: str):
        """Process a single symbol for trading signals."""
        try:
            await self.update_positions()
            current_rsi = await self.calculate_rsi(symbol)
            logger.info(f"{symbol} RSI: {current_rsi}")
            
            current_position = self.positions.get(symbol, 0)
            
            # Cancel any existing pending orders
            if symbol in self.pending_orders:
                order_id = self.pending_orders[symbol]
                if await self.api.cancel_order(self.account_number, order_id):
                    del self.pending_orders[symbol]
            
            # Simple RSI-based strategy
            if current_rsi <= self.rsi_oversold and current_position == 0:
                # Buy signal
                order_id = await self.api.place_order(
                    self.account_number,
                    symbol,
                    'BUY',
                    int(self.position_size)
                )
                if order_id:
                    self.pending_orders[symbol] = order_id
                    await self.log_trade(symbol, 'BUY', current_rsi)
                    logger.info(f"Bought {self.position_size} shares of {symbol}")
            
            elif current_rsi >= self.rsi_overbought and current_position > 0:
                # Sell signal
                order_id = await self.api.place_order(
                    self.account_number,
                    symbol,
                    'SELL',
                    int(current_position)
                )
                if order_id:
                    self.pending_orders[symbol] = order_id
                    await self.log_trade(symbol, 'SELL', current_rsi)
                    logger.info(f"Sold {current_position} shares of {symbol}")

        except Exception as e:
            logger.error(f"Error processing {symbol}: {e}")

    async def start(self):
        """Initialize and start the bot."""
        logger.info("Starting RSI Trading Bot...")
        try:
            # Connect to Schwab
            self.api = SchwabAPI(self.trader_token, self.market_token)
            await self.api.connect()
            try:
                await self.run()
            finally:
                await self.api.disconnect()
        except Exception as e:
            logger.error(f"Bot error: {e}")
            raise

    async def run(self):
        """Main bot loop."""
        logger.info("Connected to Schwab API, starting main loop...")
        try:
            while True:
                try:
                    if await self.check_market_hours():
                        logger.info("Market is open, processing symbols...")
                        for symbol in self.symbols:
                            try:
                                logger.info(f"Processing symbol: {symbol}")
                                await self.process_symbol(symbol)
                                logger.info(f"Finished processing {symbol}")
                            except Exception as e:
                                logger.error(f"Error processing {symbol}: {e}")
                        logger.info("Finished processing all symbols")
                    else:
                        logger.info("Market is closed, waiting for next check")
                    
                    logger.info("Waiting 60 seconds before next check...")
                    await asyncio.sleep(60)
                    
                except Exception as e:
                    logger.error(f"Error in main loop: {e}")
                    logger.info("Waiting 60 seconds before retry...")
                    await asyncio.sleep(60)
                
        except Exception as e:
            logger.error(f"Critical bot error: {e}")
            raise
        finally:
            logger.info("Cleaning up bot resources...")

    async def get_filled_orders(self, days_back: int = 30) -> List[Dict]:
        """Get filled orders for analysis."""
        from_date = datetime.now(timezone.utc) - timedelta(days=days_back)
        return await self.api.get_orders(
            self.account_number,
            from_date=from_date,
            status="FILLED"
        )


async def main():
    """Main entry point for the trading bot."""
    try:
        logger.info("Starting RSI Trading Bot...")
        bot = RSITradingBot()
        await bot.start()
    except Exception as e:
        logger.error(f"Bot failed to start: {e}")
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot failed with error: {e}")
        raise