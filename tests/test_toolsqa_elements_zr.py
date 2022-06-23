import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest

BASE_URL = 'https://demoqa.com/elements'
TEXT_BOX_URL = 'https://demoqa.com/text-box'
CHECKBOX_URL ='https://demoqa.com/checkbox'

class TestDemoqaRedirection(BaseTest):
    def setUp(self) -> None:
        super(TestDemoqaRedirection, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 7)

    def test_textbox_element(self):
        user_name = 'Full Name'
        email = 'fullname@gmail.com'
        current_address = '2222 S Fairy Ave'
        permanent_address = '1111 E Exposition Ave'
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Text Box')]").click()
        self.assertEqual(self.driver.current_url, TEXT_BOX_URL)
        name_box = self.driver.find_element(By.ID, 'userName')
        name_box.click()
        name_box.send_keys(user_name)
        email_box = self.driver.find_element(By.ID, "userEmail")
        email_box.click()
        email_box.send_keys(email)
        current_address_box = self.driver.find_element(By.ID, 'currentAddress')
        current_address_box.click()
        current_address_box.send_keys(current_address)
        permanent_address_box = self.driver.find_element(By.ID, 'permanentAddress')
        permanent_address_box.click()
        permanent_address_box.send_keys(permanent_address)
        self.driver.find_element(By.ID, 'submit').click()
        actual_result_name = self.driver.find_element(By.XPATH, "//p[@id='name']").text
        expected_result_name = f'Name:{user_name}'
        actual_result_email = self.driver.find_element(By.XPATH, "//p[@id='email']").text
        expected_result_email = f'Email:{email}'
        actual_result_current_address = self.driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
        expected_result_current_address = f'Current Address :{current_address}'
        actual_result_permanent_address = self.driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text
        expected_result_permanent_address = f'Permananet Address :{permanent_address}'
        self.assertEqual(expected_result_name, actual_result_name)
        self.assertEqual(expected_result_email, actual_result_email)
        self.assertEqual(expected_result_current_address, actual_result_current_address)
        self.assertEqual(expected_result_permanent_address, actual_result_permanent_address)

    def test_checkbox_element(self):
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Check Box')]").click()
        self.assertEqual(self.driver.current_url, CHECKBOX_URL)
        home_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, 'tree-node-home')))
        self.assertFalse(home_checkbox.is_selected())
        self.driver.find_elegment(By.CSS_SELECTOR, 'label[for=tree-node-home] span.rct-checkbox').click()
        self.assertTrue(home_checkbox.is_selected())






if __name__ == '__main__':
    unittest.main()