from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')
driver.maximize_window()

time.sleep(5)
driver.refresh()
