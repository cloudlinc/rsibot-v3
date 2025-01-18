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

read -r -d '' BOOTSTRAP_SCRIPT << 'END_BOOTSTRAP'
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

# Create systemd service for IB Gateway
cat << SERVICE_EOF > /etc/systemd/system/ibgateway.service
[Unit]
Description=Interactive Brokers Gateway
After=network.target

[Service]
Type=simple
User=root
Environment="DISPLAY=:1"
ExecStartPre=/usr/bin/Xvfb :1 -screen 0 1024x768x24 &
ExecStart=$IBGW_DIR/ibc/scripts/ibcstart.sh
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
SERVICE_EOF

# Enable and start IB Gateway service
systemctl daemon-reload
systemctl enable ibgateway
systemctl start ibgateway

# Wait for IB Gateway to start
echo "Waiting for IB Gateway to start..."
sleep 30

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
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ2dGlwYW9mZm15bWR6cXF6dXhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY4Njk2MTksImV4cCI6MjA1MjQ0NTYxOX0.A1UEMtMauspO8UVdl5ikaOzGA-TYr7v90oLFKWnffFM")

# Initialize Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Trading configuration
SYMBOLS = ["AAPL", "MSFT", "GOOGL"]  # List of stocks to monitor
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
CHECK_INTERVAL = 300  # 5 minutes
POSITION_SIZE = 100  # Number of shares per trade

class IBKRConnection:
    def __init__(self):
        self.ib = IB()
        self.connected = False

    async def connect(self):
        try:
            if not self.connected:
                logger.info("Connecting to IBKR...")
                self.ib.connect('127.0.0.1', IBKR_PORT, clientId=1)
                await asyncio.sleep(1)  # Wait for connection
                self.connected = True
                logger.info("Connected to IBKR successfully")
        except Exception as e:
            logger.error(f"Failed to connect to IBKR: {e}")
            self.connected = False
            raise

    async def disconnect(self):
        if self.connected:
            self.ib.disconnect()
            self.connected = False
            logger.info("Disconnected from IBKR")

    def get_contract(self, symbol):
        return Stock(symbol, 'SMART', 'USD')

    async def get_historical_data(self, symbol):
        try:
            contract = self.get_contract(symbol)
            bars = self.ib.reqHistoricalData(
                contract,
                endDateTime='',
                durationStr='5 D',
                barSizeSetting='1 hour',
                whatToShow='TRADES',
                useRTH=True
            )
            df = util.df(bars)
            return df
        except Exception as e:
            logger.error(f"Error fetching historical data for {symbol}: {e}")
            return None

    async def place_order(self, symbol, action, quantity):
        try:
            contract = self.get_contract(symbol)
            order = MarketOrder(action, quantity)
            trade = self.ib.placeOrder(contract, order)
            while not trade.isDone():
                await asyncio.sleep(1)
            logger.info(f"Order completed: {symbol} {action} {quantity} shares")
            return trade
        except Exception as e:
            logger.error(f"Error placing order for {symbol}: {e}")
            return None

def calculate_rsi(data: pd.DataFrame, period: int = 14) -> float:
    """Calculate RSI for the given data."""
    try:
        rsi = ta.rsi(data['close'], length=period)
        return float(rsi.iloc[-1])
    except Exception as e:
        logger.error(f"Error calculating RSI: {e}")
        return None

