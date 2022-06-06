import unittest
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest

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


class TestSaucedemo(BaseTest):
    def setUp(self):
        self._setUp(TARGET_URL)

    def test_empty_fields(self):
        self.driver.find_element(By.ID, LOGIN_BUTTON_ID).click()

        actual_error_message = self.driver.find_element(By.XPATH, ERROR_MESSAGE_XPATH)
        expected_error_message = 'Epic sadface: Username is required'
        self.assertTrue(actual_error_message.is_displayed())
        self.assertEqual(actual_error_message.text, expected_error_message, 'Error message is not equal to expected')

        # trying to sign in without password
        user_name = 'standard_user'
        user_name_input = self.driver.find_element(By.ID, USER_NAME_ID)
        user_name_input.click()
        user_name_input.send_keys(user_name)

        self.driver.find_element(By.ID, LOGIN_BUTTON_ID).click()

        actual_error_message = self.driver.find_element(By.XPATH, ERROR_MESSAGE_XPATH)
        expected_error_message = 'Epic sadface: Password is required'
        self.assertTrue(actual_error_message.is_displayed())
        self.assertEqual(actual_error_message.text, expected_error_message, 'Error message is not equal to expected')

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


    def test_pgu_autorization_and_order(self):
        user_name = 'performance_glitch_user'
        password = 'secret_sauce'

        user_name_field = self.driver.find_element(By.ID, USER_NAME_ID)
        user_name_field.click()
        user_name_field.send_keys(user_name)

        password_field = self.driver.find_element(By.ID, PASSWORD_ID)
        password_field.click()
        password_field.send_keys(password)

        self.driver.find_element(By.ID, LOGIN_BUTTON_ID).click()

        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/inventory.html', 'Not an expected url')

        item_4_title = self.driver.find_element(By.XPATH, ITEM_4_TITLE_XPATH)
        item_4_title_text = self.driver.find_element(By.XPATH, ITEM_4_TITLE_XPATH).text
        item_4_title.click()

        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/inventory-item.html?id=4')
        item_4_info = self.driver.find_element(By.XPATH, ITEM_4_INFO_XPATH).text
        self.assertEqual(item_4_title_text, item_4_info, 'Item and description does not match')

        self.driver.find_element(By.ID, ADD_ITEM_4_ID).click()

        self.driver.find_element(By.XPATH, CART_LINK_XPATH).click()

    #     checkout
        self.driver.find_element(By.ID, CHECKOUT_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/checkout-step-one.html')

    #     typing personal info
        first_name = 'first'
        last_name = 'last'
        zip_code = 'aaa'

        first_name_input = self.driver.find_element(By.ID, 'first-name')
        first_name_input.click()
        first_name_input.send_keys(first_name)

        last_name_input = self.driver.find_element(By.ID, 'last-name')
        last_name_input.click()
        last_name_input.send_keys(last_name)

        zip_code_input = self.driver.find_element(By.ID, 'postal-code')
        zip_code_input.click()
        zip_code_input.send_keys(zip_code)

        self.driver.find_element(By.ID, CONTINUE_BUTTON_ID ).click()

        self.driver.find_element(By.ID, FINISH_BUTTON_ID).click()

        self.assertTrue(self.driver.current_url, f'{TARGET_URL}/checkout-complete.html')


    # def tearDown(self) -> None:
    #     self.driver.close()


if __name__ == '__main__':
    unittest.main()
