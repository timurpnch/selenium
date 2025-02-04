import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    s = int(num1)+int(num2)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(s))

    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
