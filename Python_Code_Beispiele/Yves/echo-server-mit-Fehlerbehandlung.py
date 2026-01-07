import socket

# Adresse vom Server mit variablem Port (Client oder Proxy senden dort hin)
HOST = "0.0.0.0" # Bindet an alle Netzwerkschnittstellen
# Variabler Port aber default 65432
port_input = input("Server listen Port (default 65432): ").strip()
PORT = int(port_input) if port_input else 65432

last_message = 0

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    sock.settimeout(5)
    print(f"UDP server listening on {PORT}")

    while True:
        try:
            data, addr = sock.recvfrom(1024)
        except socket.timeout:
            print("Timeout - no package received!")
            continue

        try:
            message = int(data.decode())
        except ValueError:
            print(f"Ungültige Daten von {addr}: {data}")
            continue

        print(f"Received from Client {addr}: {message}\n")

        # Fehlerprüfung: kommt die erwartete nächste Zahl?
        if message != last_message + 1:
            print("UDP receive is wrong on SERVER!!!")
        last_message += 2
        # Antwort zurück
        response = str(message + 1).encode()
        sock.sendto(response, addr)
