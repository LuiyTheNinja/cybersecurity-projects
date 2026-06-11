from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    return requests.get(url).json()

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        domain = request.form["domain"]
        results = get_subdomains(domain)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