async def log_to_supabase(symbol: str, rsi: float, price: float, action: str = None):
    """Log trading data to Supabase."""
    try:
        data = {
            "symbol": symbol,
            "rsi": rsi,
            "price": price,
            "action": action,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        result = supabase.table("trading_logs").insert(data).execute()
        logger.info(f"Logged to Supabase: {data}")
        return result
    except Exception as e:
        logger.error(f"Error logging to Supabase: {e}")
        return None

async def process_symbol(ibkr: IBKRConnection, symbol: str):
    """Process a single symbol."""
    try:
        # 1. Fetch historical data
        df = await ibkr.get_historical_data(symbol)
        if df is None or df.empty:
            logger.error(f"No data received for {symbol}, skipping")
            return

        # 2. Calculate RSI
        current_price = float(df['close'].iloc[-1])
        rsi = calculate_rsi(df, RSI_PERIOD)
        
        if rsi is None:
            logger.error(f"Failed to calculate RSI for {symbol}")
            return

        # 3. Log current state
        logger.info(f"Symbol: {symbol}, Price: {current_price:.2f}, RSI: {rsi:.2f}")

        # 4. Generate and execute trading signals
        action = None
        if rsi > RSI_OVERBOUGHT:
            logger.info(f"{symbol} - SELL Signal - RSI: {rsi:.2f}")
            trade = await ibkr.place_order(symbol, "SELL", POSITION_SIZE)
            action = "SELL"
        elif rsi < RSI_OVERSOLD:
            logger.info(f"{symbol} - BUY Signal - RSI: {rsi:.2f}")
            trade = await ibkr.place_order(symbol, "BUY", POSITION_SIZE)
            action = "BUY"

        # 5. Log to Supabase
        await log_to_supabase(symbol, rsi, current_price, action)

    except Exception as e:
        logger.error(f"Error processing {symbol}: {e}")

async def main():
    logger.info("RSI Trading Bot starting...")
    ibkr = IBKRConnection()
    
    while True:
        try:
            # Connect to IBKR
            await ibkr.connect()

            if is_market_open():
                # Process all symbols concurrently
                await asyncio.gather(*[process_symbol(ibkr, symbol) for symbol in SYMBOLS])
            else:
                logger.info("Market is closed. Waiting...")
                await asyncio.sleep(CHECK_INTERVAL)
                continue

        except Exception as e:
            logger.error(f"Error in main loop: {e}")
            await ibkr.disconnect()  # Disconnect on error
            await asyncio.sleep(60)  # Wait before retrying
            continue

        await asyncio.sleep(CHECK_INTERVAL)

def is_market_open() -> bool:
    """Check if US stock market is open."""
    now = datetime.now(timezone.utc)
    if now.weekday() > 4:  # Weekend
        return False
    et_hour = (now.hour - 4) % 24  # UTC-4 for ET
    return 9.5 <= et_hour < 16  # 9:30 AM - 4:00 PM ET

if __name__ == "__main__":
    asyncio.run(main())
EOF

# 4. Write requirements.txt inline
cat << 'EOF' > requirements.txt
pandas==2.1.4
pandas-ta==0.3.14b0
supabase==1.0.3
ib_insync==0.9.86
python-dotenv==1.0.0
EOF

# 5. Create a python venv + install deps
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 6. Create .env file for configuration
cat << 'ENV_EOF' > .env
IBKR_USERNAME=scap3883
IBKR_PASSWORD=XMVSKhajEx9ZN!Q
IBKR_PORT=7497
SUPABASE_URL=https://rvtipaoffmymdzqqzuxo.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ2dGlwYW9mZm15bWR6cXF6dXhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY4Njk2MTksImV4cCI6MjA1MjQ0NTYxOX0.A1UEMtMauspO8UVdl5ikaOzGA-TYr7v90oLFKWnffFM
ENV_EOF

# 7. Create a systemd service that loads environment variables
SERVICE_PATH="/etc/systemd/system/rsi-bot.service"
cat << SERVICE_EOF > "$SERVICE_PATH"
[Unit]
Description=RSI Trading Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$BOT_DIR
EnvironmentFile=$BOT_DIR/.env
ExecStart=/bin/bash -c 'cd $BOT_DIR && source venv/bin/activate && python main.py'
Restart=always

[Install]
WantedBy=multi-user.target
SERVICE_EOF

# 8. Reload systemd, enable & start
systemctl daemon-reload
systemctl enable rsi-bot
systemctl start rsi-bot

echo "SUCCESS: RSI bot deployed and running under systemd."
END_BOOTSTRAP

###################################
# 5) SSH into droplet, run bootstrap
###################################
echo "Running bootstrap script on droplet $DROPLET_IP ..."
ssh -o StrictHostKeyChecking=no "$SSH_USER@$DROPLET_IP" "bash -s" << EOF
$BOOTSTRAP_SCRIPT
EOF

if [ $? -ne 0 ]; then
  echo "ERROR: Bootstrap script failed."
  exit 1
fi

###################################
# Done!
###################################
echo "All done! Your RSI bot droplet is at $DROPLET_IP."
echo "You can SSH in with: ssh $SSH_USER@$DROPLET_IP"
echo "Check the bot logs via: journalctl -u rsi-bot -f"