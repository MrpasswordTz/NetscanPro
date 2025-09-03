import subprocess
import os
import signal
import logging
import json
import threading
import datetime
from colorama import Fore, Style, init
from .banner import *
from .cve import *



init()  # Initialize colorama

def setup_logger():
    """Set up the logger for the application."""
    logger = logging.getLogger('netscanpro')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()

print(Fore.BLUE + banner + Fore.RESET)

# Set up logging
logging.basicConfig(filename='netscanpro.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')





# New feature: Configuration file support
CONFIG_FILE = "netscanpro_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            try:
                config = json.load(f)
                logger.info("Configuration loaded from file.")
                return config
            except json.JSONDecodeError:
                print("Error: Configuration file is corrupted.")
                logger.error("Configuration file is corrupted.")
                return {}
    else:
        return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
        logger.info("Configuration saved to file.")

# Scan history and reports
SCAN_HISTORY_FILE = "scan_history.json"
REPORTS_DIR = "reports"

def ensure_reports_dir():
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)
        logger.info(f"Created reports directory: {REPORTS_DIR}")

def save_scan(scan_name, target, results):
    ensure_reports_dir()
    history = load_scan_history()
    scan_entry = {
        "name": scan_name,
        "target": target,
        "timestamp": datetime.datetime.now().isoformat(),
        "results": results
    }
    history.append(scan_entry)
    with open(SCAN_HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)
    logger.info(f"Scan saved: {scan_name}")

def load_scan_history():
    if os.path.exists(SCAN_HISTORY_FILE):
        with open(SCAN_HISTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def analyze_vulnerabilities(scan_results):
    """Analyze scan results for known vulnerabilities."""
    recommendations = []
    lines = scan_results.split('\n')
    for line in lines:
        if '/tcp' in line and 'open' in line:
            port = line.split('/')[0] + '/tcp'
            if port in CVE_DATABASE:
                vuln_info = CVE_DATABASE[port]
                recommendations.append({
                    "port": port,
                    "service": vuln_info["service"],
                    "vulnerabilities": vuln_info["vulnerabilities"]
                })
    return recommendations

# New feature: Progress indicator for scans
def progress_indicator():
    import time
    import sys
    spinner = ['|', '/', '-', '\\']
    idx = 0
    while True:
        sys.stdout.write(f"\rScanning... {spinner[idx % len(spinner)]}")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)

# New feature: Save scan results
def save_scan_results(scan_name, results):
    filename = f"{scan_name}_results.txt"
    with open(filename, "w") as f:
        f.write(results)
    print(f"Scan results saved to {filename}")
    logger.info(f"Scan results saved to {filename}")

