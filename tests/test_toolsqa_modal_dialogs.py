import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils.base_test import BaseTest

BASE_URL = 'https://demoqa.com/modal-dialogs'

SMALL_MODAL_BUTTON_ID = 'showSmallModal'
SMALL_MODAL_CLOSE_BUTTON_ID = 'closeSmallModal'
SMALL_MODAL_TITLE_ID = 'example-modal-sizes-title-sm'
MODAL_BODY_CLASS = 'modal-body'
MODAL_CLOSE_X_BUTTON_CLASS = 'close'
LARGE_MODAL_BUTTON_ID = 'showLargeModal'
LARGE_MODAL_CLOSE_BUTTON_ID = 'closeLargeModal'
LARGE_MODAL_TITLE_ID = 'example-modal-sizes-title-lg'


class TestToolsQAModalDialogs(BaseTest):
    def setUp(self):
        super(TestToolsQAModalDialogs, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

    def wait_modal_to_load(self):
        # wait until presence an element on the DOM
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role=dialog]')))

    def test_verify_buttons_names_not_equal(self):
        small_button_text = self.driver.find_element(By.ID, SMALL_MODAL_BUTTON_ID).text
        large_button_text = self.driver.find_element(By.ID, LARGE_MODAL_BUTTON_ID).text

        self.assertNotEqual(small_button_text, large_button_text,
                            f"Buttons names suppose to be different, but first button name: '{small_button_text}', "
                            f"second button name: '{large_button_text}'.")

    def test_small_modal_dialog(self):
        self.driver.find_element(By.ID, SMALL_MODAL_BUTTON_ID).click()

        self.wait_modal_to_load()
        expected_modal_title_text = "Small Modal"
        actual_modal_title_text = self.driver.find_element(By.ID, SMALL_MODAL_TITLE_ID).text

        self.assertEqual(expected_modal_title_text, actual_modal_title_text,
                         f"Unexpected title: '{actual_modal_title_text}', "
                         f"expected: '{expected_modal_title_text}'.")

    def test_large_modal_dialog(self):
        self.driver.find_element(By.ID, LARGE_MODAL_BUTTON_ID).click()

        self.wait_modal_to_load()
        expected_modal_title_text = "Large Modal"
        actual_modal_title_text = self.driver.find_element(By.ID, LARGE_MODAL_TITLE_ID).text

        self.assertEqual(expected_modal_title_text, actual_modal_title_text,
                         f"Unexpected title: '{actual_modal_title_text}', "
                         f"expected: '{expected_modal_title_text}'.")

    def test_small_modal_close_by_x(self):
        self.driver.find_element(By.ID, SMALL_MODAL_BUTTON_ID).click()

        self.wait_modal_to_load()
        expected_modal_title_text = "Small Modal"
        modal_title = self.driver.find_element(By.ID, SMALL_MODAL_TITLE_ID)
        actual_modal_title_text = modal_title.text

        self.assertEqual(expected_modal_title_text, actual_modal_title_text,
                         f"Unexpected title: '{actual_modal_title_text}', "
                         f"expected: '{expected_modal_title_text}'.")

        self.driver.find_element(By.CLASS_NAME, MODAL_CLOSE_X_BUTTON_CLASS).click()

        self.wait.until(EC.staleness_of(modal_title))
        try:
            actual_text = self.driver.find_element(By.ID, SMALL_MODAL_TITLE_ID).text
            self.fail(f"Modal dialog should be closed, but modal dialog title was received: '{actual_text}'.")
        except NoSuchElementException:
            pass

    def test_large_modal_close_by_x(self):
        self.driver.find_element(By.ID, LARGE_MODAL_BUTTON_ID).click()

        self.wait_modal_to_load()
        expected_modal_title_text = "Large Modal"
        modal_title = self.driver.find_element(By.ID, LARGE_MODAL_TITLE_ID)
        actual_modal_title_text = modal_title.text

        self.assertEqual(expected_modal_title_text, actual_modal_title_text,
                         f"Unexpected title: '{actual_modal_title_text}', "
                         f"expected: '{expected_modal_title_text}'.")

        self.driver.find_element(By.CLASS_NAME, MODAL_CLOSE_X_BUTTON_CLASS).click()

        self.wait.until(EC.staleness_of(modal_title))
        try:
            actual_text = self.driver.find_element(By.ID, LARGE_MODAL_TITLE_ID).text
            self.fail(f"Modal dialog should be closed, but modal dialog title was received: '{actual_text}'.")
        except NoSuchElementException:
            pass

    def test_small_modal_close_by_button(self):
        self.driver.find_element(By.ID, SMALL_MODAL_BUTTON_ID).click()

        self.wait_modal_to_load()
        expected_modal_title_text = "Small Modal"
        modal_title = self.driver.find_element(By.ID, SMALL_MODAL_TITLE_ID)
        actual_modal_title_text = modal_title.text

        self.assertEqual(expected_modal_title_text, actual_modal_title_text,
                         f"Unexpected title: '{actual_modal_title_text}', "
                         f"expected: '{expected_modal_title_text}'.")

        self.driver.find_element(By.ID, SMALL_MODAL_CLOSE_BUTTON_ID).click()

        self.wait.until(EC.staleness_of(modal_title))
        try:
            actual_text = self.driver.find_element(By.ID, SMALL_MODAL_TITLE_ID).text
            self.fail(f"Modal dialog should be closed, but modal dialog title was received: '{actual_text}'.")
        except NoSuchElementException:
            pass

    def test_large_modal_close_by_button(self):
        self.driver.find_element(By.ID, LARGE_MODAL_BUTTON_ID).click()

        self.wait_modal_to_load()
        expected_modal_title_text = "Large Modal"
        modal_title = self.driver.find_element(By.ID, LARGE_MODAL_TITLE_ID)
        actual_modal_title_text = modal_title.text

        self.assertEqual(expected_modal_title_text, actual_modal_title_text,
                         f"Unexpected title: '{actual_modal_title_text}', "
                         f"expected: '{expected_modal_title_text}'.")

        self.driver.find_element(By.ID, LARGE_MODAL_CLOSE_BUTTON_ID).click()

        self.wait.until(EC.staleness_of(modal_title))
        try:
            actual_text = self.driver.find_element(By.ID, LARGE_MODAL_TITLE_ID).text
            self.fail(f"Modal dialog should be closed, but modal dialog title was received: '{actual_text}'.")
        except NoSuchElementException:
            pass


if __name__ == '__main__':
    unittest.main()
