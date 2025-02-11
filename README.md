# SimplePort
SimplePort is a basic port scanner written and runs using Python

## Description

This is a simple Python port scanner that allows users to input a target IP address or hostname and a range of ports to scan. The script attempts to connect to each port in the specified range to determine if it is open. If a port is open, it tries to identify the service running on that port.

## Features

- Scans a user-defined range of ports.
- Attempts to identify services running on open ports.
- Handles common exceptions such as invalid hostnames or connection issues.
- Provides a timestamped summary of the scanning process.

## Prerequisites

- Python 3.x

## Usage

1.  Save the script to a file, e.g., `port_scanner.py`.
2.  Run the script from the command line:

    ```
    python port_scanner.py
    ```
3.  Enter the target IP address or hostname when prompted.
4.  Enter the starting and ending port numbers to define the range of ports to scan.

    Example:
    ```
    Enter the target IP address or hostname: 127.0.0.1
    Enter the starting port number (e.g., 1): 20
    Enter the ending port number (e.g., 1024): 25
    ```

## Example Output
Starting scan on target: 127.0.0.1
Scanning ports from 20 to 25
Scan started at: 2025-02-11 09:32:00
Port 21: Open - Service: ftp
Port 22: Open - Service: ssh
Scan completed at: 2025-02-11 09:32:10

## Notes

- Scanning privileged ports (below 1024) might require administrative/root access depending on your system.
- The timeout for each connection attempt is set to 1 second. You can adjust this in `s.settimeout(1)`.
- Use this script responsibly and only on systems you own or have explicit permission to scan.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests.
