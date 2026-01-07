import socket # Importiert das Modul, um Sockets für Netzwerkkommunikation zu verwenden

# Hostadresse und Portnummer angeben
HOST = input("IP des Servers angeben: ")
PORT = int(input("Portnummer angeben "))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Nachricht an den Server senden
    message = b"Ping" # Nachricht als Bytes senden
    sock.sendto(message, (HOST, PORT)) # Sendet Nachricht an angegebene IP und Port

    # Antwort vom Server empfangen und Ausgeben
    data, addr = sock.recvfrom(1024) # Wartet auf Antwort vom Server
    print(f"Received from {addr}: {data.decode()}")