# New feature: Batch processing mode
def batch_process(scan_commands):
    threads = []
    for cmd in scan_commands:
        t = threading.Thread(target=safe_run_command, args=(cmd,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# Global variable to store last scan result
last_scan_result = ""


def validate_target(target):
    """Basic validation for target input."""
    if not target or target.strip() == "":
        return False
    # Check for basic shell metacharacters
    dangerous_chars = [';', '&', '|', '`', '$', '(', ')']
    if any(char in target for char in dangerous_chars):
        return False
    return True

def safe_run_command(command):
    """Run command with better error handling and result capture."""
    global last_scan_result
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        full_output = result.stdout + result.stderr
        print(full_output)
        last_scan_result = full_output  # Store the result
        # Prompt to save scan
        print("\n" + "="*50)
        print("SCAN COMPLETED!")
        save_choice = input("Save this scan for reporting? (y/n): ").lower().strip()
        if save_choice == 'y':
            scan_name = input("Enter scan name: ").strip()
            if scan_name:
                target = command[-1] if len(command) > 1 else "unknown"
                save_scan(scan_name, target, full_output)
                print(f"Scan '{scan_name}' saved successfully!")
            else:
                print("Scan name cannot be empty.")
        else:
            print("Scan not saved.")
        print("="*50 + "\n")
        return True
    except subprocess.CalledProcessError as e:
        error_msg = f"Error running command: {e}\nError output: {e.stderr}"
        print(error_msg)
        last_scan_result = error_msg
        return False
    except FileNotFoundError:
        msg = "Command not found. Please ensure required tools are installed."
        print(msg)
        last_scan_result = msg
        return False



def signal_handler(sig, frame):
    print("\nProgram stopped. Goodbye!")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

def run_nmap_command(args):
    try:
        subprocess.run(["nmap"] + args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    return True

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input
        print("Invalid input. Please try again.")

lines = "---------------------------------------------------------------------->\n"
results = Fore.BLUE + "#RESULTS #...please wait...\n" + Fore.RESET

def basic_scanning():
    print(lines)
    print("Basic Scanning Options:\n")
    print("1. Scan Multiple Targets")
    print("2. Scan a Single Target")
    print("3. Scan a Range of Hosts")
    print("4. Scan an Entire Subnet")
    print("5. Scan Random Hosts")
    print("6. Perform an Aggressive Scan")
    print("7. Scan an IPv6 Target")
    choice = input("Enter your choice: ")
    if choice == "1":
        targets = input("Enter multiple targets (comma separated): ")
        if validate_target(targets):
            print("\n")
            print(results)
            logger.info(f"Starting basic scan on multiple targets: {targets}")
            safe_run_command(["nmap", "-sT", targets])
            print(lines)
        else:
            print("Invalid target input. Please try again.")
    elif choice == "2":
        target = input("Enter a single target: ")
        if validate_target(target):
            print("\n")
            print(results)
            logger.info(f"Starting basic scan on single target: {target}")
            safe_run_command(["nmap", target])
            print(lines)
        else:
            print("Invalid target input. Please try again.")
    elif choice == "3":
        target = input("Enter a target with range (e.g. 192.168.1.1-100): ")
        if validate_target(target):
            print("\n")
            print(results)
            logger.info(f"Starting range scan on: {target}")
            safe_run_command(["nmap", "-sT", target])
            print(lines)
        else:
            print("Invalid target input. Please try again.")
    elif choice == "4":
        target = input("Enter a target with subnet (e.g. 192.168.1.0/24): ")
        if validate_target(target):
            print("\n")
            print(results)
            logger.info(f"Starting subnet scan on: {target}")
            safe_run_command(["nmap", "-sT", target])
            print(lines)
        else:
            print("Invalid target input. Please try again.")
    elif choice == "5":
        target = input("Enter a target for random hosts: ")
        if validate_target(target):
            print("\n")
            print(results)
            logger.info(f"Starting random hosts scan on: {target}")
            safe_run_command(["nmap", "-iR", target])
            print(lines)
        else:
            print("Invalid target input. Please try again.")
    elif choice == "6":
        target = input("Enter a target for aggressive scan: ")
        if validate_target(target):
            print("\n")
            print(results)
            logger.info(f"Starting aggressive scan on: {target}")
            safe_run_command(["nmap", "-A", target])
            print(lines)
        else:
            print("Invalid target input. Please try again.")
    elif choice == "7":
        target = input("Enter an IPv6 target: ")
        if validate_target(target):
            print("\n")
            print(results)
            logger.info(f"Starting IPv6 scan on: {target}")
            safe_run_command(["nmap", "-6", target])
            print(lines)
        else:
            print("Invalid target input. Please try again.")

def discover_options():
    print(lines)
    print("Discover Options:\n")
    print("1. Only Single IP Protocol Ping")
    print("2. UDP Ping")
    print("3. CMP Address Mask Ping")
    print("4. ICMP Echo Ping")
    print("5. TCP ACK Ping")
    print("6. TCP SYN Ping")
    print("7. ICMP Timestamp Ping")
    print("8. SCTP INIT Ping")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter Target ip for single ping ")
        subprocess.run(["nmap", "-sP", target])
    elif choice == "2":
        target = input("Enter a target for UDP ping: ")
        subprocess.run(["nmap", "-sU", target])
    elif choice == "3":
        target = input("Enter ICMP Address Mask Ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PM", target])
        print(lines)
    elif choice == "4":
        target = input("Enter ECHO ICMP ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PE", target])
        print(lines)
    elif choice == "5":
        target = input("Enter TCP ACK ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PA", target])
        print(lines)
    elif choice == "6":
        target = input("Enter TCP SYN ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PS", target])
        print(lines)
    elif choice == "7":
        target = input("Enter ICMP Timestamp ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PP", target])
        print(lines)
    elif choice == "8":
        target = input("Enter IP protocol to ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PO", target])
        print(lines)
    #... implement other options...

