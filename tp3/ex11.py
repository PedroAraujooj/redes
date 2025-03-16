import socket
import struct

HOST = '127.0.0.1'
PORT = 9999


def receive_file_size(sock: socket.socket):
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()

    while received_bytes < expected_bytes:
        chunk = sock.recv(expected_bytes - received_bytes)
        stream += chunk
        received_bytes += len(chunk)

    filesize = struct.unpack(fmt, stream)[0]
    return filesize

def receive_file(sock: socket.socket, file_name):
    file_size = receive_file_size(sock)
    with open(file_name, "wb") as f:
        received_bytes = 0
        while received_bytes < file_size:
            chunk = sock.recv(1024)
            if chunk:
                f.write(chunk)
                received_bytes += len(chunk)

with socket.create_server((HOST, PORT)) as server:
    print(f'Conectando com {HOST}:{PORT}...')
    conn, addr = server.accept()
    print(f'Conectado com {addr[0]}:{addr[1]}')
    print("Recebendo arquivo...")
    receive_file(conn, "file_received.py")
    print("Arquivo recebido")
