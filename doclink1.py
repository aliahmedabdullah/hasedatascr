from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Replace with the URL of the page you want to scrape
url = 'https://www.fedlex.admin.ch/eli/cc/2010/413/de'
driver.get(url)

try:
    # Locate the table rows in the desired div
    rows = driver.find_elements(By.XPATH, "//div[@class='well well-white']//table[@id='versionContent']//tbody//tr")
    
    # Loop through all rows
    for row in rows:
        # Check if the span with the class 'circle soft-green' is present in the row
        soft_green_span = row.find_elements(By.XPATH, ".//td//span[@class='circle soft-green']")
        
        if soft_green_span:
            # If the span is found, locate the DOC link in the same row
            doc_link = row.find_element(By.XPATH, ".//a[contains(text(), 'DOC')]")
            doc_link_url = doc_link.get_attribute("href")
            
            # Print the DOC link or click it if needed
            print(f"Found DOC link: {doc_link_url}")
            # doc_link.click()  # Uncomment this to automatically click the link
            
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser after operation
    driver.quit()
