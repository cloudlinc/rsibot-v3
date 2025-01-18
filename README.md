# RSI Trading Bot Deployment

This repository contains an RSI (Relative Strength Index) trading bot that can be deployed to DigitalOcean using Interactive Brokers (IBKR) or Charles Schwab as the broker.

## Prerequisites

1. A DigitalOcean account with an API token
2. `doctl` CLI tool installed and configured
3. SSH key added to your DigitalOcean account
4. Git repository access token (for private repositories)
5. IBKR or Schwab account credentials

## Environment Setup

Before deploying, you need to set up the following environment variables:

```bash
# DigitalOcean configuration
export DO_TOKEN="your_digitalocean_api_token"
export SSH_KEY_NAME="your_ssh_key_name_in_digitalocean"

# GitHub configuration
export GITHUB_USERNAME="your_github_username"
export GITHUB_PAT="your_github_personal_access_token"

# Broker credentials (set in .env file on the server)
# For IBKR:
IBKR_USERNAME="your_ibkr_username"
IBKR_PASSWORD="your_ibkr_password"

# For Schwab:
SCHWAB_USERNAME="your_schwab_username"
SCHWAB_PASSWORD="your_schwab_password"
```

## Deployment

The deployment script supports both IBKR and Schwab brokers. To deploy:

1. For IBKR (default):
```bash
./do-deploy.sh
```

2. For Schwab:
```bash
./do-deploy.sh schwab
```

The script will:
1. Create a new DigitalOcean droplet
2. Install necessary dependencies
3. Set up a Python virtual environment
4. Clone the repository
5. Install Python requirements
6. Create and start a systemd service

## Monitoring

After deployment, you can:

1. Check bot status:
```bash
ssh trading@<droplet_ip> 'sudo systemctl status trading-bot'
```

2. View logs:
```bash
ssh trading@<droplet_ip> 'sudo journalctl -fu trading-bot'
```

3. Restart the bot:
```bash
ssh trading@<droplet_ip> 'sudo systemctl restart trading-bot'
```

## Project Structure

```
.
├── README.md
├── do-deploy.sh              # Deployment script
├── requirements.ibkr.txt     # IBKR-specific Python requirements
├── requirements.schwab.txt   # Schwab-specific Python requirements
├── .env.ibkr.example        # Example IBKR environment variables
├── .env.schwab.example      # Example Schwab environment variables
└── monitoring.py            # Monitoring utilities
```

## Security Notes

1. Never commit sensitive credentials to the repository
2. Use environment variables for sensitive information
3. Keep your API tokens and credentials secure
4. Regularly rotate your credentials and tokens

## Troubleshooting

1. If deployment fails, check:
   - DigitalOcean API token validity
   - SSH key configuration
   - GitHub access token permissions
   - Network connectivity

2. If the bot fails to start:
   - Check systemd service logs
   - Verify broker credentials
   - Ensure Python dependencies are installed correctly

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License - See LICENSE file for details




