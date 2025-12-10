import socket # Importiert das Modul, um Sockets für Netzwerkkommunikation zu verwenden

# Hostadresse und Portnummer angeben
HOST = input("IP des Servers angeben: ")
PORT = int(input("Portnummer angeben "))
anzahl = int(input("Wie viele nachrichten sollen gesendet werden? "))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

    zahl_client = 1

    for i in range (anzahl):

        # Aktueller Werd senden
        client_message = str(zahl_client).encode()
        sock.sendto(client_message, (HOST, PORT))

        # Antwort empfangen
        data, addr = sock.recvfrom(1024)
        server_wert = int(data.decode())

        print(f"Server antwortet: {server_wert}")

        zahl_client = server_wert + 1
