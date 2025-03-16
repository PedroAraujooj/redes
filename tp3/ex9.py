import socket

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
    print(f'Servidor iniciado em {HOST}:{PORT}')
    conn, addr = server.accept()
    print(f"conexão estabelecida em {addr}")
    data = conn.recv(1024)
    if not data:
        break
    message = data.decode("utf-8")
    print(f"Mensagem recebida: {message}")
    response = (f"HTTP/1.1 200 OK\r\n\r\n <html><body><h1>"
                f"Bem vindo!</h1></body></html> \r\n")
    conn.sendall(response.encode())
    print(f'Mensagem enviada com sucesso: "{response}"')
    conn.close()

print('Conexão encerrada')

