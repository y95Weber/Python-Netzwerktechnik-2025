#!/usr/bin/env python3
from __future__ import annotations

import argparse
import socket
import sys


def ping_tcp(host: str, port: int, n: int, timeout: float) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((host, port))  # -> ConnectionRefusedError wenn Server nicht läuft
        s.sendall(f"{n}\n".encode("utf-8"))

        data = b""
        while b"\n" not in data:
            chunk = s.recv(4096)
            if not chunk:
                raise RuntimeError("Server closed connection without response")
            data += chunk

        line, _, _ = data.partition(b"\n")
        txt = line.decode("utf-8").strip()
        if txt == "ERR":
            raise ValueError("Server returned ERR")
        return int(txt)


def ping_udp(host: str, port: int, n: int, timeout: float) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(timeout)
        s.sendto(f"{n}\n".encode("utf-8"), (host, port))

        raw, _ = s.recvfrom(4096)  # -> socket.timeout wenn Server nicht antwortet
        txt = raw.decode("utf-8").strip()
        if txt == "ERR":
            raise ValueError("Server returned ERR")
        return int(txt)


def main() -> None:
    p = argparse.ArgumentParser(description="Ping-Pong Client (TCP/UDP)")
    p.add_argument("--proto", choices=["tcp", "udp"], default="tcp")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=9000)
    p.add_argument("--timeout", type=float, default=2.0)
    p.add_argument("spin", nargs="?", type=int, help="Ping spin (n)")
    args = p.parse_args()

    spin = args.spin
    while spin is None:
        try:
            spin = int(input("Bitte spin (Ganzzahl) eingeben: ").strip())
        except ValueError:
            print("Ungültig. Bitte eine Ganzzahl eingeben (z.B. 5).")

    try:
        if args.proto == "tcp":
            out = ping_tcp(args.host, args.port, spin, args.timeout)
        else:
            out = ping_udp(args.host, args.port, spin, args.timeout)
    except ConnectionRefusedError:
        print(f"FEHLER: TCP Server nicht erreichbar auf {args.host}:{args.port} (Connection refused).", file=sys.stderr)
        sys.exit(2)
    except socket.timeout:
        print(f"FEHLER: Keine UDP Antwort innerhalb von {args.timeout}s von {args.host}:{args.port}.", file=sys.stderr)
        sys.exit(3)
    except OSError as e:
        print(f"FEHLER: Netzwerkfehler: {e}", file=sys.stderr)
        sys.exit(4)

    print(out)


if __name__ == "__main__":
    main()