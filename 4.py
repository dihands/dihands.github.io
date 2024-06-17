import scapy.all as scapy
import socket
import argparse

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        print(f"Port {port} on {target} is open.")
        sock.close()
    except socket.error:
        pass

def scan_target(target):
    print(f"Scanning target: {target}")
    for port in range(1, 100):
        scan_port(target, port)

def main():
    parser = argparse.ArgumentParser(description="Simple network scanner in Python.")
    parser.add_argument("target", help="Target IP address or hostname to scan.")
    args = parser.parse_args()

    scan_target(args.target)

if __name__ == "__main__":
    main()
