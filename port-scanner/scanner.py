import socket
import json
from config import TARGET, PORT_RANGE, TIMEOUT
from banner import print_banner

open_ports = []

# Load CVE database
with open("cve_db.json", "r") as f:
    cve_db = json.load(f)

# Simple service mapping
COMMON_PORTS = {
    21: "ftp",
    22: "ssh",
    23: "telnet",
    80: "http",
    443: "http",
    3389: "rdp"
}

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)

    try:
        sock.connect((TARGET, port))
        return True
    except:
        return False
    finally:
        sock.close()

def identify_service(port):
    return COMMON_PORTS.get(port, "unknown")

def check_cve(service):
    return cve_db.get(service, None)

def print_result(port, service, cve):
    print(f"[+] Port {port} OPEN ({service})")

    if cve:
        severity = cve['severity']
        print(f"    ⚠ CVE Found: {cve['cve']}")
        print(f"    Severity: {severity}")
        print(f"    Desc: {cve['description']}")

        if severity == "Critical":
            print("    🚨 CRITICAL RISK 🚨")
        elif severity == "High":
            print("    🔥 HIGH RISK")
        elif severity == "Medium":
            print("    ⚠ MEDIUM RISK")
        else:
            print("    Low risk")

def main():
    print_banner()
    print(f"Scanning target: {TARGET}\n")

    for port in range(PORT_RANGE[0], PORT_RANGE[1]):
        if scan_port(port):
            service = identify_service(port)
            cve = check_cve(service)

            print_result(port, service, cve)

if __name__ == "__main__":
    main()
