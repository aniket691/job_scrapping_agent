from flask import Flask, jsonify
from job_crawler import JobCrawler
from naukri_parser import NaukriParser
from converter import normalize_jobs

app = Flask(__name__)

@app.route("/run-scraper", methods=["GET"])
def run_scraper():
    start_urls = [
        "https://www.naukri.com/python-developer-jobs-in-mumbai"
    ]
    parser = NaukriParser()
    crawler = JobCrawler(start_urls, parser, max_jobs=50, delay=2)
    jobs = crawler.run()
    normalized_jobs = normalize_jobs(jobs, source="naukri")
    return jsonify(normalized_jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)