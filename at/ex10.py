from scapy.all import sniff, TCP


def detect_tcp_packet(packet):
    if TCP in packet:
        print(f"[*] Pacote detectado entre a origem <{packet[0][1].src}> e destino <{packet[0][1].dst}>")


if __name__ == "__main__":
    print("Iniciando captura de pacotes. Pressione Ctrl+C para encerrar.\n")
    sniff(prn=detect_tcp_packet, store=False)
