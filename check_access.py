import httpx
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
    with httpx.Client(headers=headers, follow_redirects=True) as client:
        response = client.get(url)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title"
            print(f"Page Title: {title}")
            
            # Try to find a product to see if we got the real page
            products = soup.find_all('div', class_='catalog-product')
            print(f"Found {len(products)} products (by class 'catalog-product')")
            
            # DNS often uses different classes, let's try a broader search if 0
            if len(products) == 0:
                 # Look for something that looks like a product name
                 items = soup.find_all('a', class_='catalog-product__name')
                 print(f"Found {len(items)} product names (by class 'catalog-product__name')")

        else:
            print("Failed to retrieve page")
            
except Exception as e:
    print(f"Error: {e}")
