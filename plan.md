Below is a high-level guide and reference architecture on how you might build, deploy, and maintain a 24/7 trading bot using RSI and MACD signals, integrated with a broker like Interactive Brokers (via IBKR API or a library such as ib_insync), storing and retrieving configuration/trade data in Supabase, and wrapping the entire system in Docker for easy, repeatable deployments (e.g., on Amazon Lightsail or DigitalOcean).

1. Architecture Overview
	1.	Core Trading Bot (Python)
	•	Uses Python libraries (e.g., ta or pandas_ta for RSI/MACD calculations).
	•	Communicates with Interactive Brokers or Schwab API to place trades.
	•	Periodically checks Supabase for configuration settings (RSI thresholds, stock ticker, strategy parameters, auto/manual mode, etc.).
	•	Logs completed trades and relevant metrics to Supabase.
	2.	Supabase
	•	Acts as your database for storing:
	•	Bot Configuration: Tickers, RSI thresholds, MACD parameters, timeframe, etc.
	•	Trade History: Executed trades, timestamps, P&L, etc.
	•	Also used as a common backend for your Next.js website so that users can configure the bot or review pending trades in “manual approval” mode.
	3.	Next.js Website (Manual Review / Dashboard)
	•	Uses Supabase as the backend (both for user authentication, possibly, and reading/updating configurations/trade records).
	•	“Manual Review” feature can be implemented by having the bot mark a pending trade entry in Supabase. Then, your Next.js site can show that pending trade to the user, who either approves or rejects it. On approval, the bot sees that in Supabase and executes the trade.
	4.	Deployment & Hosting
	•	Containerize the bot with Docker, specifying all dependencies for Python, broker API libraries, and environment variables (for broker credentials, Supabase credentials, etc.).
	•	Host on Amazon Lightsail or DigitalOcean with an Ubuntu instance.
	•	(Optionally) attach a simple CI/CD pipeline or shell script that pulls your source from Git (or a container registry), builds the Docker image, and runs the container.
	5.	Automation Script
	•	A single shell script or small CI pipeline that:
	1.	Reads your custom variables (API keys, different tickers, timeframes, RSI thresholds, etc.).
	2.	Builds the Docker image with those environment variables baked in or passed in.
	3.	Deploys the container to your hosting provider.

2. Bot Logic (RSI & MACD)

RSI (Relative Strength Index)
	•	RSI is a momentum oscillator measured on a 0–100 scale.
	•	Overbought signal is typically above 70, oversold signal is typically below 30.
	•	Your requirements:
	•	Buy when RSI goes below 30 (oversold).
	•	Sell when RSI goes above 70 (overbought).

MACD (Moving Average Convergence Divergence)
	•	MACD is composed of two lines: the MACD line (difference of two EMAs) and a signal line (EMA of MACD line).
	•	A bullish trend is often spotted when the MACD line crosses above the signal line; a bearish trend is typically when the MACD line crosses below the signal line.
	•	You mentioned “considering the MACD trend.” Usually, that means:
	•	Only buy if MACD is bullish (e.g., MACD line above signal line).
	•	Only sell if MACD is bearish (e.g., MACD line below signal line).
	•	You can fine-tune this logic (e.g., read from Supabase how many periods you want to confirm the trend).

Combining RSI & MACD

One straightforward approach is:
	1.	Check RSI:
	•	If below 30, candidate to buy.
	•	If above 70, candidate to sell.
	2.	If candidate to buy, confirm that MACD is bullish.
	3.	If candidate to sell, confirm that MACD is bearish.

Alternatively, you could simply use RSI for entry and exit signals, but filter out trades that don’t align with the MACD direction.

3. Using Python for the Bot

Below is a simplified example showing how you might structure a Python bot. This example uses:
	•	ib_insync for Interactive Brokers connectivity. (If using Schwab or another broker, you’d swap in their API library or a wrapper library.)
	•	pandas_ta for RSI and MACD. (You could also use TA-Lib or any other technical analysis library.)
	•	asyncpg or supabase-py for database access to Supabase. (Note: The Supabase folks provide a Python client that wraps PostgREST calls. Check Supabase docs for details.)

	Note: This is not a production-ready code snippet. It’s a skeleton to illustrate the approach.

