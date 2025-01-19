#!/bin/bash
set -e

# DigitalOcean configuration
DO_TOKEN=${DO_TOKEN:-"dop_v1_e3148d56db62bb0a574b1271540498367804099a710254c6cf607f843aa284c0"}
SSH_KEY_NAME=${SSH_KEY_NAME:-"my-trading-key"}
DROPLET_NAME="schwab-trading-bot"
DROPLET_REGION="nyc1"
DROPLET_SIZE="s-1vcpu-1gb"
IMAGE="ubuntu-22-04-x64"

# Check for required tools
if ! command -v doctl &> /dev/null; then
    echo "Error: doctl is not installed. Please install it first."
    exit 1
fi

# Validate environment variables
if [ -z "$DO_TOKEN" ]; then
    echo "Error: DO_TOKEN environment variable is not set"
    exit 1
fi

if [ -z "$SSH_KEY_NAME" ]; then
    echo "Error: SSH_KEY_NAME environment variable is not set"
    exit 1
fi

# Configure doctl
doctl auth init -t "$DO_TOKEN"

# Get SSH key ID and public key
SSH_KEY_ID=$(doctl compute ssh-key list --format ID,Name --no-header | grep "$SSH_KEY_NAME" | awk '{print $1}')
if [ -z "$SSH_KEY_ID" ]; then
    echo "Error: SSH key '$SSH_KEY_NAME' not found"
    exit 1
fi

SSH_PUBLIC_KEY=$(doctl compute ssh-key get "$SSH_KEY_ID" --format PublicKey --no-header)
if [ -z "$SSH_PUBLIC_KEY" ]; then
    echo "Error: Could not retrieve public key for '$SSH_KEY_NAME'"
    exit 1
fi

# Create cloud-init user data with the actual SSH key
cat > cloud-init.yaml << EOF
#cloud-config
users:
  - name: trading
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    shell: /bin/bash
    ssh_authorized_keys:
      - $SSH_PUBLIC_KEY

packages:
  - python3-pip
  - python3-venv
  - python3.10-venv
  - python3-dev
  - build-essential
  - git

runcmd:
  - mkdir -p /home/trading/bot/logs
  - chown -R trading:trading /home/trading/bot
  - apt-get update
  - apt-get install -y python3.10-venv
EOF

# Create droplet
echo "Creating droplet..."
DROPLET_ID=$(doctl compute droplet create \
    --image "$IMAGE" \
    --size "$DROPLET_SIZE" \
    --region "$DROPLET_REGION" \
    --ssh-keys "$SSH_KEY_ID" \
    --user-data-file cloud-init.yaml \
    --wait \
    "$DROPLET_NAME" \
    --format ID --no-header)

# Get droplet IP
DROPLET_IP=$(doctl compute droplet get "$DROPLET_ID" --format PublicIPv4 --no-header)

echo "Waiting for SSH to be available..."
MAX_ATTEMPTS=30
ATTEMPT=0

while [ $ATTEMPT -lt $MAX_ATTEMPTS ]; do
    if ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 trading@"$DROPLET_IP" echo ready 2>/dev/null; then
        break
    fi
    echo "Waiting for SSH... Attempt $((ATTEMPT + 1))/$MAX_ATTEMPTS"
    sleep 10
    ATTEMPT=$((ATTEMPT + 1))
done

if [ $ATTEMPT -eq $MAX_ATTEMPTS ]; then
    echo "Error: Could not establish SSH connection after $MAX_ATTEMPTS attempts"
    exit 1
fi

# Wait for cloud-init to complete
echo "Waiting for cloud-init to complete..."
ssh -o StrictHostKeyChecking=no trading@"$DROPLET_IP" "cloud-init status --wait"

# Copy files
echo "Copying files..."
scp -o StrictHostKeyChecking=no -r schwab_bot.py requirements.schwab.txt .env trading@"$DROPLET_IP":/home/trading/bot/

# Set up Python environment and install dependencies
echo "Setting up Python environment..."
ssh -o StrictHostKeyChecking=no trading@"$DROPLET_IP" "cd /home/trading/bot && \
    python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install wheel && \
    pip install -r requirements.schwab.txt"

# Create systemd service
echo "Creating systemd service..."
ssh -o StrictHostKeyChecking=no trading@"$DROPLET_IP" "sudo bash -c 'cat > /etc/systemd/system/schwab-bot.service << EOF
[Unit]
Description=Schwab Trading Bot
After=network.target

[Service]
Type=simple
User=trading
WorkingDirectory=/home/trading/bot
Environment=PATH=/home/trading/bot/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ExecStart=/home/trading/bot/venv/bin/python3 schwab_bot.py
Restart=always
RestartSec=10
StandardOutput=append:/home/trading/bot/logs/trading.log
StandardError=append:/home/trading/bot/logs/trading.log

[Install]
WantedBy=multi-user.target
EOF'"

# Create log directory and set permissions
ssh -o StrictHostKeyChecking=no trading@"$DROPLET_IP" "sudo mkdir -p /home/trading/bot/logs && sudo chown -R trading:trading /home/trading/bot/logs"

# Enable and start the service
echo "Starting the bot service..."
ssh -o StrictHostKeyChecking=no trading@"$DROPLET_IP" "sudo systemctl daemon-reload && \
    sudo systemctl enable schwab-bot && \
    sudo systemctl start schwab-bot"

# Check service status
echo "Checking service status..."
ssh -o StrictHostKeyChecking=no trading@"$DROPLET_IP" "sudo systemctl status schwab-bot --no-pager"

echo "Deployment complete!"
echo "Your bot has been deployed to: $DROPLET_IP"
echo ""
echo "Next steps:"
echo "1. SSH into your server: ssh trading@$DROPLET_IP"
echo "2. Check the bot status: sudo systemctl status schwab-bot"
echo ""
echo "To monitor the bot:"
echo "- Check status: sudo systemctl status schwab-bot"
echo "- View service logs: sudo journalctl -fu schwab-bot"
echo "- View application logs: tail -f /home/trading/bot/logs/trading.log"
echo ""
echo "To manage the bot:"
echo "- Stop bot: sudo systemctl stop schwab-bot"
echo "- Start bot: sudo systemctl start schwab-bot"
echo "- Restart bot: sudo systemctl restart schwab-bot" 