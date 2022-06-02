import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from utils.base_test import BaseTest

URL = 'https://demoqa.com/alerts'
INSTANT_ALERT_BUTTON_ID = 'alertButton'
CONFIRMATION_ALERT_BUTTON_ID = 'confirmButton'
CONFIRMATION_RESULT_ID = 'confirmResult'


class TestToolsQAAlerts(BaseTest):
    def setUp(self):
        super().setUp()
        self.driver.get(URL)

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


if __name__ == '__main__':
    unittest.main()
