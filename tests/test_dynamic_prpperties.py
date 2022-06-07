import unittest
from selenium.webdriver.support.wait import WebDriverWait
from utils.base_test import BaseTest

BASE_URL = 'https://demoqa.com/dynamic-properties'
BODY_TEXT_CSS = 'p[id]'
DELAYED_ENABLED_BUTTON_ID = 'enableAfter'
COLOR_CHANGE_BUTTON_ID = 'colorChange'
DELAYED_VISIBLE_BUTTON_ID = 'visibleAfter'


class TestDynamicProperties(BaseTest):

    def setUp(self):
        super(TestDynamicProperties, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 6)

    def test(self):
        # TODO: verify body text
        # TODO: verify first button text
        # TODO: verify first button disabled
        # TODO: verify second button text
        # TODO: verify second button color
        # TODO: verify second button text color
        # TODO: wait for first button to be enabled
        # TODO: wait for second button text color to be RED
        # TODO: verify third button is enabled (so it's visible)
        # TODO: verify third button text
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
