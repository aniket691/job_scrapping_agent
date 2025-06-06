from typing import List, Dict
import csv

def print_jobs(jobs: List[Dict]):
    for job in jobs:
        print(job)

def save_jobs_to_csv(jobs, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'company', 'location', 'link', 'post_date'])
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)

def log(message):
    import datetime

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{timestamp} - {message}")