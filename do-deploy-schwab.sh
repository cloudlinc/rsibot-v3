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
  - git

runcmd:
  - mkdir -p /home/trading/bot/logs
  - chown -R trading:trading /home/trading/bot
  - sudo -u trading python3 -m venv /home/trading/bot/venv
  - sudo -u trading /home/trading/bot/venv/bin/pip install -r /home/trading/bot/requirements.schwab.txt
  - systemctl daemon-reload
  - systemctl enable schwab-bot
  - systemctl start schwab-bot
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

# Copy files
echo "Copying files..."
scp -o StrictHostKeyChecking=no -r schwab_bot.py requirements.schwab.txt .env.schwab.example trading@"$DROPLET_IP":/home/trading/bot/
ssh -o StrictHostKeyChecking=no trading@"$DROPLET_IP" "cd /home/trading/bot && cp .env.schwab.example .env"

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
ExecStart=/home/trading/bot/venv/bin/python schwab_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF'"

echo "Deployment complete!"
echo "Your bot has been deployed to: $DROPLET_IP"
echo ""
echo "Next steps:"
echo "1. SSH into your server: ssh trading@$DROPLET_IP"
echo "2. Edit the environment file: nano /home/trading/bot/.env"
echo "3. Start the bot: sudo systemctl start schwab-bot"
echo ""
echo "To monitor the bot:"
echo "- Check status: sudo systemctl status schwab-bot"
echo "- View logs: sudo journalctl -fu schwab-bot"
echo "- Check detailed logs: tail -f /home/trading/bot/logs/trading.log" 