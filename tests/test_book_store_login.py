import time
import unittest
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--start-maximized")

BASE_URL = 'https://demoqa.com/login'
url_after_login = 'https://demoqa.com/profile'
url_after_logout = BASE_URL
username_id = 'userName'
username = 'Lucifer'
password_id = 'password'
password = 'Abcd1234!'
login_button_id = 'login'
log_out_button_xpath = "//button[contains(text(),'Log out')]"
error_message_1 = 'Wrong url'
error_message_2 = 'Unexpected color'


class TestBookStoreLogin(BaseTest):
    def setUp(self) -> None:
        super(TestBookStoreLogin, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

    @pytest.mark.smoke
    def test_log_in_E2E(self):
        self.assertEqual(self.driver.current_url, "https://demoqa.com/login", error_message_1)
        welcoming_message = self.driver.find_element(By.XPATH, "//h5[contains(text(),'Login in Book Store')]")
        self.assertTrue(welcoming_message.is_displayed())

        self.driver.find_element(By.ID, username_id).send_keys(username)
        self.driver.find_element(By.ID, password_id).send_keys(password)
        self.driver.find_element(By.ID, login_button_id).click()

        self.wait.until(EC.url_to_be(url_after_login))
        self.assertEqual(self.driver.current_url, url_after_login, error_message_1)

        profile_header = self.driver.find_element(By.XPATH, "//div[contains(text(),'Profile')]")
        self.assertEqual(profile_header.value_of_css_property('color'), 'rgba(170, 170, 170, 1)', error_message_2 )

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#userName-value')))
        uname_profile = self.driver.find_element(By.CSS_SELECTOR, '#userName-value')
        self.assertEqual(uname_profile.value_of_css_property('color'), 'rgba(0, 0, 0, 1)', error_message_2)

        log_out = self.driver.find_element(By.XPATH, log_out_button_xpath)
        self.assertEqual(log_out.value_of_css_property('background-color'), 'rgba(0, 123, 255, 1)', error_message_2)
        log_out.click()

        self.wait.until(EC.url_to_be(BASE_URL))
        self.assertEqual(self.driver.current_url, BASE_URL, error_message_1)


if __name__ == '__main__':
    unittest.main()