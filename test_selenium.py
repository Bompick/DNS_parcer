import sys
import os

# Add local packages to path
local_packages = os.path.abspath("./.packages")
if local_packages not in sys.path:
    sys.path.append(local_packages)

print(f"Added {local_packages} to sys.path")

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    print("Selenium imported successfully")
except ImportError as e:
    print(f"Failed to import selenium: {e}")
    sys.exit(1)

import time

def test_selenium():
    print("Starting Selenium test...")
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Anti-detection options
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    try:
        print("Installing ChromeDriver...")
        driver_path = ChromeDriverManager().install()
        print(f"ChromeDriver installed at: {driver_path}")
        
        service = Service(driver_path)
        print("Starting Chrome driver...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("Chrome driver started!")
        
        # Bypass detection
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            """
        })
        
        url = "https://www.dns-shop.ru/catalog/17a8ae4916404e77/televizory/?order=1&stock=now-today-tomorrow-later&brand=lg"
        print(f"Navigating to {url}...")
        driver.get(url)
        time.sleep(5) # Wait for page to load
        
        print(f"Page Title: {driver.title}")
        
        driver.quit()
        print("Selenium test passed!")
        
    except Exception as e:
        print(f"Selenium error: {e}")

if __name__ == "__main__":
    test_selenium()
