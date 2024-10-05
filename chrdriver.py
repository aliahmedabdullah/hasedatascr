import requests
import zipfile
import os
import re
import shutil

def get_latest_chromedriver_version():
    # Get the latest version of ChromeDriver
    response = requests.get('https://googlechromelabs.github.io/chrome-for-testing/#stable')
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception("Failed to retrieve the latest ChromeDriver version.")

def download_chromedriver(version, download_dir="chromedriver"):
    # Construct the URL to download the ChromeDriver zip file for Linux (Ubuntu)
    url = "https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.89/linux64/chromedriver-linux64.zip"
    
    # Create download directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    zip_path = os.path.join(download_dir, "chromedriver_linux64.zip")
    
    # Download the file
    print(f"Downloading ChromeDriver version")
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(zip_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        print("Download complete!")
    else:
        raise Exception(f"Failed to download ChromeDriver from {url}")

    return zip_path

def unzip_chromedriver(zip_path):
    # Get the directory where the script is running
    extract_to = os.getcwd()  # or use os.path.dirname(__file__) for the script's directory
    
    # Unzip the ChromeDriver zip file
    print(f"Unzipping {zip_path} to {extract_to}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Unzipped to {extract_to}")
    
    # Optionally remove the zip file after extraction
    os.remove(zip_path)
    print(f"Removed zip file: {zip_path}")


if __name__ == "__main__":
    try:
        # Step 1: Get the latest ChromeDriver version
        latest_version = get_latest_chromedriver_version()
        version_pattern = r"Version: <code>(\d+\.\d+\.\d+\.\d+)</code>"
    
        # Search for the pattern in the input text
        match = re.search(version_pattern, latest_version)
        
        # # If a match is found, return the version
        # if match:
        #     with open("filename.txt", 'w', encoding='utf-8') as file:
        #      file.write(match.group(1)) 
        
        # Step 2: Download the latest ChromeDriver zip file
        zip_file = download_chromedriver(latest_version)
        
        # Step 3: Unzip the ChromeDriver
        unzip_chromedriver(zip_file)
        
        print("ChromeDriver setup completed!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
