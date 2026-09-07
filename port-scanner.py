import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP or hostname: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname or IP address")
    exit()

print(f"\nScanning {target} ({target_ip})...\n")


def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "Unknown"

        print(f"Port {port:<5} OPEN    Service: {service}")

    sock.close()


# Scan ports 1–1024
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1025))

print("\nScan completed.")
