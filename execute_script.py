import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    res = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    browser.execute_script('arguments[0].scrollIntoView(true);', answer)
    answer.send_keys(res)

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
