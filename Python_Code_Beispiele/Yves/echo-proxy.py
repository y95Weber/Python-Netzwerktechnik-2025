import socket

# Adresse des Proxy mit variablem Port(Der Client sendet dort hin)
PROXY_HOST = "0.0.0.0"
# Variabler Port aber default 50000
proxy_port_input = input("Proxy listen Port (default 50000): \n").strip()
PROXY_PORT = int(proxy_port_input) if proxy_port_input else 50000


# Eingeben Der Server Adresse
server_input = input("Server IP (default localhost): ").strip()
if server_input == "" or server_input.lower() == "localhost":
    SERVER_HOST = "127.0.0.1"
else:
    SERVER_HOST = server_input

server_port_input = input("Server Port (default 65432): ").strip()
SERVER_PORT = int(server_port_input) if server_port_input else 65432


print(f"Proxy listening on {PROXY_PORT}")

# Socket erstellen für Proxy
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy:
    proxy.bind((PROXY_HOST,PROXY_PORT))

    # Persistentes Socket für Server erstellen (Quellport bleibt gleich)
    server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_sock.settimeout(5)

    # Pakete senden und Empfangen
    while True:
        # Paket von Client empfangen
        data, client_addr = proxy.recvfrom(1024)
        print(f"[Proxy] From client {client_addr}: {data.decode()}")

        # Paket an Server weiterleiten
        server_sock.sendto(data, (SERVER_HOST, SERVER_PORT))

        # Antwort vom Server empfangen --> Mit Timeout
        try:
            response, _ = server_sock.recvfrom(1024)
        except socket.timeout:
            print("[Proxy] Timeout - no response from server")

        print(f"[Proxy] From Server: {response.decode()}")

        # Antwort zurück an den Client
        proxy.sendto(response, client_addr)
        print(f"[Proxy] Sent back to client\n")