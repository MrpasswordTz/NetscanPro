#!/data/data/com.termux/files/usr/bin/bash

echo "setup for NetScanPro"


apt update && apt upgrade
apt install git wget python python2 python3 nmap nslookup whois
pip install colorama

echo "Installation complete!"
