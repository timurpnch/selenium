import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 17).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    btn1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn1.click()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(y)

    btn2 = browser.find_element(By.ID, 'solve')
    btn2.click()

    alert = browser.switch_to.alert
    text = alert.text
    alert.accept()

    result = text.split()[-1]
    print(result)
finally:
    time.sleep(10)
    browser.quit()
