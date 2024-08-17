from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(options=Options())
driver.get("https://the-internet.herokuapp.com/upload")

file_upload_element = driver.find_element(By.ID, "file-upload")

file_path = "D:/dummy/dummy.docx"

file_upload_element.send_keys(file_path)

upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()

WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "uploaded-files"), "dummy.docx"))

assert "File Uploaded!" in driver.page_source