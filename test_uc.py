import sys
import os

# Add local packages to path
local_packages = os.path.abspath("./.packages")
if local_packages not in sys.path:
    sys.path.append(local_packages)

print(f"Added {local_packages} to sys.path")

try:
    import setuptools # Should monkeypatch distutils
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    print("Undetected ChromeDriver imported successfully")
except ImportError as e:
    print(f"Failed to import undetected_chromedriver: {e}")
    sys.exit(1)

import time

def test_uc():
    print("Starting Undetected ChromeDriver test...")
    
    options = uc.ChromeOptions()
    options.add_argument("--headless=new") # Use new headless mode for better evasion
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    try:
        print("Initializing driver...")
        # uc.Chrome automatically downloads and patches the driver
        driver = uc.Chrome(options=options, version_main=120) # Try specifying version if needed, or omit for auto
        print("Driver initialized!")
        
        url = "https://www.dns-shop.ru/catalog/17a8ae4916404e77/televizory/?order=1&stock=now-today-tomorrow-later&brand=lg"
        print(f"Navigating to {url}...")
        driver.get(url)
        time.sleep(10) # Wait for Cloudflare/protection
        
        print(f"Page Title: {driver.title}")
        
        # Check for products
        products = driver.find_elements(By.CLASS_NAME, "catalog-product")
        print(f"Found {len(products)} products")
        
        driver.quit()
        print("Test passed!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_uc()
