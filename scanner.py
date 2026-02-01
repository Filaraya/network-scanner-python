
"""
Network Scanner - Main Entry Point
===================================
A simple network scanner that discovers active hosts and checks for open ports.

Author: Your Name
Date: February 2026
Purpose: Learning project for networking fundamentals and portfolio building
"""

import socket
from datetime import datetime

class NetworkScanner:
    """
    Main network scanner class that handles port scanning and host discovery
    """
    
    def __init__(self):
        self.common_ports = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            3306: "MySQL",
            3389: "RDP",
            5432: "PostgreSQL",
            8080: "HTTP-Proxy"
        }
    
    def get_local_ip(self):
        """Get the local IP address of this machine"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception as e:
            return f"Unable to determine: {e}"
    
    def scan_port(self, target_ip, port, timeout=1):
        """
        Scan a single port on the target IP
        
        Args:
            target_ip: IP address to scan
            port: Port number to check
            timeout: Connection timeout in seconds
            
        Returns:
            dict: Port status and service information
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((target_ip, port))
            sock.close()
            
            if result == 0:
                service = self.common_ports.get(port, "Unknown")
                return {
                    "port": port,
                    "status": "OPEN",
                    "service": service
                }
            else:
                return {
                    "port": port,
                    "status": "CLOSED",
                    "service": None
                }
        except socket.gaierror:
            return {
                "port": port,
                "status": "ERROR",
                "service": "Hostname resolution failed"
            }
        except socket.error:
            return {
                "port": port,
                "status": "ERROR",
                "service": "Connection error"
            }
    
    def scan_common_ports(self, target_ip):
        """
        Scan all common ports on the target IP
        
        Args:
            target_ip: IP address to scan
            
        Returns:
            list: List of scan results for each port
        """
        print(f"{'='*60}")
        print(f"Scanning common ports on {target_ip}")
        print(f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
              
        
        results = [] #pylint: disable=unused-variable
        open_ports = []
        
        for port in self.common_ports.keys():
            result = self.scan_port(target_ip, port)
            results.append(result)
            
            if result["status"] == "OPEN":
                open_ports.append(result)
                print(f"✓ Port {port:5d} | OPEN    | {result['service']}")
            else:
                print(f"✗ Port {port:5d} | CLOSED  | {self.common_ports[port]}")
        
        print(f"{'='*60}")
        print(f"Scan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        return results, open_ports
    
    def scan_port_range(self, target_ip, start_port, end_port):
        """
        Scan a range of ports on the target IP
        
        Args:
            target_ip: IP address to scan
            start_port: Starting port number
            end_port: Ending port number
            
        Returns:
            list: List of open ports found
        """
        print(f"{'='*60}")
        print(f"Scanning ports {start_port}-{end_port} on {target_ip}")
        print(f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        open_ports = []
        
        for port in range(start_port, end_port + 1):
            result = self.scan_port(target_ip, port, timeout=0.5)
            
            if result["status"] == "OPEN":
                open_ports.append(result)
                service = self.common_ports.get(port, "Unknown")
                print(f"✓ Port {port:5d} | OPEN | {service}")
        
        print(f"{'='*60}")
        print(f"Scan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total open ports found: {len(open_ports)}")
        print(f"{'='*60}")
        
        return open_ports
    
    def display_summary(self, results, open_ports):
        """Display a summary of scan results"""
        print("" + "="*60)
        print("SCAN SUMMARY")
        print("="*60)
        print(f"Total ports scanned: {len(results)}")
        print(f"Open ports found: {len(open_ports)}")
        print(f"Closed ports: {len(results) - len(open_ports)}")
        
        if open_ports:
            print("Open Ports Details:")
            print("-" * 60)
            for port_info in open_ports:
                print(f"  Port {port_info['port']:5d} - {port_info['service']}")
        else:
            print("No open ports found.")
        
        print("="*60 + "")


def main():
    """Main function to run the network scanner"""
    scanner = NetworkScanner()
    
    print("" + "="*60)
    print("NETWORK SCANNER v1.0")
    print("="*60)
    print("A simple port scanner for learning networking fundamentals")
    print("="*60 + "")
    
    # Display local network information
    print("Your Network Information:")
    print(f"  Local IP Address: {scanner.get_local_ip()}")
    print(f"  Hostname: {socket.gethostname()}")
    print()
    
    # Menu
    print("Select scanning mode:")
    print("1. Scan common ports (FTP, SSH, HTTP, HTTPS, etc.)")
    print("2. Scan custom port range")
    print("3. Scan single port")
    print("4. Exit")
    print()
    
    try:
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            target = input("Enter target IP address (or press Enter for [IP_ADDRESS]): ").strip()
            if not target:
                target = "[IP_ADDRESS]"
            
            results, open_ports = scanner.scan_common_ports(target)
            scanner.display_summary(results, open_ports)
            
        elif choice == "2":
            target = input("Enter target IP address: ").strip()
            start = int(input("Enter start port: ").strip())
            end = int(input("Enter end port: ").strip())
            
            if start > end:
                print("Error: Start port must be less than end port")
                return
            
            open_ports = scanner.scan_port_range(target, start, end)
            
        elif choice == "3":
            target = input("Enter target IP address: ").strip()
            port = int(input("Enter port number: ").strip())
            
            result = scanner.scan_port(target, port)
            print(f"Port {port} on {target}: {result['status']}")
            if result['service']:
                print(f"Service: {result['service']}")
            
        elif choice == "4":
            print("Exiting scanner. Goodbye!")
            return
        
        else:
            print("Invalid choice. Please run the program again.")
    
    except KeyboardInterrupt:
        print("Scan interrupted by user. Exiting...")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()