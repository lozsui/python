import socket

import typer

app = typer.Typer()


def is_port_open(host, port, timeout=3):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        return result == 0  # 0 bedeutet: Verbindung erfolgreich


@app.command()
def check_for_open_port(host: str, port: int):
    if is_port_open(host, port):
        print(f"Port {port} auf {host} ist offen.")
    else:
        print(f"Port {port} auf {host} ist geschlossen oder blockiert.")


if __name__ == "__main__":
    app()
