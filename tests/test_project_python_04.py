import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPleeease(unittest.TestCase):

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

    def test_1(self):
        self.driver.get("https://demoqa.com/")
        doc_link = self.driver.find_element(By.XPATH, "//h5[contains(text(),'Forms')]")

        doc_link.click()
        self.assertEqual(self.driver.current_url, "https://demoqa.com/forms")
        #time.sleep(5)



    def tearDown(self) -> None:
        self.driver.close()



if __name__ == '__main__':
    unittest.main()