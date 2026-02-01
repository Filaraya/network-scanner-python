# Network Scanner - Python Port Scanner Tool
A Python-based network scanner for discovering active hosts and checking open ports on target systems. This educational project demonstrates networking fundamentals, socket programming, and security concepts.

__🎯 Project Overview__

This network scanner is a command-line tool that allows users to scan IP addresses for open ports, identify running services, and understand network security basics. Built as a learning project to demonstrate practical networking skills and Python programming capabilities.

__✨ Features__
- __Common Port Scanning:__ Scan well-known ports (FTP, SSH, HTTP, HTTPS, MySQL, etc.)
- __Custom Port Range Scanning:__ Scan any range of ports you specify
- __Single Port Checking:__ Test connectivity to a specific port
- __Service Detection:__ Automatically identifies common services running on open ports
- __Clean Output:__ Professional, easy-to-read scan results with summary statistics
- __Error Handling:__ Graceful handling of connection errors and invalid inputs
- __Local Network Information__ Displays your computer's IP address and hostname
  
__🚀 Getting Started__
__Prerequisites__
- Python 3.6 or higher
- No external dependencies required (uses standard library only)
__Installation__
1, Clone this repository:
```
git clone https://github.com/Filaraya/network-scanner-python.git
```
```
cd network-scanner-python
```
2, Run the scanner:
```python scanner.py```

__📖 Usage__
__Basic Usage__
Run the scanner and follow the interactive menu:
```python scanner.py```
__Scanning Options__
__Option 1: Scan Common Ports__
- Scans 13 well-known ports (FTP, SSH, HTTP, HTTPS, MySQL, etc.)
- Best for quick security assessment
- Example: Scan localh[IP_ADDRESS]0.0.1)
__Option 2: Scan Custom Port Range__
- Scan any range of ports you specify
- Useful for comprehensive network analysis
- Example: Scan ports 1-1000 on a target IP
__Option 3: Scan Single Port__
- Check if a specific port is open
- Quick connectivity test
Example: Check if port 443 is open on google.com
__Example Output__
Scanning Localhost (Closed Ports):
```
============================================================
Scanning common ports on 127.0.0.1
Scan started at: 2026-01-31 21:21:22
============================================================
✗ Port    21 | CLOSED  | FTP
✗ Port    22 | CLOSED  | SSH
✗ Port    80 | CLOSED  | HTTP
✗ Port   443 | CLOSED  | HTTPS
...
============================================================
SCAN SUMMARY
============================================================
Total ports scanned: 13
Open ports found: 0
Closed ports: 13
No open ports found.
============================================================
```

__Scanning Remote Server (Open Port):__
Enter target IP address: google.com
Enter port number: 443
Port 443 on google.com: OPEN
Service: HTTPS

__🔍 How It Works__
The scanner uses Python's socket library to:

1, Create TCP connections to target IP addresses and ports
2, Attempt to establish a connection with a timeout
3, Report whether the connection succeeded (OPEN) or failed (CLOSED)
4, Identify common services based on port numbers

__🎓 Learning Objectives__
This project demonstrates understanding of:

- __TCP/IP Protocol:__ How devices communicate over networks
- __Socket Programming:__ Creating and managing network connections
- __Port Numbers:__ How services are identified on networks
- __Network Security:__ Identifying open vs. closed ports
- __Error Handling:__ Managing connection failures and timeouts
- __Python Programming:__ Classes, functions, and user interaction
  
__⚠️ Important Notes__
__Ethical Use Only:__
- Only scan networks and devices you own or have explicit permission to scan
- Unauthorized port scanning may violate network policies or laws
- This tool is for educational purposes and personal learning
  
__Safety:__
- Start by scanning localh[IP_ADDRESS]0.0.1) to test functionality
- Be aware that scanning large port ranges can take time
- Some networks may detect and block port scanning activity

__🛠️ Technical Details__
__Built With:__

- Python 3.x
- Standard Library: socket, datetime
  
__Supported Platforms:__
- Windows
- macOS
- Linux
  
__Common Ports Scanned:__
- 21 (FTP)
- 22 (SSH)
- 23 (Telnet)
- 25 (SMTP)
- 53 (DNS)
- 80 (HTTP)
- 110 (POP3)
- 143 (IMAP)
- 443 (HTTPS)
- 3306 (MySQL)
- 3389 (RDP)
- 5432 (PostgreSQL)
- 8080 (HTTP-Proxy)

__🚧 Future Enhancements__
Planned features for future versions:

 - Multi-threading for faster scanning
 - Save scan results to CSV/JSON files
 - Progress bar for long-running scans
 - Command-line arguments for automation
 - Network discovery (find all devices on local network)
 - Service version detection
 - Web interface using Flask
 - AWS integration (scan EC2 instances)
   
__📝 License__
This project is open source and available for educational purposes.

__👤 Author__
Filmon Araya

Building networking skills for System Development Engineer role
Learning Python, networking fundamentals, and cloud technologies
Portfolio: https://github.com/Filaraya

__🙏 Acknowledgments__
Built as part of self-development learning journey
Inspired by network security tools like Nmap
Created to demonstrate practical networking knowledge

Note: This is an educational project created for learning purposes. Always use responsibly and ethically.
