import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    values = {'First name*': 'Ivan',
              'Last name*': 'Ivanov',
              'Email*': 'test@mail.ru'}

    def page(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        for key, value in self.values.items():
            element = browser.find_element(By.XPATH, f"//label[text()='{key}']/following::input")
            element.send_keys(value)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.page(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.page(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == '__main__':
    unittest.main()