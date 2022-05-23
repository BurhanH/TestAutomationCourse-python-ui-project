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
        chrome_options = webdriver.ChromeOptions()
        # --disable-gpu;
        # --no-sandbox;
        # --disable-dev-shm-usage;
        # --headless;
        # --window-size=1920,1080
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


if __name__ == '__main__':
    unittest.main()
