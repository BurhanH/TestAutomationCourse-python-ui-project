import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestBrowser(unittest.TestCase):
    def setUp(self) -> None:
        """
        Initiate driver for each test
        """
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

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


if __name__ == '__main__':
    unittest.main()
