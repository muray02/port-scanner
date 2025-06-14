import socket

def scan(host, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect.ex((host, port))
        if result == 0:
            print(f"[+] Порт {port} открыт")
        sock.close()

