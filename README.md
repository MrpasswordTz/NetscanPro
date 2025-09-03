# NetscanPro V2.0

<p align="center">
  <img src="https://raw.githubusercontent.com/MrpasswordTz/NetscanPro/refs/heads/main/img/netscaN.png" alt="NetscanPro Logo" width="200">
</p>

<p align="center">
  <a href="https://github.com/MrpasswordTz/NetscanPro/blob/main/LICENSE"><img src="https://img.shields.io/github/license/MrpasswordTz/NetscanPro.svg" alt="License"></a>
  <a href="https://github.com/MrpasswordTz/NetscanPro/releases"><img src="https://img.shields.io/github/v/release/MrpasswordTz/NetscanPro" alt="Release"></a>
  <a href="https://github.com/MrpasswordTz/NetscanPro/stargazers"><img src="https://img.shields.io/github/stars/MrpasswordTz/NetscanPro" alt="Stars"></a>
  <a href="https://github.com/MrpasswordTz/NetscanPro/network/members"><img src="https://img.shields.io/github/forks/MrpasswordTz/NetscanPro" alt="Forks"></a>
  <a href="https://github.com/MrpasswordTz/NetscanPro/issues"><img src="https://img.shields.io/github/issues/MrpasswordTz/NetscanPro" alt="Issues"></a>
</p>

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Description

NetscanPro is a comprehensive, user-friendly network scanning tool built on top of Nmap. It empowers cybersecurity professionals, network administrators, and enthusiasts to perform advanced network reconnaissance, vulnerability detection, and security audits. With an intuitive menu-driven interface, NetscanPro simplifies complex Nmap operations, making network scanning accessible to users of all skill levels.

The tool provides detailed insights into network topology, identifies active devices, detects open ports, services, and potential vulnerabilities. It supports various scanning techniques, output formats, and includes features like batch processing, report generation, and configuration management.

## Features

### Core Scanning Capabilities
- **Basic Scanning**: Single target, multiple targets, IP ranges, subnets, random hosts, aggressive scans, IPv6 support
- **Discovery Options**: Multiple ping types (ICMP, TCP SYN/ACK, UDP, SCTP INIT, etc.)
- **Advanced Scanning**: SYN, Connect, UDP, NULL, FIN, Xmas, ACK scans, custom flags, IP protocol scans
- **Port Scanning**: Fast scans, specific ports, port ranges, service-based, all ports, top ports
- **Version Detection**: Service and OS fingerprinting
- **Firewall Evasion**: Fragmentation, decoys, spoofing techniques
- **NSE Scripts**: Run default, vulnerability, and discovery scripts

### Additional Features
- **Traceroute**: Network path tracing with various options
- **Fast Scan**: Quick DNS lookups and WHOIS queries
- **Output Options**: Normal, XML, Grepable, Script Kiddie, and all formats
- **Timing Options**: Paranoid to Insane timing templates
- **Miscellaneous**: Verbose output, debugging, resume scans, host exclusion
- **Configuration Management**: Save and load custom settings
- **Batch Processing**: Execute multiple scan commands simultaneously
- **Report Generation**: Professional HTML reports with vulnerability analysis
- **Scan History**: Save and manage previous scan results
- **Logging**: Comprehensive logging with configurable levels

### User Experience
- **Intuitive Menu Interface**: Easy navigation without command-line knowledge
- **Cross-Platform**: Supports Linux and Termux (Android)
- **Color-Coded Output**: Enhanced readability with colorama
- **Progress Indicators**: Real-time feedback during scans
- **Error Handling**: Robust error management and user guidance
- **Open Source**: Fully transparent and community-driven

## Installation

### Prerequisites
- Python 3.6+
- Nmap
- Root/administrator privileges (recommended for full functionality)

### Linux Installation
```bash
git clone https://github.com/MrpasswordTz/NetscanPro.git
cd NetscanPro
chmod +x setup.sh
sudo ./setup.sh
```

### Termux (Android) Installation
```bash
pkg update
pkg install git
git clone https://github.com/MrpasswordTz/NetscanPro.git
cd NetscanPro
chmod +x setup.sh
./setup.sh
```

### Manual Installation
If the setup script doesn't work:
```bash
# Install system dependencies
sudo apt update
sudo apt install -y nmap dnsutils whois

# Install Python dependencies
pip3 install colorama
```

## Usage

1. Run the tool:
   ```bash
   python3 NetscanPro.py
   ```

2. Navigate through the menu options (1-16) to select your desired scan type

3. Follow the prompts to enter target information and scan parameters

4. View results in the terminal or generate professional reports

### Example Usage
- Select option 1 for Basic Scanning
- Choose a scan type (e.g., single target)
- Enter the target IP or hostname
- The tool will execute the Nmap scan and display results
- Optionally save the scan for reporting

## Screenshots

### Main Menu
![Main Menu](https://raw.githubusercontent.com/MrpasswordTz/NetscanPro/refs/heads/main/img/netscaN.png)

### Scan Results
![Scan Results](https://via.placeholder.com/600x400?text=Scan+Results+Example)

### Generated Report
![Generated Report](https://raw.githubusercontent.com/MrpasswordTz/NetscanPro/refs/heads/main/img/res.png)

*Screenshots will be added soon. For now, the tool provides detailed terminal output.*

## Contributing

We welcome contributions from the community! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a Pull Request

### Development Setup
```bash
git clone https://github.com/MrpasswordTz/NetscanPro.git
cd NetscanPro
pip3 install -r requirements.txt  # If requirements.txt is added
```

### Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Test your changes thoroughly
- Update documentation as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

**⚠️ WARNING**: This tool is intended for educational and authorized security testing purposes only. Unauthorized use of NetscanPro against networks or systems you do not own or have explicit permission to test may violate laws and regulations. The developers and contributors are not responsible for any misuse or damage caused by this tool.

Always ensure you have proper authorization before performing any network scanning activities. Use responsibly and ethically.

---

**Developed by**: [MrpasswordTz](https://github.com/MrpasswordTz)  
**Contributors**: [iamunix](https://github.com/iamunix)

*This tool is under active development. 🚧 🏗️*
