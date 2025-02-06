import math
import time

import pytest
from selenium.webdriver.common.by import By

from selenium import webdriver
from settings import EMAIL, PASSWORD


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

The owls are not what they seem! OvO

@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_stepik_task(browser, link):
    # link = 'https://stepik.org/lesson/236895/step/1'
    answer = math.log(int(time.time()))

    browser.get(link)

    time.sleep(5)

    login_btn = browser.find_element(By.CLASS_NAME, 'navbar__auth_login ')
    login_btn.click()

    email = browser.find_element(By.ID, 'id_login_email')
    email.send_keys(EMAIL)
    password = browser.find_element(By.ID, 'id_login_password')
    password.send_keys(PASSWORD)

    login_btn2 = browser.find_element(By.XPATH, '//button[text()="Войти"]')
    login_btn2.click()
    time.sleep(25)
    placeholders = browser.find_elements(By.TAG_NAME, 'textarea')
    placeholders[0].send_keys(answer)

    time.sleep(25)
    result = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert result == 'Correct!'

    # time.sleep(5)
    #
    # submit_btn = browser.find_element(By.CLASS_NAME, 'submit-submission')
    # submit_btn.click()
    #
    # time.sleep(30)

    # result = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text
    # print(result)
    # assert result == 'Correct!'



