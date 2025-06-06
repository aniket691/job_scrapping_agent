import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class JobCrawler:
    def __init__(self, start_urls, parser, max_jobs=100, delay=2):
        self.queue = deque(start_urls)
        self.visited = set()
        self.jobs = []
        self.parser = parser
        self.max_jobs = max_jobs
        self.delay = delay

    def fetch_page(self, url):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        time.sleep(3)  # Wait for JS to load
        html = driver.page_source
        driver.quit()
        return html

    def should_visit(self, url):
        # Only visit URLs from the same domain and not visited before
        parsed = urlparse(url)
        return url not in self.visited and parsed.netloc.endswith("naukri.com")

    def run(self):
        while self.queue and len(self.jobs) < self.max_jobs:
            url = self.queue.popleft()
            if not self.should_visit(url):
                continue
            print(f"Crawling: {url}")
            self.visited.add(url)
            html = self.fetch_page(url)
            if not html:
                continue
            jobs, links = self.parser.parse_job_listings(html, url)
            for job in jobs:
                if job['link'] not in {j['link'] for j in self.jobs}:
                    self.jobs.append(job)
            for link in links:
                abs_link = urljoin(url, link)
                if self.should_visit(abs_link):
                    self.queue.append(abs_link)
            time.sleep(self.delay)
        return self.jobs