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

# Open the webpage
driver.get('https://www.fedlex.admin.ch/de/cc/internal-law/0.10#0.103.2')

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
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
