import socket

HOST=''
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REU, 1)
    sock.bind((HOST, PORT))
    print(f'listening to broadcast on port {PORT}')

    while True:
        data, addr = sock.recvfrom(1024)
        print(f'received data from broadcast on address: {addr}: {data.decode("utf-8")}')