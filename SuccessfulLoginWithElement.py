from selenium import webdriver
import time

username = "admin"
password = "admin"
url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

assert "Congratulations! You must have the proper credentials." in driver.page_source
time.sleep(5)


