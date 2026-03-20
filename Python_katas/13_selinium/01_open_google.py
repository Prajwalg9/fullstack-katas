from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()  # or Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')
