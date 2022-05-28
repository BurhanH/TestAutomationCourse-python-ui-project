import os
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException, NoAlertPresentException, \
    NoSuchElementException

BASE_URL = 'https://demoqa.com/alerts'
INSTANT_ALERT_BUTTON_ID = 'alertButton'
DELAYED_ALERT_BUTTON_ID = 'timerAlertButton'
CONFIRMATION_ALERT_BUTTON_ID = 'confirmButton'
PROMPT_ALERT_BUTTON_ID = 'promtButton'
CONFIRMATION_RESULT_ID = 'confirmResult'
PROMPT_RESULT_ID = 'promptResult'


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
        self.driver.find_element(By.ID, INSTANT_ALERT_BUTTON_ID).click()

        try:
            alert = self.driver.switch_to.alert
        except NoAlertPresentException:
            self.fail('Alert is not present after click on first button.')
        actual_alert_text = alert.text
        expected_alert_text = 'You clicked a button'
        self.assertEqual(actual_alert_text, expected_alert_text,
                         f"Unexpected alert text: '{actual_alert_text}', expected: '{expected_alert_text}'.")

    def test_delayed_alert(self):
        self.driver.find_element(By.ID, DELAYED_ALERT_BUTTON_ID).click()

        start_time = time.time()
        try:
            alert = self.wait.until(EC.alert_is_present())
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
        except TimeoutException:
            self.fail("Delayed alert didn't appear in 10 seconds.")

        actual_alert_text = alert.text
        delay = time.time() - start_time
        expected_alert_text = 'This alert appeared after 5 seconds'
        self.assertEqual(actual_alert_text, expected_alert_text,
                         f"Unexpected alert text: '{actual_alert_text}', expected: '{expected_alert_text}'.")
        self.assertAlmostEqual(delay, 5, delta=0.3, msg=f"Alert appeared in {delay} sec, expected in 5 sec.")

    def test_confirmation_alert_accept(self):
        self.driver.find_element(By.ID, CONFIRMATION_ALERT_BUTTON_ID).click()

        try:
            alert = self.driver.switch_to.alert
        except NoAlertPresentException:
            self.fail('Confirmation alert is not present after click on third button.')
        actual_confirmation_alert_text = alert.text
        expected_alert_text = 'Do you confirm action?'
        self.assertEqual(actual_confirmation_alert_text, expected_alert_text,
                         f"Unexpected alert text: '{actual_confirmation_alert_text}', "
                         f"expected: '{expected_alert_text}'.")

        alert.accept()

        actual_confirmation_result_text = self.driver.find_element(By.ID, CONFIRMATION_RESULT_ID).text
        expected_confirmation_text = 'You selected Ok'
        self.assertEqual(actual_confirmation_result_text, expected_confirmation_text,
                         f"Unexpected confirmation result text: '{actual_confirmation_result_text}', "
                         f"expected: '{expected_confirmation_text}'.")

    def test_confirmation_alert_cancel(self):
        self.driver.find_element(By.ID, CONFIRMATION_ALERT_BUTTON_ID).click()

        try:
            alert = self.driver.switch_to.alert
        except NoAlertPresentException:
            self.fail('Confirmation alert is not present after click on third button.')
        actual_confirmation_alert_text = alert.text
        expected_alert_text = 'Do you confirm action?'
        self.assertEqual(actual_confirmation_alert_text, expected_alert_text,
                         f"Unexpected alert text: '{actual_confirmation_alert_text}', "
                         f"expected: '{expected_alert_text}'.")

        alert.dismiss()

        actual_confirmation_result_text = self.driver.find_element(By.ID, CONFIRMATION_RESULT_ID).text
        expected_confirmation_text = 'You selected Cancel'
        self.assertEqual(actual_confirmation_result_text, expected_confirmation_text,
                         f"Unexpected confirmation result text: '{actual_confirmation_result_text}', "
                         f"expected: '{expected_confirmation_text}'.")

    def test_prompt_alert_cancel(self):
        self.driver.find_element(By.ID, PROMPT_ALERT_BUTTON_ID).click()

        try:
            alert = self.driver.switch_to.alert
        except NoAlertPresentException:
            self.fail('Prompt alert is not present after click on fourth button.')
        actual_prompt_result_text = alert.text
        expected_prompt_result_text = 'Please enter your name'
        self.assertEqual(actual_prompt_result_text, expected_prompt_result_text,
                         f"Unexpected alert text: '{actual_prompt_result_text}', "
                         f"expected: '{expected_prompt_result_text}'.")

        alert.dismiss()
        try:
            prompt_result_text = self.driver.find_element(By.ID, PROMPT_RESULT_ID).text
            self.fail(f"Unexpected text as a result of dismissed prompt alert: '{prompt_result_text}'.")
        except NoSuchElementException:
            pass

    def test_prompt_alert_fill_out_field_cancel(self):
        self.driver.find_element(By.ID, PROMPT_ALERT_BUTTON_ID).click()

        try:
            alert = self.driver.switch_to.alert
        except NoAlertPresentException:
            self.fail('Prompt alert is not present after click on fourth button.')

        alert.send_keys('something!')
        alert.dismiss()
        try:
            prompt_result_text = self.driver.find_element(By.ID, PROMPT_RESULT_ID).text
            self.fail(f"Unexpected text as a result of dismissed prompt alert: '{prompt_result_text}'.")
        except NoSuchElementException:
            pass

    def test_prompt_alert_empty_field_ok(self):
        self.driver.find_element(By.ID, PROMPT_ALERT_BUTTON_ID).click()

        try:
            alert = self.driver.switch_to.alert
        except NoAlertPresentException:
            self.fail('Prompt alert is not present after click on fourth button.')

        alert.accept()
        try:
            prompt_result_text = self.driver.find_element(By.ID, PROMPT_RESULT_ID).text
            self.fail(f"Unexpected text as a result of submitted empty prompt alert: '{prompt_result_text}'.")
        except NoSuchElementException:
            pass

    def test_prompt_alert_fill_out_field_ok(self):
        name = 'Elinor Mcmanus'

        self.driver.find_element(By.ID, PROMPT_ALERT_BUTTON_ID).click()

        try:
            alert = self.driver.switch_to.alert
        except NoAlertPresentException:
            self.fail('Prompt alert is not present after click on fourth button.')

        alert.send_keys(name)
        alert.accept()

        actual_prompt_result_text = self.driver.find_element(By.ID, PROMPT_RESULT_ID).text
        expected_prompt_result_text = f'You entered {name}'
        self.assertEqual(actual_prompt_result_text, expected_prompt_result_text,
                         f"Unexpected prompt result text: '{actual_prompt_result_text}', "
                         f"expected: '{expected_prompt_result_text}'.")


if __name__ == '__main__':
    unittest.main()
