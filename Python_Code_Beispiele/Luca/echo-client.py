# ping_udp.py – UDP-Ping-Client mit einfacher Fehlerbehandlung
import socket

HOST = "127.0.0.1"  # Ziel (muss zum Server passen)
PORT = 5000         # muss zum Server passen
TIMEOUT_SECONDS = 2.0  # Wartezeit auf Antwort (UDP kann verloren gehen)


def run_ping_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.settimeout(TIMEOUT_SECONDS)
        print(f"UDP-Ping-Client gestartet. Ziel ist {HOST}:{PORT}")
        print("Gib eine Zahl ein, 'quit' beendet das Programm.\n")

        while True:
            user_input = input("Ping > ")

            if user_input.lower() == "quit":
                print("Beende UDP-Ping-Client.")
                break

            # Zahl an Server schicken
            client_socket.sendto((user_input + "\n").encode(), (HOST, PORT))

            try:
                data, addr = client_socket.recvfrom(1024)
                print("Pong <", data.decode().strip())
            except socket.timeout:
                print(f"Keine Antwort innerhalb von {TIMEOUT_SECONDS} Sekunden (Timeout).")
                print("UDP kann Pakete verlieren – du kannst es einfach nochmals probieren.\n")


if __name__ == "__main__":
    run_ping_udp()
