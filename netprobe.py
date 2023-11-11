import argparse
import scanners

def main():
    parser = argparse.ArgumentParser(prog='NetProbe',
                                     description='A CLI network scanner and port scanner.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--port-scan',
                       metavar='IPv4',
                       type=str,
                       action='store',
                       nargs=(0,3),
                       help='Perform a port scan on the specified host. Usage: -p <host> [start-port] [end-port]')
    group.add_argument('-n', '--network-scan',
                       metavar='IPv4',
                       type=str,
                       action='store',
                       help='Perform a network scan to discover active hosts. Usage: -n <ip-range>')
    
    args = parser.parse_args()
    
    if args.network_scan:
        pass
    elif args.port_scan:
        host, *port_range = args.port_scan
        # Check port_range is not empty and check first elemnt of port_range is not empty. If empty set value of 1.
        start_port = int(port_range[0] if port_range and port_range[0] else 1)
        # Check port_range is not empty and check list length bigger then 1 if not set value of 65535 
        end_port = int(port_range[1] if port_range and len(port_range) else 65535)
if __name__ == '__main__':
    main()