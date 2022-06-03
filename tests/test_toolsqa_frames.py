import unittest
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest

BASE_URL = 'https://demoqa.com/frames'
FRAME_TEXT = 'This is a sample page'
FRAME_FONT_SIZE = '32px'
BLACK = 'rgba(0, 0, 0, 1)'
GRAY = 'rgba(169, 169, 169, 1)'
FRAME_1_SIZE = {'height': 350, 'width': 500}
FRAME_2_SIZE = {'height': 100, 'width': 100}



class TestToolsQAFrames(BaseTest):
    def setUp(self):
        self._setUp(BASE_URL)

    def test_frames(self):
        # Test first iframe content, style, and size
        first_frame = self.driver.find_element(By.ID, 'frame1')
        actual_first_frame_size = first_frame.size
        self.driver.switch_to.frame(first_frame)
        first_frame_text_el = self.driver.find_element(By.ID, 'sampleHeading')
        self.assertEqual(first_frame_text_el.text, FRAME_TEXT, 'Incorrect text in first iframe.')
        self.assertEqual(first_frame_text_el.value_of_css_property('font-size'), FRAME_FONT_SIZE,
                         'Incorrect text size in first iframe.')
        self.assertEqual(first_frame_text_el.value_of_css_property('color'), BLACK,
                         'Incorrect text color in first iframe.')
        self.assertEqual(actual_first_frame_size, FRAME_1_SIZE, 'Incorrect size of first iframe.')
        self.assertEqual(self.driver.find_element('tag name', 'body').value_of_css_property('background-color'),
                         GRAY, 'Incorrect background color in first iframe.')

        self.driver.switch_to.default_content()

        # Test second iframe content, style, and size
        second_frame = self.driver.find_element(By.ID, 'frame2')
        actual_second_frame_size = second_frame.size
        self.driver.switch_to.frame(second_frame)
        second_frame_text_el = self.driver.find_element(By.ID, 'sampleHeading')
        self.assertEqual(second_frame_text_el.text, FRAME_TEXT, 'Incorrect text in second iframe.')
        self.assertEqual(second_frame_text_el.value_of_css_property('font-size'), FRAME_FONT_SIZE,
                         'Incorrect text size in second iframe.')
        self.assertEqual(second_frame_text_el.value_of_css_property('color'), BLACK,
                         'Incorrect text color in second iframe.')
        self.assertEqual(actual_second_frame_size, FRAME_2_SIZE, 'Incorrect size of second iframe.')
        self.assertEqual(self.driver.find_element('tag name', 'body').value_of_css_property('background-color'),
                         GRAY, 'Incorrect background color in second iframe.')


if __name__ == '__main__':
    unittest.main()
