import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.screenshot_utils import save_screenshot


class BaseTest(unittest.TestCase):
    def setUp(self, url=None):
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        if 'CICD_RUN' in os.environ:
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        if url:
            self.driver.get(url)
        else:
            raise RuntimeError('Error: url is not defined')

    def tearDown(self):
        for method, error in self._outcome.errors:
            if error:
                save_screenshot(self.driver, self.id())
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
