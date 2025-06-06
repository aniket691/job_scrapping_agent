import json
from job_crawler import JobCrawler
from naukri_parser import NaukriParser
from utils import save_jobs_to_csv
from converter import normalize_jobs

if __name__ == "__main__":
    start_urls = [
        "https://www.naukri.com/python-developer-jobs-in-mumbai"
    ]
    parser = NaukriParser()
    crawler = JobCrawler(start_urls, parser, max_jobs=50, delay=2)
    jobs = crawler.run()
    print(f"Scraped {len(jobs)} unique jobs.")
    save_jobs_to_csv(jobs, "naukri_jobs.csv")
    print("Saved to naukri_jobs.csv")

    # Normalize and save as JSON
    normalized_jobs = normalize_jobs(jobs, source="naukri")
    with open("naukri_jobs.json", "w", encoding="utf-8") as f:
        json.dump(normalized_jobs, f, ensure_ascii=False, indent=2)
    print("Saved to naukri_jobs.json")