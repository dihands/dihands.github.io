from scapy.all import *
import argparse

def packet_handler(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet.info.decode()
        bssid = packet.addr2
        channel = int(ord(packet[Dot11Elt:3].info))
        print(f"SSID: {ssid}, BSSID: {bssid}, Channel: {channel}")

def start_scanning(interface):
    print(f"Scanning for Wi-Fi networks on interface {interface}...")
    sniff(iface=interface, prn=packet_handler, timeout=60)

def main():
    parser = argparse.ArgumentParser(description="Simple Wi-Fi scanner in Python.")
    parser.add_argument("interface", help="The wireless network interface to scan on (e.g., wlan0).")
    args = parser.parse_args()

    start_scanning(args.interface)

if __name__ == "__main__":
    main()
