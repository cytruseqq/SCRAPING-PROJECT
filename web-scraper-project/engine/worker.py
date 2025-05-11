import aiohttp
from bs4 import BeautifulSoup
import re
import asyncio
from db import save_data

async def scrape(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')

                # Grupa 1: Adresy email
                emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)

                # Grupa 2: Numery telefonów
                phones = re.findall(r"\+?\d[\d\s\-\(\)]{8,}", html)

                # Grupa 3: Nazwy organizacji (np. nagłówki z 'company' lub 'firma')
                org_names = [tag.text.strip() for tag in soup.find_all(['h1', 'h2', 'h3']) if re.search(r"firma|company|corp|spółka", tag.text, re.IGNORECASE)]

                # Grupa 4: Adresy (tag <address> lub patterny)
                addresses = [tag.text.strip() for tag in soup.find_all('address')]
                addresses += re.findall(r"\d{2}-\d{3} [A-ZŁŚŹĆŃ]{2,}(?: [A-ZŁŚŹĆŃa-ząćęłńóśżź]{2,})+", html)

                result = {
                    "url": url,
                    "emails": list(set(emails)),
                    "phones": list(set(phones)),
                    "organizations": list(set(org_names)),
                    "addresses": list(set(addresses))
                }

                print(f"Scraped from {url}: {result}")
                save_data(result)

        except Exception as e:
            print(f"Error scraping {url}: {e}")

async def async_scrape_urls(urls):
    tasks = [scrape(url) for url in urls]
    await asyncio.gather(*tasks)
