import socket # Importiert das Modul, um Sockets für Netzwerkkommunikation zu verwenden

# Hostadresse und Portnummer angeben
HOST = input("IP from Server or Proxy: ")
PORT = int(input("Port of Server or Proxy: "))
message = 1
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.settimeout(5) # Max. Wartezeit auf Antwort vom Server

    # Nachricht Senden
    while True:
        # Nachricht an den Server senden
        sock.sendto(str(message).encode(), (HOST, PORT)) # Sendet Nachricht an angegebene IP und Port
        message_test = message + 1

        # Antwort vom Server empfangen und testen ob timeout ok
        try:
            data, addr = sock.recvfrom(1024) # Wartet auf Antwort vom Server
        except socket.timeout:
            print("Timeout - no answer from Server")
            break

        # Speichert Antwort von Server und testet ob richtiger Wert
        try:
            received = int(data.decode())
        except ValueError:
            print(f"Wrong Datatype: {data}")
            break

        print(f"Send: {message}, Received from Server: {received}")

        # Fehlerprüfung (Ping-Pong-Protokoll)
        if  received != message_test:
            print("UDP receive is wrong!!!")
            break

        # UDP Ping Pong wiederholen ?
        again = input("Continue? (j/n): ").strip().lower()
        if again != "j":
            print("Ping Pong finished!")
            break
        # Nächste Zahl vorbereiten
        else:
            message = received + 1
