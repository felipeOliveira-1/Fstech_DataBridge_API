import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_website_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = [p.text for p in soup.find_all('p')]
    return content

def scrape_all_urls():
    urls = [
        "https://felipesilva.tech/",
        "https://felipesilva.tech/agentes-autonomos",
        "https://felipesilva.tech/consultoria-empresarial",
        "https://felipesilva.tech/desenvolvimento-de-chatbots",
        "https://felipesilva.tech/custom-gpts",
        "https://felipesilva.tech/blog",
        "https://felipesilva.tech/contato"
    ]
    
    scraped_data = {}
    for url in urls:
        scraped_data[url] = scrape_website_content(url)
    
    with open('website_content.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    while True:
        scrape_all_urls()
        print("Scraping completed. Waiting for 2 minutes before next run.")
        time.sleep(100)  # Wait for 2.5 minutes