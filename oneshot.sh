#!/bin/bash
#
# deploy_rsi_bot.sh
#
# Deploy a self-contained RSI-based trading bot onto a fresh Ubuntu droplet on DigitalOcean.
# - No Docker or GitHub needed; everything is inline in this script.
# - Requires 'doctl' CLI installed and configured locally.
#
# Usage:
#   export DO_TOKEN="dop_v1_abc123..."
#   export SSH_KEY_NAME="my-trading-key"
#   ./deploy_rsi_bot.sh
#

###################################
# 0) Configuration
###################################
# DigitalOcean settings
DO_TOKEN=${DO_TOKEN:-"dop_v1_e3148d56db62bb0a574b1271540498367804099a710254c6cf607f843aa284c0"}
SSH_KEY_NAME=${SSH_KEY_NAME:-"44956302"}
DROPLET_NAME="rsi-bot-droplet"
DROPLET_REGION="nyc1"
DROPLET_SIZE="s-1vcpu-1gb"  # pick your droplet size
IMAGE="ubuntu-22-04-x64"

# If you'd like, you can parameterize these as well
SSH_USER="root"

###################################
# 1) Validate 'doctl' and DO_TOKEN
###################################
if ! command -v doctl &> /dev/null; then
  echo "ERROR: 'doctl' is not installed or not in PATH."
  echo "See: https://docs.digitalocean.com/reference/doctl/how-to/install/"
  exit 1
fi

if [ -z "$DO_TOKEN" ]; then
  echo "ERROR: DO_TOKEN is not set. Please export DO_TOKEN with your DO API token."
  echo "  e.g. export DO_TOKEN='dop_v1_...' "
  exit 1
fi

###################################
# 2) Auth with DigitalOcean
###################################
echo "Authenticating with DigitalOcean using token..."
doctl auth init -t "$DO_TOKEN"

###################################
# 3) Create Droplet
###################################
echo "Creating droplet '$DROPLET_NAME'..."
CREATE_OUTPUT=$(doctl compute droplet create "$DROPLET_NAME" \
  --region "$DROPLET_REGION" \
  --size "$DROPLET_SIZE" \
  --image "$IMAGE" \
  --enable-private-networking \
  --ssh-keys "$SSH_KEY_NAME" \
  --wait \
  --format "ID,Name,PublicIPv4,Memory,VCPUs,Disk,Region" \
  --no-header)

if [ $? -ne 0 ]; then
  echo "ERROR: Failed to create droplet."
  exit 1
fi

# Extract the droplet IP address
DROPLET_IP=$(echo "$CREATE_OUTPUT" | awk '{print $3}')
if [ -z "$DROPLET_IP" ]; then
  echo "ERROR: Could not parse droplet IP address from create output."
  echo "$CREATE_OUTPUT"
  exit 1
fi

echo "Droplet created. IP: $DROPLET_IP"
echo "Waiting ~90 seconds for SSH to be ready..."
sleep 90

###################################
# 4) Build the remote bootstrap script
###################################
# This script will run on the droplet to:
#   - Install system dependencies
#   - Create /bot directory
#   - Write your main.py code (inline below)
#   - Write requirements.txt
#   - Create venv & install requirements
#   - Create systemd service
#   - Start the bot
#
# IMPORTANT:
#   In the 'INLINE_MAIN_PY' section, replace the placeholder code with your RSI logic,
#   or any Python code you want to run continuously.

echo "Running bootstrap script on droplet $DROPLET_IP ..."
ssh -o StrictHostKeyChecking=no "$SSH_USER@$DROPLET_IP" "bash -s" << 'END_BOOTSTRAP'
#!/bin/bash
set -e

# 1. Update/upgrade packages & install dependencies
apt-get update -y
apt-get upgrade -y
apt-get install -y python3 python3-pip python3-venv unzip xvfb libxslt1.1 libxrender1 libxtst6 libxi6 libgtk2.0-0

# Create IB Gateway directory
IBGW_DIR="/root/ibgateway"
mkdir -p "$IBGW_DIR"
cd "$IBGW_DIR"

