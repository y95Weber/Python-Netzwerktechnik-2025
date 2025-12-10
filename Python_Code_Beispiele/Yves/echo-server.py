import socket

HOST = "0.0.0.0" # Bindet an alle Netzwerkschnittstellen
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    print(f"UDP server listening on {PORT}")

    while True:
        data, addr = sock.recvfrom(1024)
        client_message = int(data.decode())
        print(f"Received from {addr}: {client_message}")

        # Nachricht von Client n + 1 setzen
        server_response = str(client_message + 1).encode()

        # Nachricht an Client senden
        sock.sendto(server_response, addr)
