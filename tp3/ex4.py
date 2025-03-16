import socket


def verifica_porta(host, start_port, end_port):
    portas_abertas = []

    for port in range(start_port, end_port + 1):
        print(f'Verificando porta {port}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Porta {port} está aberta.")
            portas_abertas.append(port)

        sock.close()

    return portas_abertas


if __name__ == "__main__":
    host = "localhost"

    portas_abertas = verifica_porta(host, 1, 65535)

    if portas_abertas:
        print("Portas abertas encontradas:", portas_abertas)
    else:
        print("Nenhuma porta aberta encontrada.")
