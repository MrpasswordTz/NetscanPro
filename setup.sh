#!/data/data/com.termux/files/usr/bin/bash

echo "setup for NetScanPro"


pkg update && pkg upgrade
pkg install git wget python python2 python3 nmap

echo "Installation complete!"
