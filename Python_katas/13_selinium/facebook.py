from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

driver = webdriver.Chrome()

driver.get("https://www.facebook.com")
sleep(2)

emailelement = driver.find_element(By.NAME, "email")
emailelement.send_keys('prajwalgg99@gmail.com')

passelement = driver.find_element(By.NAME, "pass")
passelement.send_keys('viruGG99@')

elem = driver.find_element(By.NAME, "login")
elem.click()

sleep(8)

statuselement = driver.find_element(By.XPATH, "//div[@role='combobox']")
statuselement.send_keys('Good morning everyone')

sleep(5)

buttons = driver.find_elements(By.TAG_NAME, 'button')

for button in buttons:
    if button.text == 'Post':
        button.click()