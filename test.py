from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = 'https://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    values = {'First name*': 'Ivan', 'Last name*': 'Ivanov', 'Email*': 'test@mail.ru'}

    for key, value in values.items():
        element = browser.find_element(By.XPATH, f"//label[text()='{key}']/following::input")
        element.send_keys(value)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()