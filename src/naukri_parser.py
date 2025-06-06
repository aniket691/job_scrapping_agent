from bs4 import BeautifulSoup
from bs4.element import Tag

class NaukriParser:
    def parse_job_listings(self, html, base_url):
        soup = BeautifulSoup(html, 'html.parser')
        # Try multiple selectors
        job_cards = soup.find_all('div', class_='cust-job-tuple')
        if not job_cards:
            job_cards = soup.find_all('div', class_='srp-jobtuple-wrapper')
        if not job_cards:
            job_cards = soup.find_all('div', attrs={'data-job-id': True})

        print(f"Found {len(job_cards)} job cards")  # Debug print

        jobs = []
        links = set()
        for card in job_cards:
            if not isinstance(card, Tag):
                continue
            title_elem = card.find('a', class_='title')
            company_elem = card.find('a', class_='comp-name')
            location_elem = card.find('span', class_='locWdth')
            post_date_elem = card.find('span', class_='job-post-day')
            link = title_elem['href'] if isinstance(title_elem, Tag) and title_elem.has_attr('href') else ''
            jobs.append({
                'title': title_elem.text.strip() if title_elem else '',
                'company': company_elem.text.strip() if company_elem else '',
                'location': location_elem.text.strip() if location_elem else '',
                'link': link,
                'post_date': post_date_elem.text.strip() if post_date_elem else ''
            })

        # Pagination links
        for a in soup.select('a[href]'):
            href = a['href']
            if 'page=' in href or 'start=' in href:
                links.add(href)
        return jobs, links