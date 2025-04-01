from scapy.all import (
    sniff,
    sendp,
    Ether,
    IP
)

NETWORK_INTERFACE = "Wi-Fi"
CAPTURE_FILTER = "ip"


def analisa_pacote(pkt):
    ether_layer = pkt.getlayer(Ether)
    if ether_layer:
        print(f"Ethernet >> src={ether_layer.src}, dst={ether_layer.dst}, type={hex(ether_layer.type)}")
    ip_layer = pkt.getlayer(IP)
    if ip_layer:
        print(f"IP >> src={ip_layer.src}, dst={ip_layer.dst}, ttl={ip_layer.ttl}")
    print("---")


def modifica_pacote(pkt):
    if IP in pkt:
        pkt[IP].ttl = int(int(pkt[IP].ttl)/2)
    return pkt


def handle_pacote(pkt):
    print("=== PACOTE CAPTURADO ===")
    analisa_pacote(pkt)
    modified_pkt = pkt.copy()
    modified_pkt = modifica_pacote(modified_pkt)
    print("=== PACOTE MODIFICADO ===")
    analisa_pacote(modified_pkt)
    try:
        sendp(modified_pkt, iface=NETWORK_INTERFACE, verbose=False)
        print(">>> Pacote injetado com sucesso!\n")
    except Exception as e:
        print(f"!!! Erro ao injetar pacote: {e}\n")


if __name__ == "__main__":
    print(f"Sniffando na interface: {NETWORK_INTERFACE}")
    print(f"Filtro de captura: {CAPTURE_FILTER}")
    print("Pressione Ctrl+C para encerrar.\n")
    sniff(iface=NETWORK_INTERFACE, filter=CAPTURE_FILTER, prn=handle_pacote, store=False)
