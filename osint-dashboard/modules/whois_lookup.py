import subprocess

def get_whois(domain):
    try:
        result = subprocess.check_output(["whois", domain]).decode()
        return result
    except:
        return "WHOIS lookup failed"
``
