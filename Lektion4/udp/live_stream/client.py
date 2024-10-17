import socket

HOST = '127.0.0.1'
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_sock:
    client_sock.sendto('hej'.encode('utf-8'), (HOST, PORT))

    while True:
        data, server = client_sock.recvfrom(1024)
        print(data.decode('utf-8'))