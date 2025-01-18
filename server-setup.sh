#!/bin/bash

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
    echo "Please run without sudo"
    exit 1
fi

# Create deployment directory
echo "Creating deployment directory..."
mkdir -p ~/deployments
cd ~/deployments

# Install Docker if not present
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    rm get-docker.sh
    echo "Docker installed. You may need to log out and back in for group changes to take effect."
fi

# Create configuration file
echo "Creating deployment configuration..."
cat > ~/.deploy-config << EOL
# GitHub Configuration
export GITHUB_USERNAME="your_github_username"
export GITHUB_PAT="your_github_pat"
EOL

chmod 600 ~/.deploy-config  # Secure the file
echo "Created ~/.deploy-config - Please edit it with your GitHub credentials"

# Download deployment script
echo "Downloading deployment script..."
curl -o deploy.sh https://raw.githubusercontent.com/\$GITHUB_USERNAME/rsibot-v1/main/deploy.sh
chmod +x deploy.sh

echo "
Setup complete! To deploy:

1. Edit ~/.deploy-config with your GitHub credentials
2. Run: source ~/.deploy-config
3. Deploy with either:
   ./deploy.sh ibkr
   or
   ./deploy.sh schwab

Note: If you just installed Docker, you may need to log out and back in first." 