def advanced_scanning_options():
    print(lines)
    print("Advanced Scanning Options:\n")
    print("1. TCP SYN Scan")
    print("2. TCP Connect Scan")
    print("3. UDP Scan")
    print("4. TCP NULL Scan")
    print("5. TCP FIN Scan")
    print("6. Xmas Scan")
    print("7. TCP ACK Scan")
    print("8. Custom TCP Scan")
    print("9. IP Protocol Scan")
    print("10. Send Raw Ethernet Packets")
    print("11. Send IP Packets")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter a target for TCP SYN scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sS", target])
        print(lines)
    elif choice == "2":
        target = input("Enter a target for TCP connect scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sT", target])
        print(lines)
    elif choice == "3":
        target = input("Enter a target for UDP connect scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sU", target])
        print(lines)
    elif choice == "4":
        target = input("Enter a target for TCP NULL scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sN", target])
        print(lines)
    elif choice == "5":
        target = input("Enter a target for TCP FIN scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sF", target])
        print(lines)    
    elif choice == "6":
        target = input("Enter a target for Xmas scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sX", target])
        print(lines)
    elif choice == "7":
        target = input("Enter a target for TCP ACK scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sA", target])
        print(lines)     
    elif choice == "8":
        target = input("Enter a target for Custom TCP scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-scanflags SYNFIN", target])
        print(lines)     
    elif choice == "9":
        target = input("Enter a target for Ip protocol scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sO", target])
        print(lines)     
    elif choice == "10":
        target = input("Enter a target for SendRaw Ethernet: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-send-eth", target])
        print(lines)     
    elif choice == "11":
        target = input("Enter a target for Send Ip Packets: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-send-ip", target])
        print(lines)   
        
    #... implement other options...

def port_scanning_options():
    print(lines)
    print("Port Scanning Options:\n")
    print("1. Perform a Fast Scan")
    print("2. Scan Specific Ports")
    print("3. Scan Ports by Name")
    print("4. Scan Ports by Protocol")
    print("5. Scan All Ports")
    print("6. Scan Top Ports")
    print("7. Perform a Sequential Port Scan")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter a target for fast scan: ")
        if validate_target(target):
            print("\n")
            print(results)
            logger.info(f"Starting fast scan on: {target}")
            safe_run_command(["nmap", "-F", target])
            print(lines)
        else:
            print("Invalid target input. Please try again.")
    elif choice == "2":
        target = input("Enter a target and specific ports (e.g. 22,80): ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-p", target])
        print(lines)        
    elif choice == "4":
        target = input("Enter a protocol port to scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sU", "-sT", "-p", "U:" + target])
        print(lines)
    elif choice == "3":
        target = input("Enter a target for Port Name To Scan: Example http, ftp - ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-p", target])
        print(lines)
    elif choice == "5":
        target = input("Enter Scan All Ports: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-p-", target])
        print(lines)
    elif choice == "6":
        target = input("Enter Scan Top Ports: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "--top-ports", target])
        print(lines)
    elif choice == "7":
        target = input("Enter Port to perform Sequential: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-r", target])
        print(lines)
    #... implement other options...

def version_detection():
    print(lines)
    print("Version Detection Options:\n")
    print("1. Operating System Detection")
    print("2. Attempt to Guess an Unknown OS")
    print("3. Service Version Detection")
    print("4. Troubleshooting Version Scans")
    print("5. Perform a RPC Scan")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter a target for OS detection: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-O", target])
        print(lines)
    elif choice == "2":
        target = input("Enter a target forunknown OS guess: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-O", "--osscan-guess", target])
        print(lines)
    elif choice == "3":
        target = input("Enter  Your Target: ")
        if validate_target(target):
            print("\n")
            print(results)
            logger.info(f"Starting service version detection on: {target}")
            safe_run_command(["nmap", "-sV", target])
            print(lines)
        else:
            print("Invalid target input. Please try again.")
    elif choice == "4":
        target = input("Enter Your Target: ")
        print("\n")
        print(results)
        subprocess.run(["nmap" , "-sV -version-trace" , target])
        print(lines)
    elif choice =="5":
        target = input("Enter Your Target: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sR", target])
        print(lines)
    #... implement other options...

