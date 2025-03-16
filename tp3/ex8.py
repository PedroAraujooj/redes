import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input(f"Digite uma mensagem para o server: ")

client.sendto(message.encode(), (HOST, PORT))
print(f"Mensagem enviada para {HOST}:{PORT}")

data, server_addr = client.recvfrom(1024)
print(f"Resposta do servidor ({server_addr}): {data.decode()}")

client.close()
