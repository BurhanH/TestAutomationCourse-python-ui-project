import pytest
import unittest
from utils.base_test import BaseTest
from model.saucedemo.home_page_logged_out import HomePageLoggedOut
from model.saucedemo.home_page_logged_in import HomePageLoggedIn

TARGET_URL = 'https://www.saucedemo.com'


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

        self.assertFalse(HomePageLoggedIn(self.driver).is_burger_icon_present(), 'Logged in with no password.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Password is required'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    def test_login_no_username(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.type_password('secret_sauce')
        login_page.click_login_button()

        self.assertFalse(HomePageLoggedIn(self.driver).is_burger_icon_present(), 'Logged in with no username.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Username is required'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    def test_login_empty_fields(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.click_login_button()

        self.assertFalse(HomePageLoggedIn(self.driver).is_burger_icon_present(), 'Logged in with no credentials.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Username is required'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    def test_login_lock_out_user(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.login('locked_out_user', 'secret_sauce')

        self.assertFalse(HomePageLoggedIn(self.driver).is_burger_icon_present(), 'Logged in as locked out user.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Sorry, this user has been locked out.'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    # @pytest.mark.skip('Test fails, login takes too long.')
    def test_login_performance_glitch_user(self):
        username = 'performance_glitch_user'
        password = 'secret_sauce'
        login_page = HomePageLoggedOut(self.driver)
        login_page.login(username, password)

        products_page = HomePageLoggedIn(self.driver)
        print(f'check is_burger_icon_present: {products_page.is_burger_icon_present()}')
        self.assertTrue(products_page.is_burger_icon_present(),
                        f'Burger menu button not found on home page after attempt to login with '
                        f'username: "{username}", password: "{password}".')
        products_page.click_burger_menu_button()
        self.assertEqual(products_page.get_logout_button_text(), 'LOGOUT',
                         f'Failed to login with username: "{username}", password: "{password}".')


if __name__ == '__main__':
    unittest.main()
