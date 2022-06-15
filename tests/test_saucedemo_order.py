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


class TestSaucedemo(BaseTest):
    def setUp(self):
        super(TestSaucedemo, self).setUp(TARGET_URL)

    def test_standard_user_order(self):
        user_name = 'standard_user'
        password = 'secret_sauce'

        self.driver.find_element(By.ID, USER_NAME_ID).send_keys(user_name)
        self.driver.find_element(By.ID, PASSWORD_ID).send_keys(password)
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

        # checkout
        self.driver.find_element(By.ID, CHECKOUT_BUTTON_ID).click()
        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/checkout-step-one.html')

        # typing personal info
        first_name = 'first'
        last_name = 'last'
        zip_code = 'aaa'

        self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(By.ID, 'postal-code').send_keys(zip_code)
        self.driver.find_element(By.ID, CONTINUE_BUTTON_ID ).click()
        self.driver.find_element(By.ID, FINISH_BUTTON_ID).click()

        self.assertTrue(self.driver.current_url, f'{TARGET_URL}/checkout-complete.html')


if __name__ == '__main__':
    unittest.main()