import asyncio
from ib_insync import IB, Stock, util
import pandas as pd
import pandas_ta as ta
import os

# For Supabase
# pip install supabase
from supabase import create_client, Client

# Example environment variables (better to inject in Docker or store in .env)
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

    async def run(self):
        while True:
            # 1. Fetch config from Supabase
            #    Example: get { "ticker": "AAPL", "rsi_buy_threshold": 30, "rsi_sell_threshold": 70, ... }
            config = self.get_bot_config()

            ticker = config.get('ticker', 'AAPL')
            rsi_buy = config.get('rsi_buy_threshold', 30)
            rsi_sell = config.get('rsi_sell_threshold', 70)
            macd_enabled = config.get('macd_enabled', True)
            manual_mode = config.get('manual_mode', False)

            # 2. Fetch historical data from IB to calculate indicators
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
            df = util.df(bars)
            if len(df) < 50:
                print("Not enough data to compute indicators.")
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

            # 4. Determine trade signal
            position = self.get_current_position(ticker)  # from broker or from your internal records

            trade_signal = None

            # RSI-based signals
            if position == 0 and current_rsi < rsi_buy:
                # Potential buy signal
                if not macd_enabled or (current_macd > current_macd_signal):
                    trade_signal = "BUY"
            elif position > 0 and current_rsi > rsi_sell:
                # Potential sell signal
                if not macd_enabled or (current_macd < current_macd_signal):
                    trade_signal = "SELL"

            # 5. If there's a trade signal and we are in automatic mode, place the trade
            #    If we are in manual mode, insert a 'pending' trade into Supabase for user to confirm
            if trade_signal:
                if manual_mode:
                    self.insert_pending_trade(ticker, trade_signal, current_rsi, current_macd)
                else:
                    self.execute_trade(contract, trade_signal)
                    self.log_trade_in_supabase(ticker, trade_signal, current_rsi, current_macd)

            # Sleep before next iteration (e.g., 5 minutes)
            await asyncio.sleep(300)

    def get_bot_config(self):
        # Example fetching from "bot_config" table with a single config row
        response = supabase.table("bot_config").select("*").execute()
        if response.data and len(response.data) > 0:
            return response.data[0]
        return {}

    def get_current_position(self, ticker):
        # For example, read from IB directly or from your own trade records in Supabase
        # This is simplified for illustration
        positions = self.ib.positions()
        for p in positions:
            if p.contract.symbol == ticker:
                return p.position
        return 0

    def insert_pending_trade(self, ticker, trade_signal, rsi, macd):
        # Insert a record indicating a pending trade
        data = {
            "ticker": ticker,
            "action": trade_signal,
            "rsi": rsi,
            "macd": macd,
            "status": "PENDING"
        }
        supabase.table("trade_signals").insert(data).execute()

    def execute_trade(self, contract, trade_signal):
        # Market order for illustration
        order = None
        if trade_signal == "BUY":
            order = MarketOrder("BUY", 10)
        elif trade_signal == "SELL":
            order = MarketOrder("SELL", 10)

        if order:
            trade = self.ib.placeOrder(contract, order)
            self.ib.sleep(1)  # Wait to ensure order is processed
            return trade

    def log_trade_in_supabase(self, ticker, trade_signal, rsi, macd):
        supabase.table("trade_history").insert({
            "ticker": ticker,
            "action": trade_signal,
            "rsi": rsi,
            "macd": macd,
            "executed_at": "now()"
        }).execute()

async def main():
    ib = IB()
    ib.connect(BROKER_HOST, BROKER_PORT, clientId=BROKER_CLIENT_ID)
    trader = RSIMACDTrader(ib)
    await trader.run()

if __name__ == "__main__":
    asyncio.run(main())

Notes on the Example
	•	Supabase: The code above uses the official supabase-py library to demonstrate how you might read and write data.
	•	Manual Mode:
	•	If manual_mode == True, your bot does not automatically execute trades. Instead, it inserts a “pending” trade into a trade_signals table on Supabase.
	•	Your Next.js site will display these pending signals to the user, who can approve or reject them.
	•	On approval, you could either have the site call a small REST endpoint in your bot or flip the status in the same table (e.g., from PENDING to APPROVED), which your bot checks regularly and then executes.

