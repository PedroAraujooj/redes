import scapy.all as scapy
from scapy.all import ARP, srp, Ether, conf


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_mac_adress(ip_address):
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request = ARP(pdst=ip_address)
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)
    return answered_list[0][0][1].hwsrc


def process_sniffed_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        ip_address = packet[ARP].psrc
        original_mac = get_mac_adress(ip_address)
        response_mac = packet[ARP].hwsrc
        if original_mac != response_mac:
            print(
                f"Alerta: Possível ARP Spoofing detectado para IP {ip_address}! MAC anterior: {original_mac}, MAC atual: {response_mac}")


if __name__ == '__main__':
    sniff(conf.iface)
