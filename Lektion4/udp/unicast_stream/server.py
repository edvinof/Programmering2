import socket
import time

HOST = '127.0.0.1'
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as stream_sock:
    stream_sock.bind((HOST, PORT))

    while True:

        data, addr = stream_sock.recvfrom(1024)

        for i in range(10):
            stream_sock.sendto(f'Meddelande nummer {i+1} till {addr}'.encode('utf-8'), addr)
            time.sleep(0.5)