4. Dockerizing the Bot

Below is a simple Dockerfile you could use. This example assumes your Python source code is in the same directory.

# Use a Python base image
FROM python:3.10-slim

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libta-lib0 \
    ta-lib \
    && rm -rf /var/lib/apt/lists/*

# Copy your requirements file
COPY requirements.txt /app/
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your bot source code
COPY . /app

# Expose port if you have an HTTP endpoint (not required for pure cron-like service)
# EXPOSE 8000 

# Run your bot
CMD ["python", "my_bot.py"]

Example requirements.txt

ib_insync==0.9.70
pandas==1.5.0
pandas_ta==0.3.14b0
supabase==0.0.0  # pin the version you need
asyncio

(Adjust versions to your preference.)

5. Deployment Script / Best Practices
	1.	Build the Docker image locally or in a CI pipeline:

docker build -t my-rsi-bot .


	2.	Push the image to a container registry (e.g., Docker Hub or AWS ECR):

docker tag my-rsi-bot:latest <YOUR_REGISTRY>/my-rsi-bot:latest
docker push <YOUR_REGISTRY>/my-rsi-bot:latest


	3.	On your remote host (e.g., Amazon Lightsail or DigitalOcean), run:

docker pull <YOUR_REGISTRY>/my-rsi-bot:latest
docker run -d \
  --name my-rsi-bot \
  -e SUPABASE_URL="..." \
  -e SUPABASE_ANON_KEY="..." \
  -e IB_HOST="..." \
  -e IB_PORT="..." \
  -e IB_CLIENT_ID="..." \
  <YOUR_REGISTRY>/my-rsi-bot:latest

	4.	If you want to auto-deploy on code changes, you can set up a simple CI/CD pipeline (GitHub Actions, GitLab CI, etc.) that triggers on push to main. The pipeline can build and push the Docker image, then you can have a shell script or service on your VPS that runs docker pull && docker run again (or an orchestration solution like Docker Compose, ECS, or Kubernetes).

6. Integrating with Next.js
	•	Next.js + Supabase: You can easily read and write from the same tables (bot_config, trade_history, trade_signals) using the Supabase JavaScript client.
	•	For manual approvals:
	1.	When the bot inserts a record to trade_signals (status = “PENDING”), your Next.js site can subscribe to changes on that table using Supabase’s realtime features or just poll it.
	2.	The user sees a “Pending trade for AAPL: BUY 10 shares.”
	3.	The user clicks Approve → you update the record’s status to “APPROVED.”
	4.	The bot can be continuously monitoring that table for entries that changed to “APPROVED,” or you can have the Next.js site call a small REST endpoint in the bot (if you expose one) which places the trade immediately.

8. Next Steps & Best Practices
	1.	Stop-Loss / Take-Profit:
	•	RSI and MACD alone are not risk management. You’ll want to incorporate a stop-loss or trailing stop to protect capital.
	2.	Position Sizing:
	•	The example code is naive (buy or sell 10 shares). In a real system, consider your capital, max risk per trade, etc.
	3.	Error Handling:
	•	Consider the reliability of your broker’s API, network errors, etc.
	4.	Securely Store Credentials:
	•	Use environment variables, secrets managers, or a secure store so that you don’t leak API keys into logs or Git repos.
	5.	Scaling:
	•	If you want multiple bots with different ticker/RSI settings, you can run multiple Docker containers, each with a different environment variable set or config.
	•	Your single codebase can check a “bot_id” or “strategy_id” column in the DB to decide which strategy or ticker to run.

9. Conclusion

By combining:
	1.	Python (with a library like ib_insync or your broker’s official API),
	2.	Technical Analysis (via pandas_ta or TA-Lib),
	3.	Supabase (for configuration, trade logs, and synergy with your Next.js site),
	4.	Docker (for consistent 24/7 deployment on a cloud VPS),

you’ll have a flexible, maintainable trading bot that can respond to RSI/MACD signals, run in manual or auto mode, and record everything for reporting and analytics.