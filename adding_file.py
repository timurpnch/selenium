import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    values = {'firstname': 'Ivan', 'lastname': 'Ivanov', 'email': 'test@mail.ru'}

    for key, value in values.items():
        element = browser.find_element(By.NAME, f'{key}')
        element.send_keys(value)

    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR,'button.btn')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
