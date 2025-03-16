import socket
import os
import struct

HOST = '127.0.0.1'
PORT = 9999


def send_file(sock: socket.socket, file):
    file_size = os.path.getsize(file)
    sock.sendall(struct.pack('<Q', file_size))
    with open(file, 'rb') as f:
        while read_bytes := f.read(1024):
            sock.sendall(read_bytes)


with socket.create_connection((HOST, PORT)) as conn:
    print('Connecting...')
    print('Enviando arquivo...')
    send_file(conn, "ex12.py")
    print('Arquivo enviado')
