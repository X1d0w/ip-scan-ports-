import socket

def scan_ip(ip, ports):
    print(f"Scanning {ip}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
        sock.close()

usage:
target_ip = "192.168.1.1"  # Change this to the IP you want to scan
ports_to_scan = range(1, 1025)  # Common ports

scan_ip(target_ip, ports_to_scan)
