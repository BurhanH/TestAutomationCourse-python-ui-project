import unittest
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest

BASE_URL = 'https://demoqa.com/nestedframes'


class TestToolsQANestedFrames(BaseTest):
    def setUp(self):
        super(TestToolsQANestedFrames, self).setUp(BASE_URL)

    def test_nested_frames(self):
        main_frame = self.driver.find_element(By.ID, 'frame1')
        self.driver.switch_to.frame(main_frame)
        main_frame_body = self.driver.find_element(By.TAG_NAME, 'body')
        self.assertEqual(main_frame_body.text, 'Parent frame', 'Incorrect text in parent frame.')
        nested_frame = self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(nested_frame)
        nested_frame_body = self.driver.find_element(By.TAG_NAME, 'body')
        self.assertEqual(nested_frame_body.text, 'Child Iframe', 'Incorrect text in child frame.')


if __name__ == '__main__':
    unittest.main()
