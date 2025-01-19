#!/bin/bash

# Exit on error
set -e

echo "Starting Schwab Trading Bot deployment..."

# Create necessary directories
echo "Creating directories..."
mkdir -p /bot/logs

# Install system dependencies
echo "Installing system dependencies..."
apt-get update
apt-get install -y python3-pip python3-venv git

# Create and activate virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv /bot/venv
source /bot/venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.schwab.txt

# Copy bot files
echo "Copying bot files..."
cp schwab_bot.py /bot/
cp .env.schwab /bot/

# Create systemd service
echo "Creating systemd service..."
cat > /etc/systemd/system/schwab-bot.service << EOL
[Unit]
Description=Schwab Trading Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/bot
Environment=PYTHONUNBUFFERED=1
ExecStart=/bot/venv/bin/python3 /bot/schwab_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd and enable service
echo "Enabling and starting service..."
systemctl daemon-reload
systemctl enable schwab-bot
systemctl start schwab-bot

echo "Deployment complete! Bot service is now running."
echo "Check status with: systemctl status schwab-bot"
echo "View logs with: journalctl -u schwab-bot -f" 