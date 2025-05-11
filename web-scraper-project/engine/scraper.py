from multiprocessing import Pool
import asyncio
from flask import Flask, request, jsonify, render_template
from worker import async_scrape_urls

app = Flask(__name__)

def run_async_scrape(urls_chunk):
    asyncio.run(async_scrape_urls(urls_chunk))

def start_scraping(urls):
    chunk_size = len(urls) // 4 or 1
    url_chunks = [urls[i:i + chunk_size] for i in range(0, len(urls), chunk_size)]

    with Pool(processes=4) as pool:
        pool.map(run_async_scrape, url_chunks)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_scraper():
    try:
        data = request.get_json()
        urls = data.get("urls", [])
        if not urls:
            return jsonify({"status": "error", "message": "Brak URL-i w żądaniu"}), 400

        start_scraping(urls)
        return jsonify({"status": "ok", "message": "Scraping started"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
