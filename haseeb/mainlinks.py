from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# List of target URLs
urls = [
    "https://www.fedlex.admin.ch/de/cc/internal-law/1",
    "https://www.fedlex.admin.ch/de/cc/internal-law/2",
    "https://www.fedlex.admin.ch/de/cc/internal-law/3",
    "https://www.fedlex.admin.ch/de/cc/internal-law/4",
    "https://www.fedlex.admin.ch/de/cc/internal-law/5",
    "https://www.fedlex.admin.ch/de/cc/internal-law/6",  
    "https://www.fedlex.admin.ch/de/cc/internal-law/7",
    "https://www.fedlex.admin.ch/de/cc/internal-law/8",
    "https://www.fedlex.admin.ch/de/cc/internal-law/9",

]

with open('hrefs.txt', 'w') as file:
# Loop through each URL and extract hrefs
    for i, url in enumerate(urls):
        # Open the target URL
        driver.get(url)
        
        # Wait for the page to load (adjust time if needed)
        time.sleep(5)
        
        try:
            # Locate the table inside the div with id 'content'
            table = driver.find_element(By.XPATH, "//div[@id='content']//table")
            
            # Extract all anchor tags within the table
            links = table.find_elements(By.TAG_NAME, "a")
            
            # Extract href attributes
            hrefs = [link.get_attribute("href") for link in links]
            
            # Write hrefs to a file, using a unique file for each URL
            
            for href in hrefs:
                file.write(href + '\n')
        
            print(f"Extracted {len(hrefs)} links from {url}")
            
        except Exception as e:
            print(f"Error extracting from {url}: {e}")

# Close the browser
driver.quit()
