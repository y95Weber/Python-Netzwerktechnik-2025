import socket

HOST = "0.0.0.0" # Bindet an alle Netzwerkschnittstellen
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    print(f"UDP server listening on {PORT}")

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")

        if data.decode() == "Ping":
            response = b"Pong"
        else:
            response = b"Unknown"

        sock.sendto(response, addr)