from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options and driver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off for headless mode

# Initialize webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# List of URLs
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
            # Add more URLs as needed
]

# Path for the output file
file_path = 'hrefslinks.txt'

# Open the file for writing (in append mode to handle multiple pages)
with open(file_path, 'w') as file:
    # Loop through each URL
    for url in urls:
        # Open the URL
        driver.get(url)
        
        # Locate the table or container by its ID and extract all hrefs
        table_div = driver.find_element(By.ID, "content")
        links = table_div.find_elements(By.TAG_NAME, "a")

        # Get href attribute from each link
        hrefs = [link.get_attribute('href') for link in links]
        
        # Write the hrefs to the file
        file.write(f"Links from {url}:\n")
        for href in hrefs:
            file.write(f"{href}\n")
        file.write("\n")  # Add a new line after each URL's links

# Close the browser
driver.quit()

print(f"Links saved to {file_path}")
