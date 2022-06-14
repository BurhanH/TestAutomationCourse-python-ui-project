import pytest
import unittest
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest
from model.saucedemo.home_page_logged_out import HomePageLoggedOut
from model.saucedemo.home_page_logged_in import HomePageLoggedIn

TARGET_URL = 'https://www.saucedemo.com'
LOGIN_BUTTON_ID = 'login-button'
USER_NAME_ID = 'user-name'
PASSWORD_ID = 'password'
ADD_ITEM_4_ID = 'add-to-cart-sauce-labs-backpack'
CART_LINK_XPATH = '//*[@id="shopping_cart_container"]/a/span'
ITEM_4_TITLE_XPATH = '//*[@id="item_4_title_link"]/div'
ITEM_4_INFO_XPATH = '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'
CHECKOUT_BUTTON_ID = 'checkout'
CONTINUE_BUTTON_ID = 'continue'
FINISH_BUTTON_ID = 'finish'
ERROR_MESSAGE_XPATH = '//*[@id="login_button_container"]//h3'


class TestSaucedemoLogin(BaseTest):
    def setUp(self):
        super(TestSaucedemoLogin, self).setUp(TARGET_URL)

    def test_login_standard_user(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.login('standard_user', 'secret_sauce')
        products_page = HomePageLoggedIn(self.driver)
        self.assertTrue(products_page.is_burger_icon_present(),
                        'Burger menu button not found on home page after login.')
        products_page.click_burger_menu_button()
        self.assertEqual(products_page.get_logout_button_text(), 'LOGOUT', 'Failed to login as standard user')

    def test_login_invalid_password(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.login('standard_user', 'aecret_sauce')
        self.assertFalse(HomePageLoggedIn(self.driver).is_burger_icon_present(), 'Logged in with invalid password.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Username and password do not match any user in this service'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    def test_login_no_password(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.type_username('standard_user')
        login_page.click_login_button()
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Password is required'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    def test_login_no_username(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.type_password('secret_sauce')
        login_page.click_login_button()
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Username is required'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')


    # @pytest.mark.skip('temporarily disabled, need refactoring')
    def test_empty_fields(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.click_login_button()

        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Username is required'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    @pytest.mark.skip('temporarily disabled, need refactoring')
    def test_lock_out_user_autorization(self):

        user_name = 'locked_out_user'
        password = 'secret_sauce'

        user_name_field = self.driver.find_element(By.ID, USER_NAME_ID)
        user_name_field.click()
        user_name_field.send_keys(user_name)

        password_field = self.driver.find_element(By.ID, PASSWORD_ID)
        password_field.click()
        password_field.send_keys(password)

        self.driver.find_element(By.ID, LOGIN_BUTTON_ID).click()

        actual_error_message = self.driver.find_element(By.XPATH, ERROR_MESSAGE_XPATH)
        expected_error_message = 'Epic sadface: Sorry, this user has been locked out.'
        self.assertTrue(actual_error_message.is_displayed())
        self.assertEqual(actual_error_message.text, expected_error_message, 'Error message is not equal to expected')

    @pytest.mark.skip('temporarily disabled, need refactoring')
    def test_problem_user_autorization(self):

        user_name = 'problem_user'
        password = 'secret_sauce'

        user_name_field = self.driver.find_element(By.ID, USER_NAME_ID)
        user_name_field.click()
        user_name_field.send_keys(user_name)

        password_field = self.driver.find_element(By.ID, PASSWORD_ID)
        password_field.click()
        password_field.send_keys(password)

        self.driver.find_element(By.ID, LOGIN_BUTTON_ID).click()

        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/inventory.html', 'Not an expected url')

        self.driver.find_element(By.ID, ADD_ITEM_4_ID).click()

        self.driver.find_element(By.XPATH, CART_LINK_XPATH).click()
        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/cart.html', 'This is not an expected url')
        item_4_title = self.driver.find_element(By.XPATH, ITEM_4_TITLE_XPATH)
        self.assertTrue(item_4_title.is_displayed())
        item_4_title_text = self.driver.find_element(By.XPATH, ITEM_4_TITLE_XPATH).text
        item_4_title.click()
        item_4_info = self.driver.find_element(By.XPATH, ITEM_4_INFO_XPATH).text
        self.assertNotEqual(item_4_title_text, item_4_info)


if __name__ == '__main__':
    unittest.main()
