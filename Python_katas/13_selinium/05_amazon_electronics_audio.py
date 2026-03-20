from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.in')
driver.maximize_window()

time.sleep(5)

electronics = driver.find_element(By.LINK_TEXT, 'Electronics')
electronics.click()

time.sleep(5)

audio = driver.find_element(By.LINK_TEXT, 'Audio')
audio.click()
