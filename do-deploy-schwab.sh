#!/bin/bash

# Configuration
DO_TOKEN=${DO_TOKEN:-"dop_v1_e3148d56db62bb0a574b1271540498367804099a710254c6cf607f843aa284c0"}  # DigitalOcean API token
SSH_KEY_NAME=${SSH_KEY_NAME:-"my-trading-key"}  # Your SSH key name in DigitalOcean
DROPLET_NAME="schwab-trading-bot"
DROPLET_REGION="nyc1"
DROPLET_SIZE="s-1vcpu-1gb"
IMAGE="ubuntu-22-04-x64"

# Check required tools
command -v doctl >/dev/null 2>&1 || { echo "Please install doctl first: https://docs.digitalocean.com/reference/doctl/how-to/install/"; exit 1; }

# Validate required environment variables
for var in DO_TOKEN SSH_KEY_NAME; do
    if [ -z "${!var}" ]; then
        echo "Error: Please set $var environment variable"
        exit 1
    fi
done

# Configure doctl with token
doctl auth init -t "$DO_TOKEN"

# Get SSH key ID from name
SSH_KEY_ID=$(doctl compute ssh-key list --format ID,Name --no-header | grep "${SSH_KEY_NAME}" | awk '{print $1}')

if [ -z "$SSH_KEY_ID" ]; then
    echo "Error: Could not find SSH key '${SSH_KEY_NAME}'"
    echo "Available SSH keys:"
    doctl compute ssh-key list
    echo "Please set SSH_KEY_NAME to one of the names above"
    exit 1
fi

# Get the SSH public key
SSH_PUBLIC_KEY=$(doctl compute ssh-key get ${SSH_KEY_ID} --format PublicKey --no-header)

# Create cloud-init user data
cat > cloud-init.yaml << EOL
#cloud-config
users:
  - name: trading
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    shell: /bin/bash
    ssh_authorized_keys:
      - ${SSH_PUBLIC_KEY}

packages:
  - python3-pip
  - python3-venv
  - git
EOL

# Create the droplet
echo "Creating DigitalOcean droplet..."
doctl compute droplet create "$DROPLET_NAME" \
    --region "$DROPLET_REGION" \
    --size "$DROPLET_SIZE" \
    --image "$IMAGE" \
    --ssh-keys "${SSH_KEY_ID}" \
    --user-data-file cloud-init.yaml \
    --wait

# Get the droplet IP
sleep 10
DROPLET_IP=$(doctl compute droplet list --format PublicIPv4,Name --no-header | grep "${DROPLET_NAME}" | awk '{print $1}')

echo "Waiting for system to be ready..."
MAX_ATTEMPTS=30
ATTEMPT=0

while ! ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 trading@${DROPLET_IP} 'exit' 2>/dev/null; do
    echo "Waiting for SSH to be available..."
    sleep 10
    ATTEMPT=$((ATTEMPT + 1))
    if [ $ATTEMPT -ge $MAX_ATTEMPTS ]; then
        echo "Timed out waiting for SSH access"
        exit 1
    fi
done

echo "Setting up the trading bot..."
# Create setup script on the server
ssh trading@${DROPLET_IP} "cat > setup.sh" << 'EOL'
#!/bin/bash
set -e

# Wait for apt locks to be released
while sudo fuser /var/lib/dpkg/lock >/dev/null 2>&1 || sudo fuser /var/lib/apt/lists/lock >/dev/null 2>&1 || sudo fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1; do
    echo "Waiting for apt locks to be released..."
    sleep 5
done

# Update system and install dependencies
echo "Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv git

# Create bot directory
mkdir -p ~/bot
cd ~/bot

# Copy bot files
cat > schwab_bot.py << 'BOTEOF'
$(cat schwab_bot.py)
BOTEOF

# Copy requirements file
cat > requirements.txt << 'REQEOF'
$(cat requirements.schwab.txt)
REQEOF

# Copy environment file template
cat > .env.example << 'ENVEOF'
$(cat .env.schwab.example)
ENVEOF

# Create logs directory
mkdir -p logs

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create systemd service file
sudo tee /etc/systemd/system/schwab-bot.service << 'SERVICEEOF'
[Unit]
Description=Schwab Trading Bot
After=network.target

[Service]
Type=simple
User=trading
WorkingDirectory=/home/trading/bot
Environment=PYTHONUNBUFFERED=1
EnvironmentFile=/home/trading/bot/.env
ExecStart=/home/trading/bot/venv/bin/python schwab_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
SERVICEEOF

# Create the actual .env file (to be filled in later)
cp .env.example .env

# Set proper permissions
chmod 600 .env

echo "Setup complete! Please edit /home/trading/bot/.env with your credentials before starting the bot."
EOL

# Make script executable and run it
ssh trading@${DROPLET_IP} "chmod +x setup.sh && ./setup.sh"

echo "
Deployment completed!

Your Schwab trading bot has been deployed to: ${DROPLET_IP}

IMPORTANT: Before starting the bot, you need to:
1. SSH into the server:
   ssh trading@${DROPLET_IP}

2. Edit the environment file with your credentials:
   nano /home/trading/bot/.env

3. Start the bot service:
   sudo systemctl start schwab-bot
   sudo systemctl enable schwab-bot

To monitor the bot:
- Check status: sudo systemctl status schwab-bot
- View logs: sudo journalctl -fu schwab-bot
- Check bot logs: tail -f /home/trading/bot/logs/trading.log

To stop the bot:
sudo systemctl stop schwab-bot
" 