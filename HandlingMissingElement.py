import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/disappearing_elements"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Total number of links on the page: {len(all_links)}")

for link in all_links:
    href = link.get_attribute('href')
    try:
        response = requests.get(href)
        if response.status_code >= 400:
            print(f"Broken link: {href} (Status code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {href}: {e}")

driver.quit()