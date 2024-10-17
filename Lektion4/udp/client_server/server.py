import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    print(f'server listening on address: {HOST}:{PORT}')

    while True:
        data, addr = sock.recvfrom(256)
        print(f'received message from {addr}')

        data_decoded = data.decode('utf-8')
        response = f'echo: {data_decoded}'
        sock.sendto(response.encode('utf-8'), addr)
