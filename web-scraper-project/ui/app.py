from flask import Flask, request, jsonify

import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return '''
        <h2>Web Scraper</h2>
        <form action="/scrape" method="post">
            <textarea name="urls" rows="10" cols="50" placeholder="Wklej URL-e oddzielone nową linią"></textarea><br>
            <button type="submit">Start Scraping</button>
        </form>
    '''

@app.route("/scrape", methods=["POST"])
def scrape():
    if request.form.get("urls"):
        urls = request.form["urls"].splitlines()
    else:
        urls = request.json.get("urls", [])

    try:
        response = requests.post("http://engine:5001/run", json={"urls": urls})
        return jsonify(response.json())
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Nie można połączyć się z silnikiem scraper"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
