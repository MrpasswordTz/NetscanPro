# CVE Database for vulnerabilities
CVE_DATABASE = {
    "22/tcp": {
        "service": "SSH",
        "vulnerabilities": [
            {
                "cve": "CVE-2018-15473",
                "description": "OpenSSH user enumeration vulnerability",
                "impact": "Information disclosure",
                "fix": "Upgrade OpenSSH to version 7.7 or later"
            },
            {
                "cve": "CVE-2020-15778",
                "description": "OpenSSH command injection vulnerability",
                "impact": "Remote code execution",
                "fix": "Upgrade OpenSSH to version 8.3 or later"
            },
            {
                "cve": "CVE-2023-38408",
                "description": "OpenSSH privilege escalation vulnerability",
                "impact": "Privilege escalation",
                "fix": "Upgrade OpenSSH to version 9.3 or later"
            }
        ]
    },
    "80/tcp": {
        "service": "HTTP",
        "vulnerabilities": [
            {
                "cve": "CVE-2019-11043",
                "description": "PHP-FPM vulnerability allowing remote code execution",
                "impact": "Remote code execution",
                "fix": "Update PHP-FPM and configure properly"
            },
            {
                "cve": "CVE-2021-44228",
                "description": "Apache Log4j remote code execution vulnerability",
                "impact": "Remote code execution",
                "fix": "Update Log4j to version 2.17.0 or later"
            },
            {
                "cve": "CVE-2021-41773",
                "description": "Apache HTTP Server path traversal vulnerability",
                "impact": "Path traversal, information disclosure",
                "fix": "Update Apache to version 2.4.51 or later"
            },
            {
                "cve": "CVE-2017-5638",
                "description": "Apache Struts remote code execution vulnerability",
                "impact": "Remote code execution",
                "fix": "Update Apache Struts to version 2.3.32 or 2.5.10.1"
            }
        ]
    },
    "443/tcp": {
        "service": "HTTPS",
        "vulnerabilities": [
            {
                "cve": "CVE-2020-0601",
                "description": "Windows CryptoAPI spoofing vulnerability",
                "impact": "Man-in-the-middle attacks",
                "fix": "Apply Windows security updates"
            },
            {
                "cve": "CVE-2014-0160",
                "description": "Heartbleed OpenSSL information disclosure",
                "impact": "Information disclosure, private key exposure",
                "fix": "Update OpenSSL to version 1.0.1g or later"
            },
            {
                "cve": "CVE-2021-3449",
                "description": "OpenSSL denial of service vulnerability",
                "impact": "Denial of service",
                "fix": "Update OpenSSL to version 1.1.1k or later"
            }
        ]
    },
    "21/tcp": {
        "service": "FTP",
        "vulnerabilities": [
            {
                "cve": "CVE-2011-2523",
                "description": "VSFTPD backdoor vulnerability",
                "impact": "Remote code execution",
                "fix": "Update VSFTPD to version 2.3.5 or later"
            },
            {
                "cve": "CVE-2020-9490",
                "description": "ProFTPD mod_copy remote code execution",
                "impact": "Remote code execution",
                "fix": "Update ProFTPD to version 1.3.6b or later"
            }
        ]
    },
    "23/tcp": {
        "service": "Telnet",
        "vulnerabilities": [
            {
                "cve": "CVE-2020-10188",
                "description": "Multiple Telnet vulnerabilities",
                "impact": "Denial of service, information disclosure",
                "fix": "Update Telnet service or disable in favor of SSH"
            }
        ]
    },
    "25/tcp": {
        "service": "SMTP",
        "vulnerabilities": [
            {
                "cve": "CVE-2021-34429",
                "description": "Exim SMTP server remote code execution",
                "impact": "Remote code execution",
                "fix": "Update Exim to version 4.94.2 or later"
            },
            {
                "cve": "CVE-2019-15846",
                "description": "Exim off-by-one remote code execution",
                "impact": "Remote code execution",
                "fix": "Update Exim to version 4.92.3 or later"
            }
        ]
    },
    "53/tcp": {
        "service": "DNS",
        "vulnerabilities": [
            {
                "cve": "CVE-2020-1350",
                "description": "Windows DNS Server wormable vulnerability",
                "impact": "Remote code execution",
                "fix": "Apply Windows security updates"
            },
            {
                "cve": "CVE-2021-25216",
                "description": "BIND denial of service vulnerability",
                "impact": "Denial of service",
                "fix": "Update BIND to version 9.16.13 or later"
            }
        ]
    },
    "53/udp": {
        "service": "DNS",
        "vulnerabilities": [
            {
                "cve": "CVE-2020-1350",
                "description": "Windows DNS Server wormable vulnerability",
                "impact": "Remote code execution",
                "fix": "Apply Windows security updates"
            },
            {
                "cve": "CVE-2021-25216",
                "description": "BIND denial of service vulnerability",
                "impact": "Denial of service",
                "fix": "Update BIND to version 9.16.13 or later"
            }
        ]
    },
    "110/tcp": {
        "service": "POP3",
        "vulnerabilities": [
            {
                "cve": "CVE-2020-12667",
                "description": "Dovecot POP3/IMAP vulnerability",
                "impact": "Information disclosure",
                "fix": "Update Dovecot to version 2.3.11.3 or later"
            }
        ]
    },
    "135/tcp": {
        "service": "MSRPC",
        "vulnerabilities": [
            {
                "cve": "CVE-2021-34527",
                "description": "Windows Print Spooler remote code execution",
                "impact": "Remote code execution",
                "fix": "Apply Windows security updates"
            },
            {
                "cve": "CVE-2020-1472",
                "description": "Netlogon elevation of privilege vulnerability",
                "impact": "Privilege escalation",
                "fix": "Apply Windows security updates"
            }
        ]
    },
    "139/tcp": {
        "service": "NetBIOS",
        "vulnerabilities": [
            {
                "cve": "CVE-2017-0143",
                "description": "EternalBlue SMB remote code execution",
                "impact": "Remote code execution",
                "fix": "Apply MS17-010 security update"
            },
            {
                "cve": "CVE-2020-0796",
                "description": "SMBv3 compression buffer overflow",
                "impact": "Remote code execution",
                "fix": "Apply Windows security updates"
            }
        ]
    },
    "143/tcp": {
        "service": "IMAP",
        "vulnerabilities": [
            {
                "cve": "CVE-2020-12667",
                "description": "Dovecot POP3/IMAP vulnerability",
                "impact": "Information disclosure",
                "fix": "Update Dovecot to version 2.3.11.3 or later"
            }
        ]
    },
    "445/tcp": {
        "service": "SMB",
        "vulnerabilities": [
            {
                "cve": "CVE-2017-0143",
                "description": "EternalBlue SMB remote code execution",
                "impact": "Remote code execution",
                "fix": "Apply MS17-010 security update"
            },
            {
                "cve": "CVE-2020-0796",
                "description": "SMBv3 compression buffer overflow",
                "impact": "Remote code execution",
                "fix": "Apply Windows security updates"
            },
            {
                "cve": "CVE-2021-34527",
                "description": "Windows Print Spooler remote code execution",
                "impact": "Remote code execution",
                "fix": "Apply Windows security updates"
            }
        ]
    },
    "993/tcp": {
        "service": "IMAPS",
        "vulnerabilities": [
            {
                "cve": "CVE-2020-12667",
                "description": "Dovecot POP3/IMAP vulnerability",
                "impact": "Information disclosure",
                "fix": "Update Dovecot to version 2.3.11.3 or later"
            }
        ]
    },
    "995/tcp": {
        "service": "POP3S",
        "vulnerabilities": [
            {
                "cve": "CVE-2020-12667",
                "description": "Dovecot POP3/IMAP vulnerability",
                "impact": "Information disclosure",
                "fix": "Update Dovecot to version 2.3.11.3 or later"
            }
        ]
    },
    "1433/tcp": {
        "service": "MSSQL",
        "vulnerabilities": [
            {
                "cve": "CVE-2021-1636",
                "description": "SQL Server remote code execution vulnerability",
                "impact": "Remote code execution",
                "fix": "Apply SQL Server security updates"
            }
        ]
    },
    "1434/tcp": {
        "service": "MSSQL Browser",
        "vulnerabilities": [
            {
                "cve": "CVE-2021-1636",
                "description": "SQL Server remote code execution vulnerability",
                "impact": "Remote code execution",
                "fix": "Apply SQL Server security updates"
            }
        ]
    },
    "1434/udp": {
        "service": "MSSQL Browser",
        "vulnerabilities": [
            {
                "cve": "CVE-2021-1636",
                "description": "SQL Server remote code execution vulnerability",
                "impact": "Remote code execution",
                "fix": "Apply SQL Server security updates"
            }
        ]
    },
    "3306/tcp": {
        "service": "MySQL",
        "vulnerabilities": [
            {
                "cve": "CVE-2021-27928",
                "description": "MySQL Server wormable vulnerability",
                "impact": "Remote code execution",
                "fix": "Update MySQL to version 8.0.23 or later"
            },
            {
                "cve": "CVE-2020-14812",
                "description": "MySQL Server privilege escalation",
                "impact": "Privilege escalation",
                "fix": "Update MySQL to version 8.0.22 or later"
            }
        ]
    },
    "3389/tcp": {
        "service": "RDP",
        "vulnerabilities": [
            {
                "cve": "CVE-2019-0708",
                "description": "BlueKeep RDP remote code execution",
                "impact": "Remote code execution",
                "fix": "Apply Windows security updates"
            },
            {
                "cve": "CVE-2020-0609",
                "description": "RDP gateway denial of service",
                "impact": "Denial of service",
                "fix": "Apply Windows security updates"
            }
        ]
    },
    "5432/tcp": {
        "service": "PostgreSQL",
        "vulnerabilities": [
            {
                "cve": "CVE-2021-23214",
                "description": "PostgreSQL privilege escalation",
                "impact": "Privilege escalation",
                "fix": "Update PostgreSQL to version 13.3 or later"
            },
            {
                "cve": "CVE-2020-25695",
                "description": "PostgreSQL information disclosure",
                "impact": "Information disclosure",
                "fix": "Update PostgreSQL to version 13.1 or later"
            }
        ]
    },
    "5900/tcp": {
        "service": "VNC",
        "vulnerabilities": [
            {
                "cve": "CVE-2019-15690",
                "description": "RealVNC authentication bypass",
                "impact": "Authentication bypass",
                "fix": "Update RealVNC to version 6.7.1 or later"
            },
            {
                "cve": "CVE-2020-25708",
                "description": "TigerVNC denial of service",
                "impact": "Denial of service",
                "fix": "Update TigerVNC to version 1.11.0 or later"
            }
        ]
    },
    "6379/tcp": {
        "service": "Redis",
        "vulnerabilities": [
            {
                "cve": "CVE-2021-32761",
                "description": "Redis Lua sandbox escape",
                "impact": "Remote code execution",
                "fix": "Update Redis to version 6.2.6 or later"
            },
            {
                "cve": "CVE-2022-24735",
                "description": "Redis remote code execution",
                "impact": "Remote code execution",
                "fix": "Update Redis to version 7.0.0 or later"
            }
        ]
    },
    "9200/tcp": {
        "service": "Elasticsearch",
        "vulnerabilities": [
            {
                "cve": "CVE-2015-1427",
                "description": "Elasticsearch Groovy sandbox escape",
                "impact": "Remote code execution",
                "fix": "Update Elasticsearch to version 1.4.3 or later"
            },
            {
                "cve": "CVE-2019-7611",
                "description": "Elasticsearch privilege escalation",
                "impact": "Privilege escalation",
                "fix": "Update Elasticsearch to version 6.8.3 or later"
            }
        ]
    },
    "27017/tcp": {
        "service": "MongoDB",
        "vulnerabilities": [
            {
                "cve": "CVE-2021-20330",
                "description": "MongoDB denial of service",
                "impact": "Denial of service",
                "fix": "Update MongoDB to version 4.4.6 or later"
            },
            {
                "cve": "CVE-2019-2391",
                "description": "MongoDB privilege escalation",
                "impact": "Privilege escalation",
                "fix": "Update MongoDB to version 4.0.12 or later"
            }
        ]
    }
}