# Download and install IB Gateway
echo "Downloading IB Gateway..."
wget -q https://download2.interactivebrokers.com/installers/ibgateway/latest-standalone/ibgateway-latest-standalone-linux-x64.sh

# Make installer executable
chmod +x ibgateway-latest-standalone-linux-x64.sh

# Run installer in silent mode
echo "Installing IB Gateway..."
./ibgateway-latest-standalone-linux-x64.sh -q -dir "$IBGW_DIR"

# Create IBC configuration
mkdir -p "$IBGW_DIR/ibc"
cd "$IBGW_DIR/ibc"

# Download and install IBC (Interactive Brokers Controller)
echo "Downloading IBC..."
wget -q https://github.com/IbcAlpha/IBC/releases/download/3.15.2/IBCLinux-3.15.2.zip
unzip -q IBCLinux-3.15.2.zip
chmod +x scripts/*

# Configure IBC
cat << 'CONFIG_EOF' > config.ini
LoginId=scap3883
Password=XMVSKhajEx9ZN!Q
FIXLoginId=
FIXPassword=
TradingMode=paper
IbLoginId=
IbPassword=
StoreSettingsOnServer=no
MinimizeMainWindow=no
ExistingSessionDetectedAction=primary
AcceptIncomingConnectionAction=accept
ShowAllTrades=no
ForceTWS=no
ReadOnlyLogin=no
AcceptNonBrokerageAccountWarning=yes
IbDir=$IBGW_DIR
Gateway=true
ConfigPath=${IBGW_DIR}/jts.ini
LogPath=${IBGW_DIR}/logs
JavaPath=
StartupScript=
ShutdownScript=
IbAutoClosedown=no
ClosedownAt=
AllowMultipleSetups=no
SaveTwsSettingsAt=
FocusOnMainWindow=no
ReloginAfterRestart=no
SendTWSLogsToConsole=no
PrintRequests=no
PrintReplies=no
LogComponents=never
CONFIG_EOF

# Create a startup script for IB Gateway
cat << 'STARTUP_EOF' > /root/start-ibgateway.sh
#!/bin/bash

# Start Xvfb
Xvfb :1 -screen 0 1024x768x24 &
export DISPLAY=:1

# Wait for Xvfb to start
sleep 5

# Start IB Gateway using IBC
cd /root/ibgateway/ibc
./scripts/ibcstart.sh
STARTUP_EOF

chmod +x /root/start-ibgateway.sh

# Create systemd service for IB Gateway
cat << 'SERVICE_EOF' > /etc/systemd/system/ibgateway.service
[Unit]
Description=Interactive Brokers Gateway
After=network.target

[Service]
Type=simple
User=root
ExecStart=/root/start-ibgateway.sh
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
SERVICE_EOF

# Enable and start IB Gateway service
systemctl daemon-reload
systemctl enable ibgateway
systemctl start ibgateway

# Wait for IB Gateway to start and check its status
echo "Waiting for IB Gateway to start..."
sleep 30
systemctl status ibgateway

# 2. Make a bot directory
BOT_DIR="/bot"
mkdir -p "$BOT_DIR"
cd "$BOT_DIR"

# 3. Write main.py inline
cat << 'EOF' > main.py
## ===============================================
## main.py (RSI Trading Bot) - Complete Implementation
## ===============================================
import asyncio
import logging
import os
import time
from datetime import datetime, timezone
import pandas as pd
import pandas_ta as ta
from supabase import create_client, Client
from ib_insync import *

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

# IBKR Configuration
IBKR_USERNAME = os.getenv("IBKR_USERNAME", "scap3883")
IBKR_PASSWORD = os.getenv("IBKR_PASSWORD", "XMVSKhajEx9ZN!Q")
IBKR_PORT = int(os.getenv("IBKR_PORT", "7497"))  # 7497 for paper trading

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://rvtipaoffmymdzqqzuxo.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ2dGlwYW9mZm15bWR6cXF6dXhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDU2MjE2NzAsImV4cCI6MjAyMTE5NzY3MH0.Ue_Ry_epqgXIGYQFXE5umxXM5dtCUqJG-jGwXxGYYtY")

# Trading parameters
SYMBOLS = ["AAPL", "MSFT", "GOOGL"]  # Stocks to monitor
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
POSITION_SIZE = 100  # Number of shares per trade

class IBKRConnection:
    def __init__(self):
        self.ib = IB()
        self.connected = False

    async def connect(self):
        try:
            if not self.connected:
                await self.ib.connectAsync('localhost', IBKR_PORT, clientId=1)
                self.connected = True
                logger.info("Successfully connected to IBKR")
        except Exception as e:
            logger.error(f"Failed to connect to IBKR: {e}")
            raise

    async def disconnect(self):
        if self.connected:
            self.ib.disconnect()
            self.connected = False

    async def get_historical_data(self, symbol):
        contract = Stock(symbol, 'SMART', 'USD')
        bars = await self.ib.reqHistoricalDataAsync(
            contract,
            endDateTime='',
            durationStr='2 D',
            barSizeSetting='1 min',
            whatToShow='TRADES',
            useRTH=True
        )
        return util.df(bars)

    async def place_order(self, symbol, action, quantity):
        contract = Stock(symbol, 'SMART', 'USD')
        order = MarketOrder(action, quantity)
        trade = await self.ib.placeOrderAsync(contract, order)
        return trade

class RSITradingBot:
    def __init__(self):
        self.ibkr = IBKRConnection()
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.positions = {}

    def calculate_rsi(self, df):
        return ta.rsi(df['close'], length=RSI_PERIOD)

    async def log_trade(self, symbol, action, rsi_value):
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

    async def check_market_hours(self):
        now = datetime.now(timezone.utc)
        if now.weekday() >= 5:  # Weekend
            return False
        ny_time = now.replace(tzinfo=timezone.utc).astimezone(timezone.utc)
        market_open = ny_time.replace(hour=13, minute=30, second=0)  # 9:30 AM ET
        market_close = ny_time.replace(hour=20, minute=0, second=0)  # 4:00 PM ET
        return market_open <= ny_time <= market_close

    async def process_symbol(self, symbol):
        try:
            df = await self.ibkr.get_historical_data(symbol)
            if df.empty:
                logger.warning(f"No data received for {symbol}")
                return

            rsi = self.calculate_rsi(df)
            current_rsi = rsi.iloc[-1]
            logger.info(f"{symbol} RSI: {current_rsi}")

            if current_rsi <= RSI_OVERSOLD and symbol not in self.positions:
                # Buy signal
                trade = await self.ibkr.place_order(symbol, 'BUY', POSITION_SIZE)
                self.positions[symbol] = POSITION_SIZE
                await self.log_trade(symbol, 'BUY', current_rsi)
                logger.info(f"Bought {POSITION_SIZE} shares of {symbol}")

            elif current_rsi >= RSI_OVERBOUGHT and symbol in self.positions:
                # Sell signal
                trade = await self.ibkr.place_order(symbol, 'SELL', self.positions[symbol])
                del self.positions[symbol]
                await self.log_trade(symbol, 'SELL', current_rsi)
                logger.info(f"Sold {POSITION_SIZE} shares of {symbol}")

        except Exception as e:
            logger.error(f"Error processing {symbol}: {e}")

    async def run(self):
        try:
            await self.ibkr.connect()
            
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
            await self.ibkr.disconnect()

if __name__ == "__main__":
    bot = RSITradingBot()
    asyncio.run(bot.run())
EOF

# 4. Write requirements.txt
cat << 'EOF' > requirements.txt
pandas==2.1.4
pandas-ta==0.3.14b0
supabase==2.3.0
ib-insync==0.9.86
EOF

# 5. Create venv and install requirements
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 6. Create systemd service
cat << 'EOF' > /etc/systemd/system/rsi-bot.service
[Unit]
Description=RSI Trading Bot
After=network.target ibgateway.service

[Service]
Type=simple
User=root
WorkingDirectory=/bot
Environment=PYTHONUNBUFFERED=1
ExecStart=/bot/venv/bin/python main.py
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
EOF

# 7. Enable and start the service
systemctl daemon-reload
systemctl enable rsi-bot
systemctl start rsi-bot

echo "Bootstrap complete!"
END_BOOTSTRAP

echo "Setup completed successfully!"