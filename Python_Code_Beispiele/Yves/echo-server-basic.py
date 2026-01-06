import socket
from http.client import responses

HOST = "0.0.0.0" # Bindet an alle Netzwerkschnittstellen
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    print(f"UDP server listening on {PORT}")

    while True:
        data, addr = sock.recvfrom(1024)
        message = int(data.decode())
        print(f"Received from Client {addr}: {message}")

        response = str(message + 1).encode()
        sock.sendto(response, addr)