def firewall_evasion_techniques():
    print(lines)
    print("Firewall Evasion Techniques:\n")
    print("1. Augment Packets")
    print("2. Pacify a Specific MTU")
    print("3. Use a Decoy")
    print("4. Spoof Mac Address")
    print("5. Le Zombie Scan")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter a target for augment packets: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-f", target])
        print(lines)
    elif choice == "2":
        target = input("Enter a target and MTU (e.g. 1500): ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "--mtu", target])
        print(lines)
    elif choice == "3":
            target = input("Enter a Decoy: ")
            print("\n")
            print(results)
            subprocess.run(["nmap" , "-D RND:", target ])
            print(lines)
    elif choice ==  "4":
              target = input("Enter a Mac Address: ")
              print("\n")
              print(results)
              subprocess.run(["nmap", "-spoof-mac", target])
              print(lines)
    elif choice == "5":
            target = input("Enter Le Zombie Target:")
            print("\n")
            print(results)
            subprocess.run(["nmap", " -sI", target])
            print(lines)
            
    #... implement other options...

def troubleshooting_and_debugging():
    print(lines)
    print("Troubleshooting and Debugging Options:\n")
    print("1. Trace Packet")
    print("2. Debugging")
    print("3. Open Ports")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter a target for trace packet: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "--packet-trace", target])
        print(lines)
    elif choice == "2":
        target = input("Enter a target for debugging: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-d", target])
        print(lines)
    elif choice == "3":
        target = input("Enter a target for open ports: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "--open", target])
        print(lines)
        
def fast_scan():
    print(lines)
    print("Fast Scan:\n")
    print("1. nslookup")
    print("2. whois")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter the Target: ")
        print("\n")
        print(results)
        subprocess.run(["nslookup", target])
        print(lines)
    elif choice == "2":
        target = input("Enter the Target: ")
        print("\n")
        print(results)
        subprocess.run(["whois", target])
        print(lines)
             
def trace_route():
    print(lines)
    print("Traceroute Menu:\n")
    print("1. Packet Routing")
    print("2. Packet Routing V4")
    print("3. Packet Routing V6")
    print("4. Do Not Fragment Packet")
    print("5. Start From The Ttl Hop")
    print("6. Route Packet Through The Gate")
    print("7. Set Max Number Of Hops")
    print("8. Don't Resolve Ip addr to Dns")
    print("9. Set Destination Port")
    print("10. Set Number Of Probes Per Hop")
    print("11. The Full Packet Length")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter packet Tracerouting: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", target])
        print(lines)
    elif choice == "2":
        target = input("Enter packet route V4: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "-4", target])
        print(lines)
    elif choice == "3":
        target = input("Enter packet route V6: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "-6", target])
        print(lines)
    elif choice == "4":
        target = input("Dont fragment packet: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "-F", target])
        print(lines)
    elif choice == "5":
        target = input("Enter your Target: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "-f", target])
        print(lines)
    elif choice == "6":
        target = input("Enter your Target: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "-g", target])
        print(lines)
    elif choice == "7":
        target = input("Enter target: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "-m", target])
        print(lines)
    elif choice == "8":
        target = input("Enter Your target: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "-n", target])
        print(lines)
    elif choice == "9":
        target = input("Enter Your target: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "-p", target])
        print(lines)
    elif choice == "10":
        target = input("Enter Your target: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "-q", target])
        print(lines)
    elif choice == "11":
        target = input("Enter Your target: ")
        print("\n")
        print(results)
        subprocess.run(["traceroute", "--packetlen", target])
        print(lines)
        #update checking program management
def check_for_update():
    update = "Checking for Update\n"
    print(Fore.CYAN + update + Fore.RESET)
    print("Y / N")
    choice = input("Enter your choice (Y/N): ").upper()

    if choice == "Y":
        try:
            subprocess.run(["git", "pull"], cwd="/home/zynix/projects/NetscanPro")
            print("Update completed.")
        except:
            print("Git pull failed. Please ensure you are in a git repository.")
    elif choice == "N":
        print("Update cancelled.\n")
    else:
        print("Invalid option. Please enter Y or N.")




def nse_scripts():
    print(lines)
    print("NSE Scripts Options:\n")
    print("1. Run Default Scripts")
    print("2. Run Vulnerability Scripts")
    print("3. Run Discovery Scripts")
    print("4. Run Specific Script")
    print("5. List Available Scripts")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter target: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sC", target])
        print(lines)
    elif choice == "2":
        target = input("Enter target: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "--script=vuln", target])
        print(lines)
    elif choice == "3":
        target = input("Enter target: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "--script=discovery", target])
        print(lines)
    elif choice == "4":
        script = input("Enter script name: ")
        target = input("Enter target: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "--script=" + script, target])
        print(lines)
    elif choice == "5":
        subprocess.run(["nmap", "--script-help"])
        print(lines)

def output_options():
    print(lines)
    print("Output Options:\n")
    print("1. Normal Output")
    print("2. XML Output")
    print("3. Grepable Output")
    print("4. Script Kiddie Output")
    print("5. All Formats")
    choice = input("Enter your choice: ")
    target = input("Enter target: ")
    scan_type = input("Enter scan type (e.g., -sS for SYN scan): ")
    if choice == "1":
        file = input("Enter output file name: ")
        subprocess.run(["nmap", scan_type, "-oN", file, target])
    elif choice == "2":
        file = input("Enter output file name: ")
        subprocess.run(["nmap", scan_type, "-oX", file, target])
    elif choice == "3":
        file = input("Enter output file name: ")
        subprocess.run(["nmap", scan_type, "-oG", file, target])
    elif choice == "4":
        file = input("Enter output file name: ")
        subprocess.run(["nmap", scan_type, "-oS", file, target])
    elif choice == "5":
        file = input("Enter output file name: ")
        subprocess.run(["nmap", scan_type, "-oA", file, target])

def timing_options():
    print(lines)
    print("Timing Options:\n")
    print("1. Paranoid")
    print("2. Sneaky")
    print("3. Polite")
    print("4. Normal")
    print("5. Aggressive")
    print("6. Insane")
    choice = input("Enter your choice: ")
    target = input("Enter target: ")
    if choice == "1":
        subprocess.run(["nmap", "-T0", target])
    elif choice == "2":
        subprocess.run(["nmap", "-T1", target])
    elif choice == "3":
        subprocess.run(["nmap", "-T2", target])
    elif choice == "4":
        subprocess.run(["nmap", "-T3", target])
    elif choice == "5":
        subprocess.run(["nmap", "-T4", target])
    elif choice == "6":
        subprocess.run(["nmap", "-T5", target])

def miscellaneous():
    print(lines)
    print("Miscellaneous Options:\n")
    print("1. Verbose Output")
    print("2. Debug Output")
    print("3. Resume Scan")
    print("4. Exclude Hosts")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter target: ")
        subprocess.run(["nmap", "-v", target])
    elif choice == "2":
        target = input("Enter target: ")
        subprocess.run(["nmap", "-d", target])
    elif choice == "3":
        file = input("Enter resume file: ")
        subprocess.run(["nmap", "--resume", file])
    elif choice == "4":
        exclude = input("Enter hosts to exclude: ")
        target = input("Enter target: ")
        subprocess.run(["nmap", "--exclude", exclude, target])

def configuration_menu():
    print(lines)
    print("Configuration Menu:\n")
    print("1. Load Configuration")
    print("2. Save Current Settings")
    print("3. View Current Configuration")
    choice = input("Enter your choice: ")
    if choice == "1":
        config = load_config()
        if config:
            print("Configuration loaded:")
            for key, value in config.items():
                print(f"{key}: {value}")
        else:
            print("No configuration file found.")
    elif choice == "2":
        # Example: save some settings
        config = {"default_scan_type": "basic", "verbose": True}
        save_config(config)
        print("Configuration saved.")
    elif choice == "3":
        config = load_config()
        if config:
            print("Current Configuration:")
            for key, value in config.items():
                print(f"{key}: {value}")
        else:
            print("No configuration loaded.")

def batch_processing_menu():
    print(lines)
    print("Batch Processing Menu:\n")
    print("Enter scan commands separated by semicolons (e.g., nmap -sS 192.168.1.1;nmap -sU 192.168.1.1)")
    commands_input = input("Enter commands: ")
    commands = [cmd.strip().split() for cmd in commands_input.split(';') if cmd.strip()]
    if commands:
        print("Starting batch processing...")
        batch_process(commands)
        print("Batch processing completed.")
    else:
        print("No valid commands entered.")

def generate_report_menu():
    from .report_gen import generate_professional_report
    print(lines)
    print("Generate Report Menu:\n")
    history = load_scan_history()
    if not history:
        print("No saved scans found. Please run and save a scan first.")
        return

    print("Available Scans:")
    for i, scan in enumerate(history, 1):
        print(f"{i}. {scan['name']} - {scan['target']} - {scan['timestamp']}")

    choice = input("Select scan number to generate report: ")
    try:
        scan_index = int(choice) - 1
        if 0 <= scan_index < len(history):
            selected_scan = history[scan_index]
            generate_professional_report(selected_scan)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")
