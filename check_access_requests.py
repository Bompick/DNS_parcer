import sys
import os

# Add local packages to path
sys.path.append(os.path.abspath("./.packages"))

import requests
from bs4 import BeautifulSoup

url = "https://www.dns-shop.ru/catalog/17a8ae4916404e77/televizory/?order=1&stock=now-today-tomorrow-later&brand=lg"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}

try:
    session = requests.Session()
    session.headers.update(headers)
    
    response = session.get(url, timeout=30)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title"
        print(f"Page Title: {title}")
        
        products = soup.find_all('div', class_='catalog-product')
        print(f"Found {len(products)} products")
    else:
        print("Failed to retrieve page")

except Exception as e:
    print(f"Error: {e}")
