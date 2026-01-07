import socket

HOST = "127.0.0.1"
PORT = 5000


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f"UDP-Server läuft auf {HOST}:{PORT} (Strg+C zum Stoppen).")

        while True:
            data, addr = server_socket.recvfrom(1024)
            text = data.decode().strip()
            print(f"Von {addr} empfangen: {text}")

            try:
                n = int(text)
                response = str(n + 1) + "\n"
            except ValueError:
                response = "error: please send an integer\n"

            print(f"Antworte an {addr} mit: {response.strip()}")
            server_socket.sendto(response.encode(), addr)


if __name__ == "__main__":
    run_server()
