from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('selenium')
time.sleep(5)

search_button = driver.find_element(By.NAME, 'btnK')
search_button.click()
