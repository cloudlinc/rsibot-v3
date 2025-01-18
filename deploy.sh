#!/bin/bash

# Configuration
GITHUB_PAT=${GITHUB_PAT:-"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"}  # Must be set by user
GITHUB_USERNAME=${GITHUB_USERNAME:-"cloudlinc"}  # Must be set by user
REPO_NAME="rsibot-v1"
BROKER=${1:-"ibkr"}  # Default to IBKR if not specified
BACKUP_DIR=~/config-backups
MONITORING_SETUP=${2:-"true"}  # Whether to set up monitoring tables

# Ensure we have the PAT
if [ -z "$GITHUB_PAT" ]; then
    echo "Please set GITHUB_PAT environment variable"
    exit 1
fi

# Ensure we have the username
if [ -z "$GITHUB_USERNAME" ]; then
    echo "Please set GITHUB_USERNAME environment variable"
    exit 1
fi

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Backup existing configuration
backup_configs() {
    local timestamp=$(date +%Y%m%d_%H%M%S)
    if [ -f .env ]; then
        cp .env "$BACKUP_DIR/env_${BROKER}_${timestamp}"
        echo "Backed up .env to $BACKUP_DIR/env_${BROKER}_${timestamp}"
    fi
    if [ -f ~/.deploy-config ]; then
        cp ~/.deploy-config "$BACKUP_DIR/deploy-config_${timestamp}"
        echo "Backed up deploy-config to $BACKUP_DIR/deploy-config_${timestamp}"
    fi
}

# Clone/pull repository
if [ ! -d "$REPO_NAME" ]; then
    echo "Cloning repository..."
    git clone https://x-access-token:${GITHUB_PAT}@github.com/${GITHUB_USERNAME}/${REPO_NAME}.git
    cd $REPO_NAME
else
    echo "Updating repository..."
    cd $REPO_NAME
    git pull
fi

# Determine which broker to deploy
if [ "$BROKER" = "ibkr" ]; then
    DOCKERFILE="Dockerfile.ibkr"
    IMAGE_NAME="rsi-macd-bot-ibkr"
    ENV_FILE=".env.ibkr.example"
    export BOT_ID="ibkr-bot-${HOSTNAME}"
    export BROKER_TYPE="ibkr"
elif [ "$BROKER" = "schwab" ]; then
    DOCKERFILE="Dockerfile.schwab"
    IMAGE_NAME="rsi-macd-bot-schwab"
    ENV_FILE=".env.schwab.example"
    export BOT_ID="schwab-bot-${HOSTNAME}"
    export BROKER_TYPE="schwab"
else
    echo "Invalid broker specified. Use 'ibkr' or 'schwab'"
    exit 1
fi

# Backup existing configs
backup_configs

# Check if .env exists, if not create from example
if [ ! -f ".env" ]; then
    echo "Creating .env file from $ENV_FILE..."
    cp $ENV_FILE .env
    echo "Please edit .env with your credentials before continuing"
    exit 1
fi

# Set up monitoring tables if requested
if [ "$MONITORING_SETUP" = "true" ]; then
    echo "Setting up monitoring tables in Supabase..."
    # Extract Supabase URL and key from .env
    SUPABASE_URL=$(grep SUPABASE_URL .env | cut -d '=' -f2)
    SUPABASE_KEY=$(grep SUPABASE_ANON_KEY .env | cut -d '=' -f2)
    
    if [ -n "$SUPABASE_URL" ] && [ -n "$SUPABASE_KEY" ]; then
        # Use curl to execute the SQL (you'll need to adjust this based on your Supabase setup)
        curl -X POST "${SUPABASE_URL}/rest/v1/rpc/exec_sql" \
             -H "apikey: ${SUPABASE_KEY}" \
             -H "Authorization: Bearer ${SUPABASE_KEY}" \
             -H "Content-Type: application/json" \
             -d @monitoring_tables.sql
        
        echo "Monitoring tables created successfully"
    else
        echo "Warning: Could not set up monitoring tables. Missing Supabase credentials."
    fi
fi

# Add monitoring environment variables
echo "
# Monitoring Configuration
BOT_ID=${BOT_ID}
BROKER_TYPE=${BROKER_TYPE}" >> .env

# Build and run Docker container
echo "Building Docker image..."
docker build -f $DOCKERFILE -t $IMAGE_NAME .

echo "Stopping existing container if it exists..."
docker stop $IMAGE_NAME 2>/dev/null || true
docker rm $IMAGE_NAME 2>/dev/null || true

echo "Starting new container..."
docker run -d \
    --name $IMAGE_NAME \
    --restart unless-stopped \
    --env-file .env \
    -v $(pwd)/logs:/app/logs \
    $IMAGE_NAME

echo "Deployment complete! Monitor logs with: docker logs -f $IMAGE_NAME"
echo "
Monitoring Information:
- Bot ID: ${BOT_ID}
- Broker Type: ${BROKER_TYPE}
- Health Status: Check Supabase table 'bot_health'
- Error Logs: Check Supabase table 'bot_errors'
- Trade Attempts: Check Supabase table 'trade_attempts'

Backup Information:
- Configurations backed up to: ${BACKUP_DIR}
- Logs directory: $(pwd)/logs" 