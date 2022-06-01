import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://demoqa.com/'
ELEMENTS_URL = 'https://demoqa.com/elements'
FORMS_URL = 'https://demoqa.com/forms'
ALERT_FRAMS_WINDOWS_URL = 'https://demoqa.com/alertsWindows'
WIDGETS_URL = 'https://demoqa.com/widgets'
INTERACTIONS_URL = 'https://demoqa.com/interaction'
BOOK_STORE_URL = 'https://demoqa.com/books'

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
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get(BASE_URL)

    def tearDown(self) -> None:
        """
        Closing driver after each test
        """
        self.driver.quit()

    def test_title_demo_qa(self):
        self.assertEqual(self.driver.title, 'ToolsQA')

    def test_registration_link(self):
        element = self.driver.find_element(By.XPATH, "//img[@class='banner-image']")
        element.click()
        tabs = self.driver.window_handles
        self.assertEqual(len(tabs), 2, f'Actual number of tabs: {len(tabs)}, expected 2 tabs.')
        self.assertEqual(self.driver.current_url, BASE_URL)
        self.driver.switch_to.window(tabs[1])
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='tools-qa-header__logo']")))
        # self.assertEqual(self.driver.title, 'Tools QA - Selenium Training')

    def test_elements_url(self):
        self.driver.find_element(By.XPATH, "//div[@class='card-body']/*[text()='Elements']").click()
        self.assertEqual(self.driver.current_url, ELEMENTS_URL)

    def test_forms_url(self):
        self.driver.find_element(By.XPATH, "//div[@class='card-body']/*[text()='Forms']").click()
        self.assertEqual(self.driver.current_url, FORMS_URL)

    def test_alerts_windows_url(self):
        self.driver.find_element(By.XPATH, "//div[@class='card-body']/*[text()='Alerts, Frame & Windows']").click()
        self.assertEqual(self.driver.current_url, ALERT_FRAMS_WINDOWS_URL)

    def test_widgets_url(self):
        self.driver.find_element(By.XPATH, "//div[@class='card-body']/*[text()='Widgets']").click()
        self.assertEqual(self.driver.current_url, WIDGETS_URL)

    def test_interaction_url(self):
        self.driver.find_element(By.XPATH, "//div[@class='card-body']/*[text()='Interactions']").click()
        self.assertEqual(self.driver.current_url, INTERACTIONS_URL)

    def test_books_store_url(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//div[@class='card-body']/*[text()='Book Store Application']").click()
        self.assertEqual(self.driver.current_url, BOOK_STORE_URL)

if __name__ == '__main__':
    unittest.main()
