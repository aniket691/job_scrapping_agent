from typing import List, Dict

class JobScraper:
    def __init__(self, url: str):
        self.url = url

    def fetch_page_source(self) -> str:
        raise NotImplementedError("Subclasses must implement fetch_page_source.")

    def parse_jobs(self, page_source: str) -> List[Dict]:
        raise NotImplementedError("Subclasses must implement parse_jobs.")

    def get_jobs(self) -> List[Dict]:
        page_source = self.fetch_page_source()
        return self.parse_jobs(page_source)