import socket
import time

HOST = '127.0.0.1'
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as stream_sock:
    stream_sock.bind((HOST, PORT))
    clients = list()
    counter = 0
    while True:
        counter += 1
        message = f'streaming data count: {counter}'

        for client in clients:
            stream_sock.sendto(message.encode('utf-8'), client)

        time.sleep(0.5)
        try:
            stream_sock.settimeout(0.1)
            data, addr = stream_sock.recvfrom(1024)
            clients.append(addr)
        except socket.timeout:
            continue

