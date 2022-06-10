import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest
import pytest

BASE_URL = 'https://www.saucedemo.com/'

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

    @pytest.mark.smoke
    def test_navigate_to_saucedemo_and_verify_title(self) -> None:
        self.assertEqual(self.driver.title, 'Swag Labs')

    @pytest.mark.smoke
    def test_success_login(self) -> None:
        user_name_input = self.driver.find_element(By.ID, USER_NAME_LOCATOR_ID)
        user_name_input.click()
        user_name_input.send_keys(USER_NAME)

        password_input = self.driver.find_element(By.ID, PASSWORD_LOCATOR_ID)
        password_input.click()
        password_input.send_keys(CORRECT_PASSWORD)

        self.driver.find_element(By.ID, LOGIN_BUTTON_LOCATOR_ID).click()
        self.assertEqual(self.driver.current_url, F'{BASE_URL}inventory.html',
                         'Current url and expected url does not match')

    def test_buy_backpack(self) -> None:
        user_name_input = self.driver.find_element(By.ID, USER_NAME_LOCATOR_ID)
        user_name_input.click()
        user_name_input.send_keys(USER_NAME)

        password_input = self.driver.find_element(By.ID, PASSWORD_LOCATOR_ID)
        password_input.click()
        password_input.send_keys(CORRECT_PASSWORD)

        self.driver.find_element(By.ID, LOGIN_BUTTON_LOCATOR_ID).click()

        actual_first_item_name = self.driver.find_element(By.ID, 'item_4_title_link').text
        expected_first_item_name = 'Sauce Labs Backpack'
        self.assertEqual(actual_first_item_name, expected_first_item_name, 'Wrong item name')

        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

        shopping_cart_badge_count = self.driver.find_element(By.XPATH, '//a/span').text
        expected_shopping_cart_badge = '1'
        self.assertEqual(shopping_cart_badge_count, expected_shopping_cart_badge,
                         f"Cart badge suppose to be equal, but actual badge is: '{shopping_cart_badge_count}') and "
                         f"expected badge is: '{expected_shopping_cart_badge}' ")

        self.driver.find_element(By.ID, 'shopping_cart_container').click()

        item_title_text = self.driver.find_element(By.ID, 'item_4_title_link').text
        self.assertEqual(item_title_text, expected_first_item_name,
                         f"Unexpected title: '{item_title_text}', "
                         f"expected: '{expected_first_item_name}'.")

        self.driver.find_element(By.ID, 'checkout').click()

        first_name_input = self.driver.find_element(By.ID, 'first-name')
        first_name_input.click()
        first_name_input.send_keys('My name')

        last_name_input = self.driver.find_element(By.ID, 'last-name')
        last_name_input.click()
        last_name_input.send_keys('My last name')

        postal_code_input = self.driver.find_element(By.ID, 'postal-code')
        postal_code_input.click()
        postal_code_input.send_keys('02211')

        self.driver.find_element(By.ID, 'continue').click()

        self.driver.find_element(By.ID, 'finish').click()

        complete_message_text = self.driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2').text
        expected_complete_message = 'THANK YOU FOR YOUR ORDER'
        self.assertEqual(complete_message_text, expected_complete_message,
                         f"After a successful purchase, the user should see '{expected_complete_message}',"
                         f" but sees: '{complete_message_text}'.")

    def test_failed_login(self) -> None:
        user_name_input = self.driver.find_element(By.ID, USER_NAME_LOCATOR_ID)
        user_name_input.click()
        user_name_input.send_keys(USER_NAME)

        password_input = self.driver.find_element(By.ID, PASSWORD_LOCATOR_ID)
        password_input.click()
        password_input.send_keys(WRONG_PASSWORD)

        self.driver.find_element(By.ID, LOGIN_BUTTON_LOCATOR_ID).click()

        actual_failed_login_text = self.driver.find_element(By.XPATH, '//form/div[3]/h3').text
        expected_failed_login_text = 'Epic sadface: Username and password do not match any user in this service'
        self.assertEqual(actual_failed_login_text, expected_failed_login_text,
                         'Actual failed login text not equal Expected failed login text')

    @pytest.mark.smoke
    def test_success_log_out(self) -> None:
        user_name_input = self.driver.find_element(By.ID, USER_NAME_LOCATOR_ID)
        user_name_input.click()
        user_name_input.send_keys(USER_NAME)

        password_input = self.driver.find_element(By.ID, PASSWORD_LOCATOR_ID)
        password_input.click()
        password_input.send_keys(CORRECT_PASSWORD)

        self.driver.find_element(By.ID, LOGIN_BUTTON_LOCATOR_ID).click()

        self.driver.find_element(By.ID, HAMBURGER_MENU_LOCATOR_ID).click()

        log_out_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]')))
        log_out_button.click()

        self.driver.find_element(By.ID, 'login_button_container').is_displayed()
        self.assertEqual(self.driver.current_url, F'{BASE_URL}',
                         f"Current url '{self.driver.current_url}' and expected url {BASE_URL} does not match')")


if __name__ == '__main__':
    unittest.main()
