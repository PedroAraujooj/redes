import sys
import logging
from scapy.layers.inet import TCP, IP, ICMP
from scapy.sendrecv import sr1, sr

logging.getLogger("scapy-runtime").setLevel(logging.ERROR)


def analyze_port(host, port, verbose_level):
    print(f"[+] Escaneando porta {port}")
    packet = IP(dst=host) / TCP(dport=port, flags="S")
    response = sr1(packet, timeout=0.5, verbose=verbose_level)
    if response is not None and response.haslayer(TCP):
        if response[TCP].flags == 18:
            print("Porta: " + str(port) + " Aberta!")
            sr(IP(dst=target) / TCP(dport=response.sport, flags="R"), timeout=0.5, verbose=0)
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            print("Porta: " + str(port) + " Fechada")
        elif response.haslayer(ICMP):
            if int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print("Porta: " + str(port) + "Filtered")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"Uso: {sys.argv[0]} target, porta de inicio, porta final, verbose level")
        sys.exit(0)
    target = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3]) + 1
    verbose_level = int(sys.argv[4])
    print(f"Escaneando {target} para as portas TCP abertas")
    for port in range(start_port, end_port):
        analyze_port(target, port, verbose_level)
