import unittest
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest

class TestPleeease(BaseTest):

    def setUp(self) -> None:
        super(TestToolsQANavigation, self).setUp("https://demoqa.com/")

    def test_1(self):
        doc_link = self.driver.find_element(By.XPATH, "//h5[contains(text(),'Forms')]")

        doc_link.click()
        self.assertEqual(self.driver.current_url, "https://demoqa.com/forms")


if __name__ == '__main__':
    unittest.main()
