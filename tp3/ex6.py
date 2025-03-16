import socket

HOST = '127.0.0.1'
PORT = 65432

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

print(f'Conexão estabelecida com o servidor: {HOST}:{PORT}')

message = input(f"Digite uma mensagem para o server: ")
cliente.sendall(message.encode())

response = cliente.recv(1024).decode()
print(f'Resposta do server: {response}')
cliente.close()
