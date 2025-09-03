# NetscanPro.py
from modules import *
from colorama import Fore, Style, init


init(autoreset=True)


def main():
    while True:
        owner = "GitHub By: MrpasswordTz\n"
        print(Fore.RED + owner +Fore.RESET)

        print("NetScannerPro Menu:\n")
        print("1.  Basic Scanning")
        print("2.  Discover Options")
        print("3.  Advanced Scanning Options")
        print("4.  Port Scanning Options")
        print("5.  Version Detection")
        print("6.  Firewall Evasion Techniques")
        print("7.  Troubleshooting and Debugging")
        print("8.  Fast Scan")
        print("9.  Traceroute")
        print("10. NSE Scripts")
        print("11. Output Options")
        print("12. Timing Options")
        print("13. Miscellaneous")
        print("14. Configuration")
        print("15. Batch Processing")
        print("16. Generate Report")
        print("99. Update Script\n")
        print("0. Exit")
        choice = input("Enter your choice: ")
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
        elif choice == "10":
             nse_scripts()
        elif choice == "11":
             output_options()
        elif choice == "12":
             timing_options()
        elif choice == "13":
             miscellaneous()
        elif choice == "14":
             configuration_menu()
        elif choice == "15":
             batch_processing_menu()
        elif choice == "16":
             generate_report_menu()
        elif choice == "99":
             check_for_update()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
