from selenium import webdriver
import time

username = "admin"
password = "alamat"
url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(5)