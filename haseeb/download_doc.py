from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your chromedriver
CHROME_DRIVER_PATH = '/home/aiobc/Desktop/projects/testing/datascraping/chromedriver-linux64/chromedriver'

# Path to the .txt file containing the URLs
LINKS_FILE = 'doc_links.txt'

# Function to read links from .txt file
def read_links(file_path):
    with open(file_path, 'r') as file:
        links = [line.strip() for line in file.readlines()]
    return links

# Function to open links in Chrome
def open_links_in_chrome(links):
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    
    # Initialize the Chrome driver
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Loop through the links and open each in Chrome
    for link in links:
        driver.get(link)
        time.sleep(5)  # Adjust the sleep time as needed

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    links = read_links(LINKS_FILE)
    open_links_in_chrome(links)
