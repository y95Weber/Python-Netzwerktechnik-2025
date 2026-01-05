import socket # Importiert das Modul, um Sockets für Netzwerkkommunikation zu verwenden

# Hostadresse und Portnummer angeben
HOST = input("IP des Servers angeben: ")
PORT = int(input("Portnummer angeben "))
message = 1
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True:
        # Nachricht an den Server senden
        sock.sendto(str(message).encode(), (HOST, PORT)) # Sendet Nachricht an angegebene IP und Port

        # Antwort vom Server empfangen und Ausgeben
        data, addr = sock.recvfrom(1024) # Wartet auf Antwort vom Server
        print(f"Send: {message}, Received: {data.decode()}")
        message = int(data.decode())

        # UDP Ping Pong wiederholen ?
        again = input("Continue? (j/n): ").strip().lower()
        if again != "j":
            print("Ping Pong finished!")
            break
        # Nächste Zahl vorbereiten
        else:
            message += 1
