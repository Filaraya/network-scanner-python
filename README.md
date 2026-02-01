Network Scanner - Python Port Scanner Tool
A Python-based network scanner for discovering active hosts and checking open ports on target systems. This educational project demonstrates networking fundamentals, socket programming, and security concepts.

🎯 Project Overview
This network scanner is a command-line tool that allows users to scan IP addresses for open ports, identify running services, and understand network security basics. Built as a learning project to demonstrate practical networking skills and Python programming capabilities.

✨ Features
Common Port Scanning: Scan well-known ports (FTP, SSH, HTTP, HTTPS, MySQL, etc.)
Custom Port Range Scanning: Scan any range of ports you specify
Single Port Checking: Test connectivity to a specific port
Service Detection: Automatically identifies common services running on open ports
Clean Output: Professional, easy-to-read scan results with summary statistics
Error Handling: Graceful handling of connection errors and invalid inputs
Local Network Information: Displays your computer's IP address and hostname
🚀 Getting Started
Prerequisites
Python 3.6 or higher
No external dependencies required (uses standard library only)
Installation
1, Clone this repository:
git clone https://github.com/YOUR_USERNAME/network-scanner-python.git
cd network-scanner-python
2, Run the scanner:
python scanner.py
📖 Usage
Basic Usage
Run the scanner and follow the interactive menu:
python scanner.py
Scanning Options
Option 1: Scan Common Ports

Scans 13 well-known ports (FTP, SSH, HTTP, HTTPS, MySQL, etc.)
Best for quick security assessment
Example: Scan localh[IP_ADDRESS]0.0.1)
Option 2: Scan Custom Port Range

Scan any range of ports you specify
Useful for comprehensive network analysis
Example: Scan ports 1-1000 on a target IP
Option 3: Scan Single Port

Check if a specific port is open
Quick connectivity test
Example: Check if port 443 is open on google.com
Example Output
Scanning Localhost (Closed Ports):

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
Scanning Remote Server (Open Port):

Enter target IP address: google.com
Enter port number: 443

Port 443 on google.com: OPEN
Service: HTTPS
🔍 How It Works
The scanner uses Python's socket library to:

Create TCP connections to target IP addresses and ports
Attempt to establish a connection with a timeout
Report whether the connection succeeded (OPEN) or failed (CLOSED)
Identify common services based on port numbers
🎓 Learning Objectives
This project demonstrates understanding of:

TCP/IP Protocol: How devices communicate over networks
Socket Programming: Creating and managing network connections
Port Numbers: How services are identified on networks
Network Security: Identifying open vs. closed ports
Error Handling: Managing connection failures and timeouts
Python Programming: Classes, functions, and user interaction
⚠️ Important Notes
Ethical Use Only:

Only scan networks and devices you own or have explicit permission to scan
Unauthorized port scanning may violate network policies or laws
This tool is for educational purposes and personal learning
Safety:

Start by scanning localh[IP_ADDRESS]0.0.1) to test functionality
Be aware that scanning large port ranges can take time
Some networks may detect and block port scanning activity
🛠️ Technical Details
Built With:

Python 3.x
Standard Library: socket, datetime
Supported Platforms:

Windows
macOS
Linux
Common Ports Scanned:

21 (FTP)
22 (SSH)
23 (Telnet)
25 (SMTP)
53 (DNS)
80 (HTTP)
110 (POP3)
143 (IMAP)
443 (HTTPS)
3306 (MySQL)
3389 (RDP)
5432 (PostgreSQL)
8080 (HTTP-Proxy)
🚧 Future Enhancements
Planned features for future versions:

 Multi-threading for faster scanning
 Save scan results to CSV/JSON files
 Progress bar for long-running scans
 Command-line arguments for automation
 Network discovery (find all devices on local network)
 Service version detection
 Web interface using Flask
 AWS integration (scan EC2 instances)
📝 License
This project is open source and available for educational purposes.

👤 Author
Filmon Araya

Building networking skills for System Development Engineer role
Learning Python, networking fundamentals, and cloud technologies
Portfolio: [Your GitHub Profile]
🙏 Acknowledgments
Built as part of self-development learning journey
Inspired by network security tools like Nmap
Created to demonstrate practical networking knowledge
---
Note: This is an educational project created for learning purposes. Always use responsibly and ethically.
