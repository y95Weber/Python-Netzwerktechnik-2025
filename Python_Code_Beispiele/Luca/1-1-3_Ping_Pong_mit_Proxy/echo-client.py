import socket

HOST = "127.0.0.1"
PORT = 5001            # Proxy-Port
TIMEOUT_SECONDS = 2.0  # UDP kann verloren gehen


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.settimeout(TIMEOUT_SECONDS)
        print(f"UDP-Client gestartet. Ziel ist {HOST}:{PORT}")
        print("Gib eine Zahl ein, 'quit' beendet das Programm.\n")

        while True:
            user_input = input("Ping > ")

            if user_input.lower() == "quit":
                print("Beende UDP-Client.")
                break

            client_socket.sendto((user_input + "\n").encode(), (HOST, PORT))

            try:
                data, _ = client_socket.recvfrom(1024)
                print("Pong <", data.decode().strip())
            except socket.timeout:
                print(f"Keine Antwort innerhalb von {TIMEOUT_SECONDS} Sekunden (Timeout).\n")


if __name__ == "__main__":
    run_client()
