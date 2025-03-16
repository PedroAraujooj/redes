import socket
import ssl

HOST = '127.0.0.1'
PORT = 8080

context = ssl.create_default_context()

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as secure_sock:
        data = bytearray()

        try:
            secure_sock.connect((HOST, PORT))
            print(f'Conexão estabelecida com o servidor: {HOST}:{PORT}')
            print(secure_sock.cipher())
            secure_sock.write(b"GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n")
            data = secure_sock.read()
            print(data.decode())
        except Exception as e:
            print(e)

