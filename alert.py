import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(y)

    btn2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn2.click()

finally:
    time.sleep(10)
    browser.quit()
