

#!/bin/bash

# NetscanPro Setup Script
# This script installs the necessary dependencies for NetscanPro

set -e  # Exit on any error

echo "Setting up NetscanPro dependencies..."

# Check if running as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root or with sudo privileges."
    exit 1
fi

echo "Updating package list..."
apt update

echo "Installing required packages..."
apt install -y git wget python3 python3-pip nmap dnsutils whois

echo "Installing Python dependencies..."
pip3 install colorama

echo "Installation complete!"
echo "You can now run NetscanPro with: python3 NetscanPro.py"
