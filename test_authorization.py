import pytest
from selenium.webdriver.common.by import By

from selenium import webdriver
from settings import EMAIL, PASSWORD

link = 'https://stepik.org/lesson/236895/step/1'


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_stepik_authorization(browser):
    browser.implicitly_wait(5)
    browser.get(link)

    login_btn = browser.find_element(By.ID, 'ember471')
    login_btn.click()

    email = browser.find_element(By.ID, 'id_login_email')
    email.send_keys(EMAIL)

    password = browser.find_element(By.ID, 'id_login_password')
    password.send_keys(PASSWORD)

    login_btn2 = browser.find_element(By.XPATH, '//button[text()="Войти"]')
    login_btn2.click()
