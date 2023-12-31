import argparse
import os
import scanners

def check_sudo():
    # Check user has root privileges.
    return os.geteuid() == 0

def main():
    parser = argparse.ArgumentParser(prog='NetProbe',
                                     description='A CLI network and port scanner.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--port-scan',
                       metavar='IPv4',
                       type=str,
                       action='store',
                       nargs='*',
                       help='Perform a port scan on the specified host. Usage: -p <host> [start-port] [end-port]')
    group.add_argument('-n', '--network-scan',
                       metavar='IPv4',
                       type=str,
                       action='store',
                       const='192.168.1.1/24',
                       nargs='?',
                       help='Perform a network scan to discover active hosts. Usage: -n [ip-range]')
    
    args = parser.parse_args()
    
    if args.network_scan:
        if check_sudo():
            ip_range = args.network_scan
            print(ip_range)
            scanner = scanners.NetworkScanner(ip_range)
            scanner.scan()
            scanner.show_hosts()
        else:
            print("Error: you cannot perform this operation unless you are root.")
    elif args.port_scan:
        if len(args.port_scan) > 3:
            parser.error("Too many arguments for port-scan. Maximum allowed: 3.")
        host, *port_range = args.port_scan
        # Check port_range is not empty and check first elemnt of port_range is not empty. If empty set value of 1.
        start_port = int(port_range[0] if port_range and port_range[0] else 1)
        # Check port_range is not empty and check list length bigger then 1 if not set value of 65535 
        end_port = int(port_range[1] if port_range and len(port_range) else 65535)
        scanner = scanners.PortScanner(host, start_port, end_port)
        scanner.scan()
        scanner.show_ports()
if __name__ == '__main__':
    main()