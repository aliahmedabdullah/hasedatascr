from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options (headless or visible browsing)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode if you don't need browser UI

# Path to the Chrome WebDriver executable
chrome_driver_path = '/home/aiobc/Desktop/projects/testing/datascraping/chromedriver-linux64/chromedriver'

# Initialize WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# List of URLs to scrape
urls = [
  
"https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de",
"https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de",
"https://www.fedlex.admin.ch/eli/cc/63/946_953_954/de",
"https://www.fedlex.admin.ch/eli/cc/VI/142_141_127/de",
"https://www.fedlex.admin.ch/eli/cc/VII/38_38_39/de",

    # Add more URLs here
]

# Function to scrape DOC links from a given URL
def scrape_doc_links(url):
    print(f"Scraping {url}...")
    driver.get(url)

    # Wait until the table is present (maximum 10 seconds wait)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'versionContent')))
        print("Table found!")

        # Find the table rows
        rows = driver.find_elements(By.CSS_SELECTOR, 'table#versionContent tbody tr')
        print(f"Total rows found: {len(rows)}")  # Debug print to check if rows are found

        # Iterate through the rows
        for row in rows:
            # Check if the row contains the green circle span
            green_circle = row.find_elements(By.CSS_SELECTOR, 'span.circle.soft-green')

            if green_circle:
                print("Green circle found in row!")  # Debug print to confirm green circle found
                # If the green circle is found, look for the DOC link in the same row
                doc_link = row.find_element(By.XPATH, './/a[contains(@href, ".docx")]')

                if doc_link:
                    # Print the DOC link URL
                    with open('doc_links.txt', 'a') as file:
                        file.write(f'{doc_link.get_attribute("href")}\n')
                    break  # Exit loop after the first match

    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")

# Loop through the list of URLs and scrape each one
for url in urls:
    scrape_doc_links(url)

# Close the browser after scraping all URLs
driver.quit()
