import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestBrowser(unittest.TestCase):
    def setUp(self) -> None:
        """
        Initiate driver for each test
        """
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        if 'CICD_RUN' in os.environ:
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test_navigate_to_google(self) -> None:
        """
        Navigate to Google
        """
        self.driver.get('https://www.google.com')
        self.assertEqual(self.driver.title, 'Google')

    def tearDown(self) -> None:
        """
        Closing driver after each test
        """
        self.driver.quit()

    def test_navigate_to_toolsqa(self) -> None:
        self.driver.get('https://demoqa.com/')
        self.assertEqual(self.driver.title, 'ToolsQA')
        element = self.driver.find_element(By.XPATH, '//div[@class="card mt-4 top-card"][1]')
        element.click()
        actual_result = self.driver.find_element(By.XPATH, "//div[@class='main-header']").text
        expected_result = 'Elements'
        self.assertEqual(expected_result, actual_result)






if __name__ == '__main__':
    unittest.main()

