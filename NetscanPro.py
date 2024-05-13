import subprocess
import os
import signal
from colorama import Fore, init
import pyfiglet

init()  # Initialize colorama

banner = pyfiglet.figlet_format("NETSCAN PRO")

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
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sT", targets])
        print(lines)
    elif choice == "2":
        target = input("Enter a single target: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", target])
        print(lines)
    elif choice == "3":
        target = input("Enter a target with range (e.g. 192.168.1.1-100): ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sT", target])
        print(lines)
    elif choice == "4":
        target = input("Enter a target with subnet (e.g. 192.168.1.0/24): ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sT", target])
        print(lines)
    elif choice == "5":
        target = input("Enter a target for random hosts: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-iR", target])
        print(lines)
    elif choice == "6":
        target = input("Enter a target for aggressive scan: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-A", target])
        print(lines)
    elif choice == "7":
        target = input("Enter an IPv6 target: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-6", target])
        print(lines)

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
    elif choice == "'3":
        target = input("Enter CMP Address Mask Ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PM",  target])
        print(lines)
    elif choice == "'4 ":
        target = input("Enter ECHO ICM ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PE",  target])
        print(lines)     
    elif choice == "'5":
        target = input("Enter TCP ACK ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PA",  target])
        print(lines)        
    elif choice == "'7":
        target = input("Enter ICMP TimeStamp ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-PP",  target])
        print(lines)
    elif choice == "'6":
        target = input("Enter TCP SYN ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "PS",  target])
        print(lines)  
    elif choice == "'8":
        target = input("Enter ip protocol to ping: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "PO",  target])
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
        target = input("Enter a target for X-mass scan: ")
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
        print("\n")
        print(results)
        subprocess.run(["nmap", "-F", target])
        print(lines)
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
        subprocess.run(["nmap", "-sU -sT -pU:", target])
        print(lines)
    elif choice == "3":
        target = input("Enter a target for Port Name To Scan: Example http, Ftp- ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-p", target])
        print(lines) 
    elif choice == "'5":
        target = input("Enter Scan All Ports: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-p-",  target])
        print(lines) 
    elif choice == "6":
        target = input("Enter Scan Top Ports: ")
        print("\n")()
        print(results)
        subprocess.run(["nmap", "-top-ports",  target])
        print(lines)  
    elif choice == "'7":
        target = input("Enter Port to perfom Sequential: ")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-r",  target])
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
        target = input("Enter  Your Target")
        print("\n")
        print(results)
        subprocess.run(["nmap", "-sV", target])
        print(lines)   
    elif choice == "4":
        target = input("Enter Your Target")
        print("\n")
        print(results)
        subprocess.run(["nmap" , "-sV -version-trace" , target])
        print(lines)
    elif choice =="5":
        target = input("Enter Your Target")
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
            target = input("Enter a Decoy")
            print("\n")
            print(results)
            subprocess.run(["nmap" , "-D RND:", target ])
            print(lines)
    elif choice ==  "4":
              target = input("Enter a Mac Address")
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
        print("1.nslookup")
        print("2.whois")
        choice = input("Enter your choice:")
        if choice == "1":
            target = input("Enter the Target:")
            print("\n")
            print(results)
            subprocess.run(["nslookup",  target])
            print(lines)
        elif choice == "2":
             target = input("Enter the Target:")
             print("\n")
             print(results)
             subprocess.run(["whois" , target])
             print(lines)
             
 #...packate routing function
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
                          print("8. Don't Reslove Ip addr to Dns")
                          print("9. Set Destination Port")
                          print("10.Set Number Of Probes Per Hop")
                          print("11. The Full Packet Length")
                          choice = input("Enter your choice\n")
                          if choice == "1":
                              target = input("Enter  packet Tracerouting")
                              print("\n")
                              print(results)
                              subprocess.run(["traceroute" , target])
                              print(lines)
                          elif choice == "'2":
                              target = input("Enter packet route V4: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-4",  target])
                              print(lines)     
                          elif choice == "'2":
                              target = input("Enter packet route V4: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-4",  target])
                              print(lines)        
                          elif choice == "'3":
                              target = input("Enter packet route V6: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-6",  target])
                              print(lines)
                          elif choice == "'4":
                              target = input("Dont fragment packet: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-F",  target])
                              print(lines)     
                          elif choice == "5":
                              target = input("Enter your Target: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-f",target])
                              print(lines)
                          elif choice == "'6":
                              target = input("Enter your Target: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-g",  target])
                              print(lines)
                          elif choice == "'7":
                              target = input("Enter target: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-m",  target])
                              print(lines)
                          elif choice == "'8":
                              target = input("Enter Your target: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-n",  target])
                              print(lines)
                          elif choice == "'9":
                              target = input("Enter Your target: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-p",  target])
                              print(lines)  
                          elif choice == "'10":
                              target = input("Enter Your target: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-q",  target])
                              print(lines)
                          elif choice == "'11":
                              target = input("Enter Your target: ")
                              print("\n")
                              print(results)
                              subprocess.run(["tracetroute", "-packetlen",  target])
                              print(lines)                                                                                                                                                                                                                                     
        #update checking program management
def check_for_update():
    print("Checking for Update\n")
    print("Y / N")
    choice = input("Enter your choice (Y/N): ").upper()

    if choice == "Y":
        subprocess.run(["git", "clone", "https://github.com/MrpasswordTz/NetscanPro/blob/main/NetscanPro.py"])
    elif choice == "N":  # Correct indentation for the elif block
        print("Update cancelled.\n")
    else:
        print("Invalid option. Please enter Y or N.")

#.........Readerbility lines That Separate Between options/results..........
lines = "---------------------------------------------------------------------->\n"
#....line variable ending here...........


## PRINTED OUTPUT RESULTS VARIABLE
results = Fore.BLUE + "#RESULTS #...please wait...\n" + Fore.RESET


def main():
    while True:
        owner = "GitHub By: MrpasswordTz\n"
        print(Fore.RED + owner +Fore.RESET)
        
        print("NetScannerPro Menu:\n")
        print("1. Basic Scanning")
        print("2. Discover Options")
        print("3. Advanced Scanning Options")
        print("4. Port Scanning Options")
        print("5. Version Detection")
        print("6. Firewall Evasion Techniques")
        print("7. Troubleshooting and Debugging")
        print("8. Fast Scan")
        print("9. Traceroute")
        print("99.Update Script\n")
        print("0. Exit")
        choice = input("Enter your choice: \n")
        print("\n")
        print("\n")
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
        elif choice == "8":
            fast_scan()    
        elif choice == "9":
             trace_route()
        elif choice == "99":
             check_for_update()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
