import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

words = set()

for tag in soup.find_all():
    text = tag.get_text().strip()
    if len(text) > 3:
        words.add(text)

with open("wordlist.txt", "w") as f:
    for word in sorted(words):
        f.write(word + "\n")

print(f"Generated {len(words)} words.")
