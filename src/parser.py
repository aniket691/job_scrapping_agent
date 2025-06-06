from bs4 import BeautifulSoup

def parse_job_listings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    job_listings = []

    # Find job cards in the HTML
    job_cards = soup.find_all('div', class_='job_seen_beacon')

    from bs4.element import Tag

    # type: ignore[assignment]  # job_card is a Tag, but type checker may not infer it
    for job_card in job_cards:
        if isinstance(job_card, Tag):
            title_elem = job_card.find('h2', class_='jobTitle')
            title = title_elem.get_text(strip=True) if title_elem else None

            company_elem = job_card.find('span', class_='companyName')
            company = company_elem.get_text(strip=True) if company_elem else None

            location_elem = job_card.find('div', class_='companyLocation')
            location = location_elem.get_text(strip=True) if location_elem else None

            if title and company and location:
                job_listings.append({
                    'title': title,
                    'company': company,
                    'location': location
                })

    return job_listings