#!/data/data/com.termux/files/usr/bin/bash

echo "setup for NetScanPro"


apt update && apt upgrade
apt install git
apt install wget 
apt install python 
apt install python2 
apt install python3 
apt install nmap 
apt install nslookup 
apt install whois
apt install dnsutils
pip install colorama

echo "Installation complete!"
