from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the target URL
url = "https://www.fedlex.admin.ch/de/cc/internal-law/1"
driver.get(url)

# Wait for the page to load (adjust time if needed)
time.sleep(5)

# Locate the table inside the div with id 'content'
table = driver.find_element(By.XPATH, "//div[@id='content']//table")

# Extract all anchor tags within the table
links = table.find_elements(By.TAG_NAME, "a")

# Extract and print all href attributes
hrefs = [link.get_attribute("href") for link in links]

with open('hrefs1.txt', 'w') as file:
    for href in hrefs:
        file.write(href + '\n')

# Close the browser
driver.quit()
