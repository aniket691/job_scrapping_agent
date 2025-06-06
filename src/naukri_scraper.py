import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import List, Dict
from scraper_base import JobScraper

class NaukriScraper(JobScraper):
    def fetch_page_source(self) -> str:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self.url)
        time.sleep(3)
        page_source = driver.page_source
        driver.quit()
        return page_source

    def parse_jobs(self, page_source: str) -> List[Dict]:
        soup = BeautifulSoup(page_source, 'html.parser')
        # Try multiple selectors for robustness
        job_cards = soup.find_all('div', class_='cust-job-tuple')
        if not job_cards:
            job_cards = soup.find_all('div', class_='srp-jobtuple-wrapper')
        if not job_cards:
            job_cards = soup.find_all('div', attrs={'data-job-id': True})

        jobs = []
        for job_card in job_cards:
            if not isinstance(job_card, Tag):
                continue
            # Title and link
            title_elem = job_card.find('a', class_='title')
            title = title_elem.text.strip() if title_elem else ''
            link = str(title_elem['href']).strip() if isinstance(title_elem, Tag) and title_elem.has_attr('href') else ''
            # Company
            company_elem = job_card.find('a', class_='comp-name')
            company = company_elem.text.strip() if company_elem else ''
            # Location
            location_elem = job_card.find('span', class_='locWdth')
            location = location_elem.text.strip() if location_elem else ''
            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'link': link
            })
        return jobs