import os
import time
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

    def test_navigate_to_toolsQA(self):
        self.driver.get('https://demoqa.com')
        self.assertEqual(self.driver.title, 'ToolsQA')

    def test_logo(self):
        self.driver.get('https://demoqa.com')
        self.driver.find_element(By.XPATH, '(//*[@id="app"]/header/a/img)')

    def test_element_link(self):
        self.driver.get('https://demoqa.com')
        element = self.driver.find_element(By.XPATH, '(/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2])')
        element.click()
        time.sleep(8)
        self.assertEqual(self.driver.current_url, 'https://demoqa.com/elements')

    def test_form_link(self):
        self.driver.get('https://demoqa.com')
        form = self.driver.find_element(By.XPATH, '(//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2])')
        form.click()
        time.sleep(8)
        self.assertEqual(self.driver.current_url, 'https://demoqa.com/forms')

    def test_alerts_link(self):
        self.driver.get('https://demoqa.com')
        alerts = self.driver.find_element(By.XPATH, '(//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[2])')
        alerts.click()
        time.sleep(8)
        self.assertEqual(self.driver.current_url, 'https://demoqa.com/alertsWindows')

    def test_widgets_link(self):
        self.driver.get('https://demoqa.com')
        widgets = self.driver.find_element(By.XPATH, '(//*[@id="app"]/div/div/div[2]/div/div[4]/div/div[2])')
        widgets.click()
        time.sleep(8)
        self.assertEqual(self.driver.current_url, 'https://demoqa.com/widgets')

    def test_interactions_link(self):
        self.driver.get('https://demoqa.com')
        interactions = self.driver.find_element(By.XPATH, '(//*[@id="app"]/div/div/div[2]/div/div[5]/div/div[2])')
        interactions.click()
        time.sleep(8)
        self.assertEqual(self.driver.current_url, 'https://demoqa.com/interaction')

    @unittest.skip ("need fix")
    def test_books_link(self):
        self.driver.get('https://demoqa.com')
        books = self.driver.find_element(By.XPATH, '(//*[@id="app"]/div/div/div[2]/div/div[6]/div/div[2])')
        books.click()
        time.sleep(8)
        self.assertEqual(self.driver.current_url, 'https://demoqa.com/books')

    def tearDown(self) -> None:
        """
        Closing driver after each test
        """
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
