import os
import logging
import time
import uuid
import asyncio
import json
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Optional

import pandas as pd
import pandas_ta as ta
from dotenv import load_dotenv
from supabase import create_client
from ib_insync import IB, Stock, util, Trade, Order

# ---------------------------------
# 1) Logging Setup
# ---------------------------------
def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=os.environ.get("LOG_LEVEL", "INFO"),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            # Optionally log to file:
            # logging.FileHandler('/home/ubuntu/trading/logs/ibkr_trading.log')
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# ---------------------------------
# 2) Load Environment Variables
# ---------------------------------
logger.info("Loading environment variables...")
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
logger.info(f"Looking for .env file at: {ENV_PATH}")

if os.path.exists(ENV_PATH):
    logger.info("Found .env file")
    load_dotenv(ENV_PATH)
    logger.info("Environment variables loaded from .env file")
else:
    logger.warning("No .env file found")

env_vars = {}
keys_to_load = [
    "SUPABASE_URL",
    "SUPABASE_KEY",
    "IBKR_HOST",
    "IBKR_PORT",
    "IBKR_CLIENT_ID",
    "SYMBOLS",
    "RSI_PERIOD",
    "RSI_OVERBOUGHT",
    "RSI_OVERSOLD",
    "POSITION_SIZE",
]

for key in keys_to_load:
    value = os.environ.get(key)
    if key in ["SUPABASE_KEY"]:
        logger.info(f"Loaded {key}: {'***' if value else 'None'}")
    else:
        logger.info(f"Loaded {key}: {value}")
    env_vars[key] = value

# Basic checks (optional)
if not env_vars.get("IBKR_HOST"):
    logger.warning("IBKR_HOST is missing. Defaulting to 127.0.0.1")
if not env_vars.get("IBKR_PORT"):
    logger.warning("IBKR_PORT is missing. Defaulting to 7497")

# ---------------------------------
# 3) IBKR API Class
# ---------------------------------
class IBKRAPI:
    """
    Wrapper around the ib_insync IB() class that helps:
      - Connect/Disconnect
      - Retrieve positions
      - Retrieve historical data
      - Place trades
    """
    def __init__(self, host: str, port: int, client_id: int):
        self.host = host
        self.port = port
        self.client_id = client_id
        self.ib = IB()

    async def connect(self):
        """
        Connect to IBKR TWS or Gateway. 
        Since ib_insync is synchronous, we'll just run it in a thread executor or call directly.
        """
        logger.info(f"Connecting to IBKR at {self.host}:{self.port} with client ID {self.client_id}...")
        # We can do a simple synchronous connect:
        self.ib.connect(self.host, self.port, clientId=self.client_id)
        if self.ib.isConnected():
            logger.info("Successfully connected to IBKR.")
        else:
            raise ConnectionError("Could not connect to IBKR")

    async def disconnect(self):
        """Disconnect from IBKR."""
        logger.info("Disconnecting from IBKR...")
        self.ib.disconnect()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    async def get_positions(self) -> Dict[str, float]:
        """
        Retrieve open positions. 
        Returns a dictionary: symbol -> quantity (assuming stocks).
        """
        # Synchronous call
        positions = self.ib.positions()
        position_dict = {}
        for p in positions:
            # p.contract.symbol => symbol
            # p.position => float quantity
            if p.contract.secType == 'STK':
                symbol = p.contract.symbol
                qty = float(p.position)
                if qty != 0:
                    position_dict[symbol] = qty
        return position_dict

    async def get_historical_data(self, symbol: str, duration: str = '2 W', bar_size: str = '5 mins') -> pd.DataFrame:
        """
        Retrieve historical data for a given symbol.
        - `duration`: e.g. '2 W' for 2 weeks
        - `bar_size`: e.g. '5 mins', '1 day', etc.
        
        Returns a pandas DataFrame with columns: Date, Open, High, Low, Close, Volume
        """
        contract = Stock(symbol, 'SMART', 'USD')
        # Ensure IB has the contract details
        self.ib.qualifyContracts(contract)

        # Synchronous historical data call
        bars = self.ib.reqHistoricalData(
            contract,
            endDateTime='',
            durationStr=duration,
            barSizeSetting=bar_size,
            whatToShow='TRADES',  # or MIDPOINT, etc.
            useRTH=True,          # Only regular trading hours
            formatDate=1
        )
        if not bars:
            logger.warning(f"No historical data returned for {symbol}.")
            return pd.DataFrame()

        df = util.df(bars)
        # df typically has columns like: date, open, high, low, close, volume, barCount, WAP
        # For consistency with our RSI function, rename columns if needed
        df.rename(
            columns={
                'date': 'datetime',
                'open': 'open',
                'high': 'high',
                'low': 'low',
                'close': 'close',
                'volume': 'volume'
            },
            inplace=True
        )
        return df[['datetime', 'open', 'high', 'low', 'close', 'volume']]

    async def place_order(self, symbol: str, action: str, quantity: int) -> Optional[int]:
        """
        Place a MARKET order for the given symbol.
        Returns an order ID if successful, or None.
        """
        contract = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(contract)

        # Simple Market Order
        order = Order(
            action=action.upper(),  # 'BUY' or 'SELL'
            orderType='MKT',
            totalQuantity=quantity,
            tif='DAY'  # Good for day
        )
        # Place order
        trade = self.ib.placeOrder(contract, order)
        logger.info(f"Placed {action} order for {quantity} shares of {symbol} (orderId={trade.order.orderId})")

        return trade.order.orderId

    async def cancel_order(self, order_id: int):
        """
        Cancel an existing order by order_id.
        """
        logger.info(f"Attempting to cancel order ID {order_id}...")
        # We need to look up the trade by order_id
        for t in self.ib.trades():
            if t.order.orderId == order_id:
                self.ib.cancelOrder(t.order)
                return True
        logger.warning(f"No order found with ID {order_id}")
        return False


