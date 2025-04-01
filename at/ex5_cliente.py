import socket

HOST = '127.0.0.1'
PORT = 8080

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

print(f'Conexão estabelecida com o servidor: {HOST}:{PORT}')

message = f"GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
cliente.sendall(message.encode())

response = cliente.recv(4096).decode()
print(f'Resposta do server: "{response}"')
cliente.close()
