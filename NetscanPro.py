import subprocess
import os
import signal
from colorama import Fore, init

init()  # Initialize colorama

banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⢻⠋⡏⢛⢹⢹⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠤⠤⠤⠤⣄⣀⣀⠀⠀⢸⣿⢸⣀⡇⢸⣾⢸⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⣮⣿⠛⠉⠉⠉⠉⢻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠟⣩⣿⣶⢰⣖⠒⣶⣼⣀⣀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⠀⠀⠀⠀⠀⠀⣴⣖⣲⣦⠤⣿⣿⡞⠁⠙⠛⠛⢻⡿⠁⡼⠋⢀⣈⡬⠶⠛⠋⠉⠉⠉⠉⠉⠉⢉⣩⠽⠛⣛⣽⠿⣟⣛⣛⣛⡛⠲⢤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⠤⣤⣀⡈⣇⠀⠀⠀⠀⢸⣿⣿⠶⠾⣿⡿⠋⢹⠀⠀⠀⣠⡏⢀⣞⡵⢞⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⣠⢶⣻⠵⡞⣏⠁⠀⠀⠀⠉⠙⠲⣌⡑⢦⡀⠀⠀
⠀⠀⠀⣼⢿⠵⢶⣼⣷⠛⠛⣧⣄⠀⠀⢸⣇⣿⣗⣊⣿⠖⠀⢸⠀⢶⢯⣭⠟⢋⡞⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⣠⠞⡵⢻⡁⠀⢹⡼⡄⠀⠀⠀⠀⠀⠀⠀⠙⢦⡹⣄⠀
⠀⠀⠀⣿⢸⠀⢾⠁⠈⣳⠞⢛⣿⣟⠶⣿⣿⣻⠿⢽⣿⣦⣀⡼⠀⢸⠶⡇⠀⢸⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⢀⡜⢡⡞⠁⠀⡇⠀⠀⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡹⡄
⠀⠀⠀⠙⠛⠒⢚⣷⠞⣡⢞⡉⠀⠹⣿⣮⠙⣿⠯⠟⠉⢹⡿⣤⣀⠸⡶⣧⣀⡸⡄⢹⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⡼⢠⠏⠀⠀⠀⣷⠀⠀⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⢻
⠀⢀⣤⠶⢶⣴⠋⣠⢾⡇⠹⣷⣄⠀⠉⠻⣷⡼⣳⣤⣴⣿⣷⡇⢨⣽⣿⣿⠿⣝⣿⣾⣆⠀⠀⠀⠀⠀⠀⢸⠁⠀⡇⡞⠀⠀⠀⢰⠃⠀⢸⢳⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸
⠀⡸⠹⢾⣖⣛⣿⣅⠀⢧⠀⠈⢻⣧⡀⠀⠘⠻⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣦⣬⡿⣿⣿⣦⡀⠀⠀⠀⠀⠘⡆⠀⡇⣇⠀⠀⣠⠋⠀⢠⢏⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸
⣶⠃⠀⠈⠋⢻⢴⣗⣻⣮⣷⡀⠀⢹⣟⣦⡄⠀⠈⠛⠉⡹⠉⠈⠓⢿⡿⣿⣿⣿⠷⣄⣹⡆⠙⠲⣄⡀⠀⠀⢿⠀⢧⠸⡶⠚⠁⢀⡴⢣⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢸
⠛⢦⡀⠀⠀⠀⢸⠋⠀⠀⢈⡿⡄⢸⣺⡀⠀⠀⠀⠀⢠⡇⡾⣦⡀⠀⠉⢿⣿⠻⣷⣮⠟⢁⣀⣀⣨⣿⣷⣤⡈⢧⠈⣇⠳⣤⠖⣩⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢁⠇
⠀⠀⠙⢦⡀⠀⡏⠀⠀⠀⡼⠀⠙⣎⠙⣿⣾⣷⡀⠀⠘⢧⢿⣻⡇⢠⣄⠘⠿⠿⠻⠿⣼⡟⢷⣿⣿⣾⠯⠿⠋⠛⠧⣈⢦⡙⣏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⠊⠀
⠀⠀⠀⠀⠈⠻⠥⠤⠤⠼⠁⠀⠀⠘⢿⣿⡿⣏⣹⣆⠀⠀⠻⣍⠀⢸⣏⠳⡄⠀⠀⠀⠀⠑⢤⣿⣙⣟⣄⠀⠀⢠⡤⠬⠿⢿⣌⡓⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⠴⣣⠞⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠈⢠⡾⣷⡀⠀⠈⠳⣜⢟⣾⠀⢰⣄⡀⠀⣴⣾⢿⣽⡿⣞⣆⠀⠀⢻⡋⠉⠙⢧⢻⡳⢦⣉⡑⠲⠶⠶⠶⢒⣫⠵⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠳⣝⢿⣦⠀⠀⠈⠳⣍⠀⣞⡇⢹⣶⡏⡇⠀⠙⢿⣹⣜⢦⠀⠀⠳⣄⣀⣬⣷⣷⡄⢳⡌⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠈⢦⡙⣷⠀⠀⠀⠈⠳⣝⠓⣸⢠⢇⡇⠀⠀⠀⠀⠹⣎⢧⠀⠀⠻⣄⣀⣀⣹⡿⡄⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣆⠀⠀⠀⠀⢻⠃⠀⠀⠀⠀⠀⠈⠣⡍⢸⢸⠀⠀⠀⠀⠀⠀⠘⣆⢣⡀⠀⠙⣧⠴⠛⢣⠘⣄⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠘⣆⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣼⡀⠀⠀⠀⠀⠀⢀⡼⣶⠗⠦⡄⠘⣆⠀⠀⣳⣸⡆⠘⣦⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⣦⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠀⠀⠀⢀⡏⢀⠘⡆⠀⠹⣶⢮⡉⠉⠀⠀⠀⠀⠈⢯⠉⠙⣎⢻⡉⠑⢦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠋⢧⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⢸⢸⠋⡇⣷⠀⠀⣏⡇⣷⠤⣤⡤⠤⠤⠤⢤⡇⠀⠸⡄⢇⠀⠸⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⠈⣧⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠈⡞⠦⠇⡿⠀⠀⡿⡇⣹⣶⣾⡷⠖⠲⣶⣟⠀⠀⠀⡇⢸⠀⢠⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⣸⠀⠀⡼⢳⡀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡻⣄⣠⡇⣀⡴⠃⡇⢻⠀⠀⠳⣤⡤⠇⠈⢦⡀⠀⡇⢸⣧⠞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⡇⠀⢳⡀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠉⠉⠁⡀⠀⡇⢈⣀⣁⡀⢉⣀⣉⣉⣉⣷⡀⡇⢸⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⡇⠀⠀⣿⡜⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠙⢦⡇⠘⠒⠒⠒⠒⠒⠒⠒⠒⠺⠟⠃⢸⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⢰⠇⠀⠀⢸⠻⡜⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠛⠛⠉⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠀⠀⠀⢸⠂⠙⡎⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣀⣀⣀⡈⠂
"""

print(Fore.GREEN + banner + Fore.RESET)



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

def basic_scanning():
    print("Basic Scanning Options:")
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
        subprocess.run(["nmap", "-sT", targets])
    elif choice == "2":
        target = input("Enter a single target: ")
        subprocess.run(["nmap", target])
    elif choice == "3":
        target = input("Enter a target with range (e.g. 192.168.1.1-100): ")
        subprocess.run(["nmap", "-sT", target])
    elif choice == "4":
        target = input("Enter a target with subnet (e.g. 192.168.1.0/24): ")
        subprocess.run(["nmap", "-sT", target])
    elif choice == "5":
        target = input("Enter a target for random hosts: ")
        subprocess.run(["nmap", "-iR", target])
    elif choice == "6":
        target = input("Enter a target for aggressive scan: ")
        subprocess.run(["nmap", "-A", target])
    elif choice == "7":
        target = input("Enter an IPv6 target: ")
        subprocess.run(["nmap", "-6", target])

def discover_options():
    print("Discover Options:")
    print("1. IP Protocol Ping")
    print("2. UDP Ping")
    print("3. CMP Address Mask Ping")
    print("4. ICMP Echo Ping")
    print("5. TCP ACK Ping")
    print("6. TCP SYN Ping")
    print("7. ICMP Timestamp Ping")
    print("8. SCTP INIT Ping")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter a target for IP protocol ping: ")
        subprocess.run(["nmap", "-sP", target])
    elif choice == "2":
        target = input("Enter a target for UDP ping: ")
        subprocess.run(["nmap", "-sU", target])
    #... implement other options...

def advanced_scanning_options():
    print("Advanced Scanning Options:")
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
        subprocess.run(["nmap", "-sS", target])
    elif choice == "2":
        target = input("Enter a target for TCP connect scan: ")
        subprocess.run(["nmap", "-sT", target])
    #... implement other options...

def port_scanning_options():
    print("Port Scanning Options:")
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
        subprocess.run(["nmap", "-F", target])
    elif choice == "2":
        target = input("Enter a target and specific ports (e.g. 22,80): ")
        subprocess.run(["nmap", "-p", target])
    #... implement other options...

def version_detection():
    print("Version Detection Options:")
    print("1. Operating System Detection")
    print("2. Attempt to Guess an Unknown OS")
    print("3. Service Version Detection")
    print("4. Troubleshooting Version Scans")
    print("5. Perform a RPC Scan")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter a target for OS detection: ")
        subprocess.run(["nmap", "-O", target])
    elif choice == "2":
        target = input("Enter a target forunknown OS guess: ")
        subprocess.run(["nmap", "-O", "--osscan-guess", target])
    #... implement other options...

def firewall_evasion_techniques():
    print("Firewall Evasion Techniques:")
    print("1. Augment Packets")
    print("2. Pacify a Specific MTU")
    print("3. Use a Decoy")
    print("4. Spoof Mac Address")
    print("5. Le Zombie Scan")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter a target for augment packets: ")
        subprocess.run(["nmap", "-f", target])
    elif choice == "2":
        target = input("Enter a target and MTU (e.g. 1500): ")
        subprocess.run(["nmap", "--mtu", target])
    #... implement other options...

def troubleshooting_and_debugging():
    print("Troubleshooting and Debugging Options:")
    print("1. Trace Packet")
    print("2. Debugging")
    print("3. Open Ports")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = input("Enter a target for trace packet: ")
        subprocess.run(["nmap", "--packet-trace", target])
    elif choice == "2":
        target = input("Enter a target for debugging: ")
        subprocess.run(["nmap", "-d", target])
    elif choice == "3":
        target = input("Enter a target for open ports: ")
        subprocess.run(["nmap", "--open", target])

def main():
    while True:
        owner = "GitHub By: MrpasswordTz\n"
        print(owner)
        
        print("NetScannerPro Menu:\n")
        print("1. Basic Scanning")
        print("2. Discover Options")
        print("3. Advanced Scanning Options")
        print("4. Port Scanning Options")
        print("5. Version Detection")
        print("6. Firewall Evasion Techniques")
        print("7. Troubleshooting and Debugging")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            basic_scanning()
        elif choice == "2":
            discover_options()
        elif choice == "3":
            advanced_scanning_options()
        elif choice == "4":
            port_scanning_options()
        elif choice == "5":
            version_detection()
        elif choice == "6":
            firewall_evasion_techniques()
        elif choice == "7":
            troubleshooting_and_debugging()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
