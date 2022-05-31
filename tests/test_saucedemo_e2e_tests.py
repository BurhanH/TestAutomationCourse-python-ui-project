import unittest
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest

BASE_URL = 'https://www.saucedemo.com'


class TestBrowser(BaseTest):
    def setUp(self):
        self._setUp(BASE_URL)

    def test_navigate_to_saucedemo_and_verify_title(self) -> None:
        self.assertEqual(self.driver.title, 'Swag Labs')

    def test_success_login(self) -> None:
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
        self.assertEqual(self.driver.current_url, F'{BASE_URL}/inventory.html')


if __name__ == '__main__':
    unittest.main()
