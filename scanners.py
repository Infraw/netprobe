import scapy.all as scapy
import socket

class NetworkScanner:
    def __init__(self, target_ip = "192.168.1.1/24"):
        self.target_ip = target_ip
        self.clients = []
    
    def scan(self):
        try:
            arp_request = scapy.ARP(pdst=self.target_ip)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_broadcast = broadcast/arp_request
            #Send ARP request and get response
            answered = scapy.srp(arp_broadcast, timeout=2, verbose=False)[0]
            for idx, e in enumerate(answered):
                #Store IP and MAC addr
                client = {"index": idx, "ip": e[1].psrc, "mac": e[1].hwsrc}
                self.clients.append(client)
        except Exception as e:
            print(f"Error during scannig: {e}")
            
    def show_hosts(self):
        print("Index\tIP Address\t\tMAC Address")
        print("-----------------------------------------")
        for client in self.clients:
            print(f"{client['index']}\t{client['ip']}\t\t{client['mac']}")

class PortScanner:
    def __init__(self, host, start_port, end_port):
        self.host = host
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []
    
    def scan(self):
        for port in range(self.start_port, self.end_port+1):
            try:
                # AF_INET stands for Adress Family (AF) Ipv4 and SOCK_STREAM is used for TCP sockets for specify socket type.
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                # connect_ex method takes on arg tuple and returns 0 if connection successfull
                result = sock.connect_ex((self.host, port))
                if result == 0:
                    self.open_ports.append(port)
                    print(f"Port {port} is open.")
            except socket.timeout:
                print(f"Port {port} is timed out.")
            except socket.error:
                print(f"Host is not reachable. Exiting...")
                exit()
    
    def show_ports(self):
            print("-----------------------------------------")
            print(f"Open ports: {self.open_ports}")