# ---------------------------------
# 4) RSI Trading Bot
# ---------------------------------
class RSITradingBot:
    def __init__(self):
        """Initialize the RSI trading bot."""
        logger.info("Initializing IBKR RSI Trading Bot...")

        # Supabase credentials
        self.supabase_url = env_vars["SUPABASE_URL"]
        self.supabase_key = env_vars["SUPABASE_KEY"]
        self.supabase = None
        if self.supabase_url and self.supabase_key:
            try:
                logger.info(f"Connecting to Supabase at {self.supabase_url}")
                self.supabase = create_client(self.supabase_url, self.supabase_key)
                logger.info("Successfully connected to Supabase.")
            except Exception as e:
                logger.error(f"Failed to initialize Supabase client: {e}")
                self.supabase = None
        else:
            logger.info("No Supabase credentials provided. Trade/performance logging will be disabled.")

        # IBKR connection details
        self.ibkr_host = env_vars.get("IBKR_HOST", "127.0.0.1")
        self.ibkr_port = int(env_vars.get("IBKR_PORT", "7497"))
        self.ibkr_client_id = int(env_vars.get("IBKR_CLIENT_ID", "123"))

        # RSI Trading parameters
        self.symbols = json.loads(env_vars["SYMBOLS"]) if env_vars["SYMBOLS"] else ["AAPL"]
        self.rsi_period = int(env_vars["RSI_PERIOD"]) if env_vars["RSI_PERIOD"] else 14
        self.rsi_overbought = float(env_vars["RSI_OVERBOUGHT"]) if env_vars["RSI_OVERBOUGHT"] else 70.0
        self.rsi_oversold = float(env_vars["RSI_OVERSOLD"]) if env_vars["RSI_OVERSOLD"] else 30.0
        self.position_size = float(env_vars["POSITION_SIZE"]) if env_vars["POSITION_SIZE"] else 10

        # Track pending orders
        self.pending_orders = {}  # symbol -> order_id

        # Current positions
        self.positions = {}

        # IBKR API client (initialized in start())
        self.api = None

    def calculate_rsi_from_df(self, df: pd.DataFrame) -> pd.Series:
        """
        Calculate RSI from a DataFrame containing columns: ['datetime','open','high','low','close','volume'].
        """
        if df.empty:
            return pd.Series(dtype=float)

        # We'll do a quick RSI approach (manually or via pandas_ta)
        # Manual approach:
        df['price_change'] = df['close'].diff()
        df['gain'] = df['price_change'].apply(lambda x: x if x > 0 else 0)
        df['loss'] = df['price_change'].apply(lambda x: abs(x) if x < 0 else 0)
        
        avg_gain = df['gain'].rolling(window=self.rsi_period).mean()
        avg_loss = df['loss'].rolling(window=self.rsi_period).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    async def calculate_rsi(self, symbol: str) -> float:
        """
        Retrieve data from IBKR, then calculate RSI. Returns the latest RSI value.
        """
        try:
            # Get ~2 weeks of data in 5-minute bars
            df = await self.api.get_historical_data(symbol, duration='2 W', bar_size='5 mins')
            if df.empty:
                logger.warning(f"No data returned for {symbol}, defaulting RSI to 50.")
                return 50.0

            # Calculate RSI
            rsi_series = self.calculate_rsi_from_df(df)
            if rsi_series.empty:
                logger.warning(f"No RSI data for {symbol}, defaulting to 50.")
                return 50.0
            current_rsi = rsi_series.iloc[-1]
            logger.info(f"Calculated RSI for {symbol}: {current_rsi:.2f}")
            return current_rsi
        except Exception as e:
            logger.error(f"Error calculating RSI for {symbol}: {e}")
            return 50.0

    async def log_trade(self, symbol: str, action: str, rsi_value: float):
        """
        Log a trade to Supabase (if available).
        """
        if not self.supabase:
            return
        try:
            now_utc = datetime.now(timezone.utc).isoformat()
            data = {
                'symbol': symbol,
                'action': action,
                'rsi': float(rsi_value),
                'timestamp': now_utc
            }
            self.supabase.table('trades').insert(data).execute()
            logger.info(f"Trade logged in Supabase: {data}")
        except Exception as e:
            logger.error(f"Failed to log trade to Supabase: {e}")

    async def log_performance(self, symbol: str, closing_price: float, rsi_value: float, position_size: float, pnl: float):
        """
        Log performance metrics to Supabase (if available).
        """
        if not self.supabase:
            return
        try:
            data = {
                'symbol': symbol,
                'date': datetime.now(timezone.utc).date().isoformat(),
                'closing_price': float(closing_price),
                'rsi_value': float(rsi_value),
                'position_size': float(position_size),
                'pnl': float(pnl),
                'created_at': datetime.now(timezone.utc).isoformat()
            }
            self.supabase.table('performance_metrics').insert(data).execute()
            logger.info(f"Performance logged in Supabase: {data}")
        except Exception as e:
            logger.error(f"Failed to log performance: {e}")

    async def check_market_hours(self) -> bool:
        """
        Check if the market is open. Basic approach: 9:30am-4:00pm US/Eastern.
        For a real approach, consider using IBKR calendars or queries.
        """
        now_utc = datetime.now(timezone.utc)
        if now_utc.weekday() >= 5:  # Sat (5) or Sun (6)
            return False
        # Approx check for US/Eastern
        # 9:30am ET = 13:30 UTC
        # 4:00pm ET = 20:00 UTC
        ny_time = now_utc.astimezone(timezone.utc)
        market_open = ny_time.replace(hour=13, minute=30, second=0)
        market_close = ny_time.replace(hour=20, minute=0, second=0)
        return market_open <= ny_time <= market_close

    async def update_positions(self):
        """
        Update current positions from IBKR.
        """
        self.positions = await self.api.get_positions()

    async def process_symbol(self, symbol: str):
        """
        Check RSI for a symbol, place trades if signals are triggered.
        """
        try:
            await self.update_positions()
            current_rsi = await self.calculate_rsi(symbol)
            logger.info(f"{symbol} RSI: {current_rsi}")

            current_position = self.positions.get(symbol, 0.0)

            # If there's a pending order, optionally cancel it if you want 
            # (similar to your Schwab code). For brevity, let's omit here.
            
            # Example: If RSI < RSI_OVERSOLD => buy
            if current_rsi <= self.rsi_oversold and current_position == 0:
                order_id = await self.api.place_order(symbol, 'BUY', int(self.position_size))
                if order_id:
                    await self.log_trade(symbol, 'BUY', current_rsi)
                    logger.info(f"Bought {self.position_size} shares of {symbol}")

            # If RSI > RSI_OVERBOUGHT => sell existing positions
            elif current_rsi >= self.rsi_overbought and current_position > 0:
                order_id = await self.api.place_order(symbol, 'SELL', int(current_position))
                if order_id:
                    await self.log_trade(symbol, 'SELL', current_rsi)
                    logger.info(f"Sold {current_position} shares of {symbol}")

        except Exception as e:
            logger.error(f"Error processing {symbol}: {e}")

    async def start(self):
        """
        Initialize and start the bot. 
        Sets up IBKRAPI, connects, then calls run().
        """
        logger.info("Starting IBKR RSI Trading Bot...")
        self.api = IBKRAPI(self.ibkr_host, self.ibkr_port, self.ibkr_client_id)
        try:
            await self.api.connect()
            try:
                await self.run()
            finally:
                await self.api.disconnect()
        except Exception as e:
            logger.error(f"Error starting bot: {e}")
            raise

    async def run(self):
        """
        Main loop that runs indefinitely, checking RSI signals periodically.
        """
        logger.info("Entering main loop...")
        while True:
            try:
                # Check if market is open
                if await self.check_market_hours():
                    logger.info("Market is open, processing symbols...")
                    for symbol in self.symbols:
                        await self.process_symbol(symbol)
                    logger.info("Finished processing all symbols.")
                else:
                    logger.info("Market is closed, waiting for next check.")
                
                logger.info("Waiting 60 seconds before next cycle...")
                await asyncio.sleep(60)
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                logger.info("Waiting 60 seconds before retry...")
                await asyncio.sleep(60)

# ---------------------------------
# 5) Main Entry Point
# ---------------------------------
async def main():
    """Main entry point for the trading bot."""
    try:
        logger.info("Launching IBKR RSI Trading Bot...")
        bot = RSITradingBot()
        await bot.start()
    except Exception as e:
        logger.error(f"Bot failed to start: {e}")
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error(f"Bot failed with error: {e}")
        raise