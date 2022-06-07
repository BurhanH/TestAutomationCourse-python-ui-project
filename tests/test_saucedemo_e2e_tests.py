import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest

BASE_URL = 'https://www.saucedemo.com'

USER_NAME = 'standard_user'
CORRECT_PASSWORD = 'secret_sauce'
WRONG_PASSWORD = 'wrong_password'
USER_NAME_LOCATOR_ID = 'user-name'
PASSWORD_LOCATOR_ID = 'password'
LOGIN_BUTTON_LOCATOR_ID = 'login-button'
HAMBURGER_MENU_LOCATOR_ID = 'react-burger-menu-btn'


class TestSaucedemoE2E(BaseTest):
    def setUp(self):
        super(TestSaucedemoE2E, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 8)

    def test_navigate_to_saucedemo_and_verify_title(self) -> None:
        self.assertEqual(self.driver.title, 'Swag Labs')

    def test_success_login(self) -> None:
        user_name_input = self.driver.find_element(By.ID, USER_NAME_LOCATOR_ID)
        user_name_input.click()
        user_name_input.send_keys(USER_NAME)

        password_input = self.driver.find_element(By.ID, PASSWORD_LOCATOR_ID)
        password_input.click()
        password_input.send_keys(CORRECT_PASSWORD)

        login_button = self.driver.find_element(By.ID, LOGIN_BUTTON_LOCATOR_ID)
        login_button.click()
        self.assertEqual(self.driver.current_url, F'{BASE_URL}/inventory.html')

    def test_failed_login(self) -> None:
        user_name_input = self.driver.find_element(By.ID, USER_NAME_LOCATOR_ID)
        user_name_input.click()
        user_name_input.send_keys(USER_NAME)

        password_input = self.driver.find_element(By.ID, PASSWORD_LOCATOR_ID)
        password_input.click()
        password_input.send_keys(WRONG_PASSWORD)

        login_button = self.driver.find_element(By.ID, LOGIN_BUTTON_LOCATOR_ID)
        login_button.click()

        alert_failed_login = self.driver.find_element(By.XPATH, '//form/div[3]/h3')
        actual_failed_login_text = alert_failed_login.text
        expected_failed_login_text = 'Epic sadface: Username and password do not match any user in this service'
        self.assertEqual(actual_failed_login_text, expected_failed_login_text)

    def test_success_log_out(self) -> None:
        user_name_input = self.driver.find_element(By.ID, USER_NAME_LOCATOR_ID)
        user_name_input.click()
        user_name_input.send_keys(USER_NAME)

        password_input = self.driver.find_element(By.ID, PASSWORD_LOCATOR_ID)
        password_input.click()
        password_input.send_keys(CORRECT_PASSWORD)

        login_button = self.driver.find_element(By.ID, LOGIN_BUTTON_LOCATOR_ID)
        login_button.click()

        hamburger_menu = self.driver.find_element(By.ID, HAMBURGER_MENU_LOCATOR_ID)
        hamburger_menu.click()

        log_out_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]')))
        log_out_button.click()

        login_form = self.driver.find_element(By.ID, 'login_button_container')
        login_form.is_displayed()


if __name__ == '__main__':
    unittest.main()
