import socket

PROXY_HOST = "127.0.0.1"
PROXY_PORT = 5001

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000


def run_proxy():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((PROXY_HOST, PROXY_PORT))
        print(f"UDP-Proxy läuft auf {PROXY_HOST}:{PROXY_PORT} -> Server {SERVER_HOST}:{SERVER_PORT}")

        while True:
            data, client_addr = s.recvfrom(1024)
            print(f"Proxy: von {client_addr} -> Server ({SERVER_HOST}:{SERVER_PORT}) : {data.decode().strip()}")

            s.sendto(data, (SERVER_HOST, SERVER_PORT))

            server_data, _ = s.recvfrom(1024)
            print(f"Proxy: von Server -> {client_addr} : {server_data.decode().strip()}")

            s.sendto(server_data, client_addr)


if __name__ == "__main__":
    run_proxy()
