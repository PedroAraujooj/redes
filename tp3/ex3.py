import socket

if __name__ == '__main__':
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    print("Aguardando pacotes ICMP...")

    while True:
        pacote, endereco = raw_socket.recvfrom(65535)
        print(f"Pacote recebido de {endereco}: {pacote}")