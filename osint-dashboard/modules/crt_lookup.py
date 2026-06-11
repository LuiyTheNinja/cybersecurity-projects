import requests

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        subdomains = set()
        for entry in data:
            subdomains.add(entry["name_value"])

        return list(subdomains)

    except Exception:
        return []
``
