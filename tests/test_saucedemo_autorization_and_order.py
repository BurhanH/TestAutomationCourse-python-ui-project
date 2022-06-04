import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

TARGET_URL = 'https://www.saucedemo.com'


class TestSaucedemo(unittest.TestCase):

    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.set_window_size(1024, 768)


    def test_lock_out_user_autorization(self):

        self.driver.get(TARGET_URL)
        user_name = 'locked_out_user'
        password = 'secret_sauce'

        user_name_field = self.driver.find_element(By.ID, 'user-name')
        user_name_field.click()
        user_name_field.send_keys(user_name)

        password_field = self.driver.find_element(By.ID, 'password')
        password_field.click()
        password_field.send_keys(password)

        sign_in = self.driver.find_element(By.ID, 'login-button')
        sign_in.click()
        actual_error_message = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]//h3')
        expected_error_message = 'Epic sadface: Sorry, this user has been locked out.'
        self.assertTrue(actual_error_message.is_displayed())
        self.assertEqual(actual_error_message.text, expected_error_message, 'Error message is not equal to expected')

    def test_problem_user_autorization(self):

        self.driver.get(TARGET_URL)
        user_name = 'problem_user'
        password = 'secret_sauce'

        user_name_field = self.driver.find_element(By.ID, 'user-name')
        user_name_field.click()
        user_name_field.send_keys(user_name)

        password_field = self.driver.find_element(By.ID, 'password')
        password_field.click()
        password_field.send_keys(password)

        sign_in = self.driver.find_element(By.ID, 'login-button')
        sign_in.click()

        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/inventory.html', 'Not an expected url')

        add_item = self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        add_item.click()

        cart_link = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        cart_link.click()
        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/cart.html', 'This is not an expected url')
        item_in_cart = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
        item_in_cart_text = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
        self.assertTrue(item_in_cart.is_displayed())
        item_in_cart.click()
        item_in_cart_info = self.driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]').text
        self.assertNotEqual(item_in_cart_text, item_in_cart_info)


    def test_pgu_autorization_and_order(self):
        self.driver.get(TARGET_URL)
        user_name = 'performance_glitch_user'
        password = 'secret_sauce'

        user_name_field = self.driver.find_element(By.ID, 'user-name')
        user_name_field.click()
        user_name_field.send_keys(user_name)

        password_field = self.driver.find_element(By.ID, 'password')
        password_field.click()
        password_field.send_keys(password)

        sign_in = self.driver.find_element(By.ID, 'login-button')
        sign_in.click()

        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/inventory.html', 'Not an expected url')

        inventory_item_4 = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
        inventory_item_4_text = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
        inventory_item_4.click()

        self.assertEqual(self.driver.current_url, f'{TARGET_URL}/inventory-item.html?id=4')
        inventory_item_4_info = self.driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]').text
        self.assertEqual(inventory_item_4_text, inventory_item_4_info, 'Item and description does not match')

        add_item = self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        add_item.click()

        cart_link = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        cart_link.click()

    #     checkout
        checkout = self.driver.find_element(By.ID, 'checkout')
        checkout.click()

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

        continue_button = self.driver.find_element(By.ID, 'continue')
        continue_button.click()

        finish_button = self.driver.find_element(By.ID, 'finish')
        finish_button.click()

        self.assertTrue(self.driver.current_url, f'{TARGET_URL}/checkout-complete.html')


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
