#!/bin/bash

# Configuration
DO_TOKEN=${DO_TOKEN:-"dop_v1_e3148d56db62bb0a574b1271540498367804099a710254c6cf607f843aa284c0"}
GITHUB_PAT=${GITHUB_PAT:-"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"}
GITHUB_USERNAME=${GITHUB_USERNAME:-"cloudlinc"}
BROKER=${1:-"ibkr"}
DROPLET_NAME="trading-bot-${BROKER}"
SSH_KEY_NAME=${SSH_KEY_NAME:-"my-trading-key"}
IBKR_USERNAME=${IBKR_USERNAME:-"scap3883"}
IBKR_PASSWORD=${IBKR_PASSWORD:-"Maxamillion@383"}

# Check required tools
command -v doctl >/dev/null 2>&1 || { echo "Please install doctl first: https://docs.digitalocean.com/reference/doctl/how-to/install/"; exit 1; }

# Ensure we have DO token
if [ -z "$DO_TOKEN" ]; then
    echo "Error: Please set DO_TOKEN environment variable"
    echo "Example: export DO_TOKEN=\"your_digitalocean_token\""
    exit 1
fi

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
  - docker.io
  - git
EOL

# Create the droplet
echo "Creating DigitalOcean droplet..."
doctl compute droplet create "$DROPLET_NAME" \
    --region nyc1 \
    --image ubuntu-22-04-x64 \
    --size s-1vcpu-1gb \
    --ssh-keys "${SSH_KEY_ID}" \
    --user-data-file cloud-init.yaml \
    --wait

# Get the droplet IP (wait a bit for the droplet to be ready)
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

# Install Docker if not installed
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    sudo apt-get update
    sudo apt-get install -y docker.io git
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker trading
fi

# Create .env file
cat > ~/.env << 'ENVEOF'
GITHUB_USERNAME=cloudlinc
GITHUB_PAT=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
IBKR_USERNAME=scap3883
IBKR_PASSWORD=Maxamillion@383
ENVEOF
chmod 600 ~/.env

# Clone repository if not exists
if [ ! -d ~/bot ]; then
    git clone https://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@github.com/cloudlinc/rsibot-v1.git ~/bot
fi

# Build and run container
cd ~/bot
docker build -t rsi-bot -f Dockerfile.ibkr .
docker run -d --name rsi-bot --env-file ~/.env rsi-bot
EOL

# Make script executable and run it
ssh trading@${DROPLET_IP} "chmod +x setup.sh && ./setup.sh"

echo "
Deployment completed!

Your trading bot is being deployed to: ${DROPLET_IP}
Broker type: ${BROKER}

To check if the bot is running:
ssh trading@${DROPLET_IP} 'docker ps'

To view bot logs:
ssh trading@${DROPLET_IP} 'docker logs -f rsi-bot'

To check system logs:
ssh trading@${DROPLET_IP} 'sudo journalctl -fu docker'
" 