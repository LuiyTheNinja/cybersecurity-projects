from flask import Flask, render_template, request
import sqlite3

from modules.crt_lookup import get_subdomains
from modules.whois_lookup import get_whois

app = Flask(__name__)

def save_to_db(domain, subdomains):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT,
            subdomain TEXT
        )
    """)

    for sub in subdomains:
        cursor.execute("INSERT INTO results (domain, subdomain) VALUES (?, ?)", (domain, sub))

    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    data = None

    if request.method == "POST":
        domain = request.form.get("domain")

        subdomains = get_subdomains(domain)
        whois_data = get_whois(domain)

        save_to_db(domain, subdomains)

        data = {
            "domain": domain,
            "subdomains": subdomains,
            "whois": whois_data
        }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
