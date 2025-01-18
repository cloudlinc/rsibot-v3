import asyncio
from ib_insync import IB, Stock, MarketOrder, util
import pandas as pd
import pandas_ta as ta
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
BROKER_HOST = os.getenv("IB_HOST", "127.0.0.1")
BROKER_PORT = int(os.getenv("IB_PORT", 7497))
BROKER_CLIENT_ID = int(os.getenv("IB_CLIENT_ID", 999))

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

class RSIMACDTrader:
    def __init__(self, ib: IB):
        self.ib = ib
        logger.info("RSIMACDTrader initialized")

    async def run(self):
        logger.info("Starting trading bot...")
        while True:
            try:
                # 1. Fetch config from Supabase
                config = self.get_bot_config()
                logger.info(f"Loaded configuration: {config}")

                ticker = config.get('ticker', 'AAPL')
                rsi_buy = config.get('rsi_buy_threshold', 30)
                rsi_sell = config.get('rsi_sell_threshold', 70)
                macd_enabled = config.get('macd_enabled', True)
                manual_mode = config.get('manual_mode', False)
                shares_per_trade = config.get('shares_per_trade', 10)

                # 2. Fetch historical data from IB
                contract = Stock(ticker, 'SMART', 'USD')
                bars = self.ib.reqHistoricalData(
                    contract,
                    endDateTime='',
                    durationStr='1 D',
                    barSizeSetting='5 mins',
                    whatToShow='TRADES',
                    useRTH=False,
                    formatDate=1
                )
                
                if not bars:
                    logger.warning(f"No historical data received for {ticker}")
                    await asyncio.sleep(60)
                    continue

                df = util.df(bars)
                if len(df) < 50:
                    logger.warning("Not enough data to compute indicators")
                    await asyncio.sleep(60)
                    continue
                
                # 3. Compute RSI & MACD
                df['rsi'] = ta.rsi(df['close'], length=14)
                macd = ta.macd(df['close'], fast=12, slow=26, signal=9)
                df['macd'] = macd['MACD_12_26_9']
                df['macd_signal'] = macd['MACDs_12_26_9']

                current_rsi = df['rsi'].iloc[-1]
                current_macd = df['macd'].iloc[-1]
                current_macd_signal = df['macd_signal'].iloc[-1]

                logger.info(f"Current indicators - RSI: {current_rsi:.2f}, MACD: {current_macd:.2f}, MACD Signal: {current_macd_signal:.2f}")

                # 4. Determine trade signal
                position = self.get_current_position(ticker)
                logger.info(f"Current position for {ticker}: {position}")

                trade_signal = None

                # RSI-based signals with MACD confirmation
                if position == 0 and current_rsi < rsi_buy:
                    if not macd_enabled or (current_macd > current_macd_signal):
                        trade_signal = "BUY"
                        logger.info(f"Buy signal generated - RSI: {current_rsi:.2f}")
                elif position > 0 and current_rsi > rsi_sell:
                    if not macd_enabled or (current_macd < current_macd_signal):
                        trade_signal = "SELL"
                        logger.info(f"Sell signal generated - RSI: {current_rsi:.2f}")

                # 5. Handle trade execution
                if trade_signal:
                    if manual_mode:
                        logger.info(f"Manual mode: Creating pending trade for {trade_signal}")
                        self.insert_pending_trade(ticker, trade_signal, current_rsi, current_macd)
                    else:
                        logger.info(f"Auto mode: Executing {trade_signal} trade")
                        trade = self.execute_trade(contract, trade_signal, shares_per_trade)
                        if trade:
                            self.log_trade_in_supabase(ticker, trade_signal, current_rsi, current_macd)

            except Exception as e:
                logger.error(f"Error in main loop: {str(e)}")
                await asyncio.sleep(60)
                continue

            # Sleep before next iteration
            await asyncio.sleep(300)  # 5 minutes

    def get_bot_config(self):
        try:
            response = supabase.table("bot_config").select("*").execute()
            if response.data and len(response.data) > 0:
                return response.data[0]
        except Exception as e:
            logger.error(f"Error fetching bot config: {str(e)}")
        return {}

    def get_current_position(self, ticker):
        try:
            positions = self.ib.positions()
            for p in positions:
                if p.contract.symbol == ticker:
                    return p.position
        except Exception as e:
            logger.error(f"Error fetching positions: {str(e)}")
        return 0

    def insert_pending_trade(self, ticker, trade_signal, rsi, macd):
        try:
            data = {
                "ticker": ticker,
                "action": trade_signal,
                "rsi": float(rsi),
                "macd": float(macd),
                "status": "PENDING",
                "created_at": "now()"
            }
            supabase.table("trade_signals").insert(data).execute()
            logger.info(f"Inserted pending trade: {data}")
        except Exception as e:
            logger.error(f"Error inserting pending trade: {str(e)}")

    def execute_trade(self, contract, trade_signal, shares):
        try:
            order = None
            if trade_signal == "BUY":
                order = MarketOrder("BUY", shares)
            elif trade_signal == "SELL":
                order = MarketOrder("SELL", shares)

            if order:
                trade = self.ib.placeOrder(contract, order)
                self.ib.sleep(1)  # Wait for order processing
                logger.info(f"Trade executed: {trade_signal} {shares} shares of {contract.symbol}")
                return trade
        except Exception as e:
            logger.error(f"Error executing trade: {str(e)}")
        return None

    def log_trade_in_supabase(self, ticker, trade_signal, rsi, macd):
        try:
            data = {
                "ticker": ticker,
                "action": trade_signal,
                "rsi": float(rsi),
                "macd": float(macd),
                "executed_at": "now()"
            }
            supabase.table("trade_history").insert(data).execute()
            logger.info(f"Logged trade in Supabase: {data}")
        except Exception as e:
            logger.error(f"Error logging trade: {str(e)}")

async def main():
    try:
        ib = IB()
        ib.connect(BROKER_HOST, BROKER_PORT, clientId=BROKER_CLIENT_ID)
        logger.info(f"Connected to IB at {BROKER_HOST}:{BROKER_PORT}")
        
        trader = RSIMACDTrader(ib)
        await trader.run()
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
    finally:
        ib.disconnect()
        logger.info("Disconnected from IB")

if __name__ == "__main__":
    asyncio.run(main()) 