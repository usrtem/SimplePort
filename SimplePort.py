import socket
from datetime import datetime

def scan_port(target, port):
    """
    Function to scan a single port and check if it's open.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt
        result = s.connect_ex((target, port))  # Attempt to connect to the port
        if result == 0:
            try:
                service = socket.getservbyport(port)  # Try to identify the service
            except:
                service = "Unknown"
            print(f"Port {port}: Open - Service: {service}")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def port_scanner(target, start_port, end_port):
    """
    Function to scan a range of ports on a target IP address.
    """
    print(f"\nStarting scan on target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}")
    print(f"Scan started at: {str(datetime.now())}")
    print("-" * 50)

    try:
        for port in range(start_port, end_port + 1):
            scan_port(target, port)
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        exit()
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        exit()
    except socket.error:
        print("Could not connect to the server. Exiting.")
        exit()

    print("-" * 50)
    print(f"Scan completed at: {str(datetime.now())}")

if __name__ == "__main__":
    # Prompt the user for input
    target = input("Enter the target IP address or hostname: ")
    
    while True:
        try:
            start_port = int(input("Enter the starting port number (e.g., 1): "))
            end_port = int(input("Enter the ending port number (e.g., 1024): "))
            
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                raise ValueError("Invalid port range. Ports must be between 1 and 65535.")
            
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid range.")

    # Start scanning
    port_scanner(target, start_port, end_port)

    # Pause at the end to keep the window open
    input("\nScan complete. Press Enter to exit...")
