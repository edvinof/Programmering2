import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_sock:
    message = 'hello from devops24 via udp'
    encoded_message = message.encode('utf-8')

    client_sock.sendto(encoded_message, (HOST, PORT))
    response, server = client_sock.recvfrom(256)
    decoded_response = response.decode('utf-8')
    print(f'received from server: {decoded_response}')