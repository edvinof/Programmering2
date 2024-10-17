import socket
import random
import time

BROADCAST_IP = '255.255.255.255'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        random_data = random.randint(1,23000)
        message_to_broadcast = f'random data: {random_data}'.encode('utf-8')

        sock.sendto(message_to_broadcast, (BROADCAST_IP, PORT))

        time.sleep(1)

