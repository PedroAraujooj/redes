import socket

HOST = '127.0.0.1'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f'Servidor iniciado em {HOST}:{PORT}')
conn, addr = server.accept()
print(f"conexão estabelecida em {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    message = data.decode()
    print(f"Mensagem recebida: {message}")

    response = f"Boas vindas!"
    conn.sendall(response.encode())
    print(f"Mensagem enviada com sucesso: {response}")

conn.close()
print('Conexão encerrada')

