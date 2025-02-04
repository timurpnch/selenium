import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(y)

    btn2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn2.click()


finally:
    time.sleep(10)
    browser.quit()
