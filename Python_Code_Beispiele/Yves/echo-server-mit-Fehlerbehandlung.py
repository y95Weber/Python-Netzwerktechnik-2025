import socket

HOST = "0.0.0.0" # Bindet an alle Netzwerkschnittstellen
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    sock.settimeout(50)
    print(f"UDP server listening on {PORT}")

    last_message = None

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

        print(f"Received from Client {addr}: {message}")

        # Fehlerprüfung: kommt die erwartete nächste Zahl?
        if last_message is not None and message != last_message + 1:
            print("UDP receive is wrong on SERVER!!!")

        last_message = message

        # Antwort zurück
        response = str(message + 1).encode()
        sock.sendto(response, addr)
