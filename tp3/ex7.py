import socket

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f'Servidor ouvindo  em {HOST}:{PORT}')

while True:
    data,addr = server.recvfrom(1024)
    print(f"Recebido de {addr}: {data.decode()}")

    mensagem_ack = "ack"
    server.sendto(mensagem_ack.encode(), addr)
