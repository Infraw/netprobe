import scapy.all as scapy

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
            
    def print_result(self):
        print("Index\tIP Address\t\tMAC Address")
        print("-----------------------------------------")
        for client in self.clients:
            print(f"{client['index']}\t{client['ip']}\t\t{client['mac']}")