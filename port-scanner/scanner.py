import socket
import threading

target = "127.0.0.1"
open_ports = []

def scan_port(port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))
        open_ports.append(port)
        print(f"[+] Port {port} OPEN")
    except:
        pass
    finally:
        sock.close()

threads = []

for port in range(20, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScan Complete")
print("Open Ports:", open_ports)
