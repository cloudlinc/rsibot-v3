# RSI MACD Trading Bot

An automated trading bot that uses RSI (Relative Strength Index) and MACD (Moving Average Convergence Divergence) indicators to make trading decisions. The bot integrates with either Interactive Brokers or Charles Schwab for trade execution and uses Supabase for configuration and trade history storage.

## Features

- RSI-based entry and exit signals
- MACD trend confirmation
- Manual or automatic trading modes
- Real-time trade execution via Interactive Brokers or Charles Schwab
- Configuration and trade history storage in Supabase
- Comprehensive logging
- Dockerized deployment

## Prerequisites

- Python 3.10 or higher
- Docker (for containerized deployment)
- Either:
  - Interactive Brokers TWS or IB Gateway
  - OR Charles Schwab trading account
- Supabase account and project

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rsibot-v1.git
   cd rsibot-v1
   ```

2. Create and configure environment variables:
   
   For Interactive Brokers:
   ```bash
   cp .env.ibkr.example .env
   # Edit .env with your Supabase and IB credentials
   ```
   
   For Charles Schwab:
   ```bash
   cp .env.schwab.example .env
   # Edit .env with your Supabase and Schwab credentials
   ```

3. Create the required Supabase tables:

   bot_config table:
   ```sql
   create table bot_config (
     id uuid default uuid_generate_v4() primary key,
     ticker text not null,
     rsi_buy_threshold float not null default 30,
     rsi_sell_threshold float not null default 70,
     macd_enabled boolean not null default true,
     manual_mode boolean not null default false,
     shares_per_trade integer not null default 10,
     created_at timestamp with time zone default timezone('utc'::text, now()) not null,
     updated_at timestamp with time zone default timezone('utc'::text, now()) not null
   );
   ```

   trade_signals table:
   ```sql
   create table trade_signals (
     id uuid default uuid_generate_v4() primary key,
     ticker text not null,
     action text not null,
     rsi float not null,
     macd float not null,
     status text not null default 'PENDING',
     created_at timestamp with time zone default timezone('utc'::text, now()) not null,
     updated_at timestamp with time zone default timezone('utc'::text, now()) not null
   );
   ```

   trade_history table:
   ```sql
   create table trade_history (
     id uuid default uuid_generate_v4() primary key,
     ticker text not null,
     action text not null,
     rsi float not null,
     macd float not null,
     executed_at timestamp with time zone default timezone('utc'::text, now()) not null
   );
   ```

## Local Development

1. Install dependencies:
   
   For Interactive Brokers:
   ```bash
   pip install -r requirements.ibkr.txt
   ```
   
   For Charles Schwab:
   ```bash
   pip install -r requirements.schwab.txt
   ```

2. Start your trading platform:
   - For IB: Start Interactive Brokers TWS or IB Gateway
   - For Schwab: Ensure you have Chrome/Chromium installed

3. Run the bot:
   
   For Interactive Brokers:
   ```bash
   python ibkr_bot.py
   ```
   
   For Charles Schwab:
   ```bash
   python schwab_bot.py
   ```

## Docker Deployment

### Interactive Brokers Version

1. Build the IBKR version Docker image:
   ```bash
   docker build -f Dockerfile.ibkr -t rsi-macd-bot-ibkr .
   ```

2. Run the IBKR container:
   ```bash
   docker run -d \
     --name rsi-macd-bot-ibkr \
     --env-file .env \
     rsi-macd-bot-ibkr
   ```

### Charles Schwab Version

1. Build the Schwab version Docker image:
   ```bash
   docker build -f Dockerfile.schwab -t rsi-macd-bot-schwab .
   ```

2. Run the Schwab container:
   ```bash
   docker run -d \
     --name rsi-macd-bot-schwab \
     --env-file .env \
     rsi-macd-bot-schwab
   ```

Note: The Schwab version uses browser automation to interact with Schwab's trading platform. Make sure your Schwab account:
- Has 2FA disabled or uses a compatible authentication method
- Has the necessary trading permissions
- Complies with Schwab's terms of service regarding automated trading

## Configuration

Configure the bot through the `bot_config` table in Supabase:

- `ticker`: Stock symbol to trade (e.g., "AAPL")
- `rsi_buy_threshold`: RSI level for buy signals (default: 30)
- `rsi_sell_threshold`: RSI level for sell signals (default: 70)
- `macd_enabled`: Whether to use MACD confirmation (default: true)
- `manual_mode`: Whether to require manual trade approval (default: false)
- `shares_per_trade`: Number of shares per trade (default: 10)

## Monitoring

The bot logs all activities to stdout/stderr, which can be viewed using:

For Interactive Brokers:
```bash
docker logs -f rsi-macd-bot-ibkr
```

For Charles Schwab:
```bash
docker logs -f rsi-macd-bot-schwab
```

## License

MIT

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 

## Easy deploy

## Deploy with monitoring (default)
./deploy.sh ibkr

## Deploy without setting up monitoring tables
./deploy.sh ibkr false 



## Deploy on a DigitalOcean droplet

ssh root@your_droplet_ip

# Create a non-root user
adduser trading
usermod -aG sudo trading

# Switch to trading user
su - trading

# Download our server setup script
curl -O https://raw.githubusercontent.com/your_username/rsibot-v1/main/server-setup.sh
chmod +x server-setup.sh

# Run the setup
./server-setup.sh

# Edit the config with your GitHub details
nano ~/.deploy-config

# Deploy the bot
source ~/.deploy-config
cd ~/deployments
./deploy.sh ibkr  # or schwab




