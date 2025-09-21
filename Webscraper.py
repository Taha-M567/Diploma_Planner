import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# The URL you want to scrape
url = "https://uwaterloo.ca/academic-calendar/undergraduate-studies/catalog#/programs/Hk-A1y0Cj2?searchTerm=mechatronics&bc=true&bcCurrent=Mechatronics%20Engineering%20(Bachelor%20of%20Applied%20Science%20-%20Honours)&bcItemType=programs"

# Set up the Selenium WebDriver
# This line creates a new Chrome browser window that the script will control.
driver = webdriver.Chrome() 

# Open the URL in the controlled browser
driver.get(url)

try:
    # --- This is the crucial step ---
    # Wait for a maximum of 10 seconds for the elements containing your target text to become present on the page.
    # This tells Selenium to pause until the JavaScript has loaded the content.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Complete all of the following:')]"))
    )

    # Now that the page is loaded, get the full page source HTML
    html_content = driver.page_source

    # Parse the fully rendered HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Now, your original search will work!
    # We use a lambda function to find tags whose text contains our target phrase.
    target_elements = soup.find_all(lambda tag: "Complete all of the following:" in tag.get_text())
    
    print(f"Found {len(target_elements)} elements with the target text.\n")

    for i, element in enumerate(target_elements):
        print(f"--- Element {i+1} ---")
        # .text will give you the clean text inside the tag
        print(element.text.strip()) 
        print("\n")

finally:
    # Always close the browser window when you're done
    driver.quit()