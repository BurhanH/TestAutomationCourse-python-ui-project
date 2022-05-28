import os
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException, NoAlertPresentException

BASE_URL = 'https://demoqa.com/alerts'


class TestToolsQAAlerts(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        if 'CICD_RUN' in os.environ:
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.find_element(By.ID, 'alertButton').click()

        try:
            alert = self.driver.switch_to.alert
        except NoAlertPresentException:
            self.fail('Alert is not present after click on first button.')
        actual_alert_text = alert.text
        expected_alert_text = 'You clicked a button'
        self.assertEqual(actual_alert_text, expected_alert_text,
                         f"Unexpected alert text: '{actual_alert_text}', expected: '{expected_alert_text}'.")

    def test_delayed_alert(self):
        self.driver.find_element(By.ID, 'timerAlertButton').click()

        start_time = time.time()
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
        except TimeoutException:
            self.fail("Delayed alert didn't appear in 10 seconds.")
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
        actual_alert_text = alert.text
        delay = time.time() - start_time
        expected_alert_text = 'This alert appeared after 5 seconds'
        self.assertEqual(actual_alert_text, expected_alert_text,
                         f"Unexpected alert text: '{actual_alert_text}', expected: '{expected_alert_text}'.")
        self.assertAlmostEqual(delay, 5, delta=0.3, msg=f"Alert appeared in {delay} sec, expected in 5 sec.")

    @unittest.skip('TODO')
    def test_confirmation_alert(self):
        pass

    @unittest.skip('TODO')
    def test_prompt_alert(self):
        pass


if __name__ == '__main__':
    unittest.main()
