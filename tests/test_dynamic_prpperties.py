import unittest
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils.base_test import BaseTest

BASE_URL = 'https://demoqa.com/dynamic-properties'
BODY_TEXT_CSS = 'p[id]'
LATER_ENABLED_BUTTON_ID = 'enableAfter'
LATER_ENABLED_BUTTON_LABEL = 'Will enable 5 seconds'
COLOR_CHANGE_BUTTON_ID = 'colorChange'
COLOR_CHANGE_BUTTON_LABEL = 'Color Change'
DELAYED_VISIBLE_BUTTON_ID = 'visibleAfter'
WHITE = 'rgba(255, 255, 255, 1)'
RED = 'rgba(220, 53, 69, 1)'


class TestDynamicProperties(BaseTest):

    def setUp(self):
        super(TestDynamicProperties, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 6)

    @pytest.mark.toolsqa
    @pytest.mark.smoke
    def test_page_elements(self):
        # verify text above buttons
        main_area_text_el = self.driver.find_element(By.CSS_SELECTOR, BODY_TEXT_CSS)
        self.assertTrue(main_area_text_el.is_displayed(), 'Text in main page area is not shown.')
        self.assertEqual(main_area_text_el.text, 'This text has random Id',
                         'Incorrect text on page main area above buttons.')

        # verify first button disabled
        first_button_el = self.driver.find_element(By.ID, LATER_ENABLED_BUTTON_ID)
        self.assertFalse(first_button_el.is_enabled(),
                         'First button is enabled right after page loaded, must be disabled.')

        # verify first button label
        self.assertEqual(first_button_el.text, LATER_ENABLED_BUTTON_LABEL, 'Incorrect first button label.')

        # verify second button is visible and label
        second_button_el = self.driver.find_element(By.ID, COLOR_CHANGE_BUTTON_ID)
        self.assertTrue(second_button_el.is_displayed(), 'Second button is not visible.')
        self.assertEqual(second_button_el.text, COLOR_CHANGE_BUTTON_LABEL, 'Incorrect second button label.')

        # verify second button label color is white
        self.assertEqual(second_button_el.value_of_css_property('color'), WHITE,
                         f'Incorrect second button label color right after page loaded, expected red({WHITE}).')

        # verify no third button
        try:
            if self.driver.find_element(By.ID, DELAYED_VISIBLE_BUTTON_ID).is_displayed():
                self.fail('Third button is displayed right after page loaded.')
        except NoSuchElementException:
            pass

        # verify first button becomes enabled within 5 sec
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(first_button_el),
                                            'First button has not been enabled after 5 seconds.')

        # verify second button label color changed to red
        WebDriverWait(self.driver, 1).until(lambda d: second_button_el.value_of_css_property('color') == RED,
                                            f'Second button label color did not change to red ({RED}).')

        # verify third button is visible and label
        third_button_el = self.driver.find_element(By.ID, DELAYED_VISIBLE_BUTTON_ID)
        self.assertTrue(third_button_el.is_displayed(), 'Third button is not shown.')
        self.assertEqual(third_button_el.text, 'Visible After 5 Seconds', 'Incorrect third button label.')


if __name__ == '__main__':
    unittest.main()
