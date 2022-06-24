import pytest
import unittest
from parameterized import parameterized
from utils.base_test import BaseTest
from model.saucedemo.home_page_logged_out import HomePageLoggedOut
from model.saucedemo.home_page_logged_in import HomePageLoggedIn

TARGET_URL = 'https://www.saucedemo.com'


class TestSauceDemoLogin(BaseTest):
    """
    Test suite for saucedemo authentication functionality.
    Includes positive and negative test cases for login.
    TODO: add tests for logout and password masking.
    """

    def setUp(self):
        super(TestSauceDemoLogin, self).setUp(TARGET_URL)

    @pytest.mark.saucedemo
    @pytest.mark.smoke
    @parameterized.expand([
        ['standard_user', 'secret_sauce'],
        ['problem_user', 'secret_sauce'],
        ['performance_glitch_user', 'secret_sauce']
    ])
    def test_login_positive(self, username, password):
        login_page = HomePageLoggedOut(self.driver)
        login_page.login(username, password)

        error_message = f'Failed to login with username: "{username}", password: "{password}".'
        products_page = HomePageLoggedIn(self.driver)
        self.assertEqual(products_page.get_header_title_text(), 'PRODUCTS', error_message)
        products_page.click_burger_menu_button()
        self.assertEqual(products_page.get_logout_button_text(), 'LOGOUT', error_message)

    @pytest.mark.saucedemo
    @pytest.mark.smoke
    def test_login_invalid_password(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.login('standard_user', 'aecret_sauce')

        self.assertFalse(HomePageLoggedIn(self.driver).get_header_title_text(), 'Logged in with invalid password.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Username and password do not match any user in this service'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    @pytest.mark.saucedemo
    @pytest.mark.smoke
    def test_login_no_password(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.type_username('standard_user')
        login_page.click_login_button()

        self.assertFalse(HomePageLoggedIn(self.driver).get_header_title_text(), 'Logged in with no password.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Password is required'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    @pytest.mark.saucedemo
    @pytest.mark.smoke
    def test_login_no_username(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.type_password('secret_sauce')
        login_page.click_login_button()

        self.assertFalse(HomePageLoggedIn(self.driver).get_header_title_text(), 'Logged in with no username.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Username is required'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    @pytest.mark.saucedemo
    @pytest.mark.smoke
    def test_login_empty_fields(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.click_login_button()

        self.assertFalse(HomePageLoggedIn(self.driver).get_header_title_text(), 'Logged in with no credentials.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Username is required'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')

    @pytest.mark.saucedemo
    @pytest.mark.smoke
    def test_login_lock_out_user(self):
        login_page = HomePageLoggedOut(self.driver)
        login_page.login('locked_out_user', 'secret_sauce')

        self.assertFalse(HomePageLoggedIn(self.driver).get_header_title_text(), 'Logged in as locked out user.')
        actual_error_message = login_page.get_error_message()
        expected_error_message = 'Epic sadface: Sorry, this user has been locked out.'
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Actual error message: "{actual_error_message}", expected: "{expected_error_message}".')


if __name__ == '__main__':
    unittest.main()
