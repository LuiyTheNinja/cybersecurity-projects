from scapy.all import sniff

def analyze(packet):
    print(packet.summary())

print("Starting capture...")
sniff(prn=analyze, count=50)
