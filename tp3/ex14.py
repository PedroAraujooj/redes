import ssl
import socket

HOST = 'www.google.com'

context = ssl.create_default_context()

with socket.create_connection((HOST, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as secure_socket:
        print(secure_socket.cipher())