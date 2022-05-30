import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestBrowser(unittest.TestCase):
    def setUp(self) -> None:
        """
        Initiate driver for each test
        """
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        if 'CICD_RUN' in os.environ:
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test_navigate_to_saucedemo_and_verify_title(self) -> None:
        self.driver.get('https://www.saucedemo.com')
        self.assertEqual(self.driver.title, 'Swag Labs')

    def test_success_login(self) -> None:
        self.driver.get('https://www.saucedemo.com')
        user_name = 'standard_user'
        password = 'secret_sauce'

        user_name_input = self.driver.find_element(By.ID, 'user-name')
        user_name_input.click()
        user_name_input.send_keys(user_name)

        password_input = self.driver.find_element(By.ID, 'password')
        password_input.click()
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.ID, 'login-button')
        login_button.click()
        self.assertEqual(self.driver.current_url, 'https://www.saucedemo.com/inventory.html')

    def tearDown(self) -> None:
        """
        Closing driver after each test
        """
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
