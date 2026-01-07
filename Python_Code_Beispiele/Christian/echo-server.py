#!/usr/bin/env python3
from __future__ import annotations

import argparse
import socket

def run_tcp(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(16)
        print(f"[TCP SERVER] Listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                data = b""
                while b"\n" not in data:
                    chunk = conn.recv(4096)
                    if not chunk:
                        break
                    data += chunk
                line, _, _ = data.partition(b"\n")
                try:
                    n = int(line.decode("utf-8").strip())
                    conn.sendall(f"{n+1}\n".encode("utf-8"))
                except ValueError:
                    conn.sendall(b"ERR\n")


def run_udp(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"[UDP SERVER] Listening on {host}:{port}")

        while True:
            raw, addr = s.recvfrom(4096)
            try:
                n = int(raw.decode("utf-8").strip())
                s.sendto(f"{n+1}\n".encode("utf-8"), addr)
            except ValueError:
                s.sendto(b"ERR\n", addr)


def main() -> None:
    p = argparse.ArgumentParser(description="Ping-Pong Server (TCP/UDP)")
    p.add_argument("--proto", choices=["tcp", "udp"], default="tcp")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=9000)
    args = p.parse_args()

    if args.proto == "tcp":
        run_tcp(args.host, args.port)
    else:
        run_udp(args.host, args.port)


if __name__ == "__main__":
    main()