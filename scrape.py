# Program to implement selenium web scraping:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

# function:
def scrape_website(url):
    driver_path = "chromedriver.exe"  
    options = webdriver.ChromeOptions()
    # Diable Pop window:
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    try:
        driver.get(url)
        time.sleep(3)  
        html = driver.page_source
        return html
    finally:
        driver.quit()

# body extraction function:
def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

# Clean function:
def clean_html_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = '\n'.join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

# Token separation function:
def separate_into_tokens(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
