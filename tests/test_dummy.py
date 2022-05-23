import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.service import Service


class TestBrowser(unittest.TestCase):
    def setUp(self) -> None:
        """
        Initiate driver for each test
        """
        service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        chrome_options = Options()
        options = [
            "--headless",
            "--disable-gpu",
            "--window-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
        for option in options:
            chrome_options.add_argument(option)
        
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


if __name__ == '__main__':
    unittest.main()
