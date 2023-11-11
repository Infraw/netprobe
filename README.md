# NetProbe ![Python Version](https://img.shields.io/badge/python-3.8%2B-blue) [![License](https://img.shields.io/badge/license-GPLv3-green)](LICENSE)
NetProbe is a command-line interface (CLI) tool for network and port scanning. It provides functionality to discover active hosts on a network and perform port scans on specified hosts.
## Features
* Network Scan: Discover active hosts on a specified IP range.
* Port Scan: Perform a port scan on the specified host within a given port range.
## Prerequisites
* Python 3.x
* Scapy
* (Optional for network scan) Root or superuser privileges
## Installation
1. Clone Repository:
```
git clone https://github.com/Infraw/netprobe.git
cd NetProbe
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
## Usage
For network scan:
```
sudo python netprobe.py -n [ip-range]
```
For port scan:
```
python netprobe.py -p <host> [start-port] [end-port]
```
## Notes
* Ensure you have root or superuser privileges (sudo) for the network scan.
* For port scan, the specified host and port range are required.
## Licencse
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
## Disclaimer
NetProbe is a tool designed for educational and informational purposes only.
The authors and contributors of this tool are not responsible for any misuse, damage, or illegal activities caused by the use of this software.
Users are solely responsible for their actions and must comply with all applicable laws and regulations.
By using NetProbe, you agree to use it at your own risk.
