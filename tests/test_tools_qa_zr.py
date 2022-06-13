import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest

BASE_URL = 'https://demoqa.com/'
ELEMENTS_URL = f'{BASE_URL}elements'
FORMS_URL = f'{BASE_URL}forms'
ALERT_FRAMES_WINDOWS_URL = f'{BASE_URL}alertsWindows'
WIDGETS_URL = f'{BASE_URL}widgets'
INTERACTIONS_URL = f'{BASE_URL}interaction'
BOOK_STORE_URL = f'{BASE_URL}books'
SELENIUM_TRAINING_URL = 'https://www.toolsqa.com/selenium-training/'


class TestDemoqaRedirection(BaseTest):
    def setUp(self) -> None:
        super(TestDemoqaRedirection, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 30)

    def test_title_demo_qa(self):
        self.assertEqual(self.driver.title, 'ToolsQA')

    def test_training_link(self):
        selenium_training_banner = self.driver.find_element(By.XPATH, "//img[@class='banner-image']")
        selenium_training_banner.click()
        tabs = self.driver.window_handles
        self.assertEqual(len(tabs), 2, f'Actual number of tabs: {len(tabs)}, expected 2 tabs.')
        self.assertEqual(self.driver.current_url, BASE_URL)
        self.driver.switch_to.window(tabs[1])
        self.assertEqual(self.driver.current_url, SELENIUM_TRAINING_URL)

    def test_elements_url(self):
        self.driver.find_element(By.XPATH, "//div[@class='card-body']/*[text()='Elements']").click()
        self.assertEqual(self.driver.current_url, ELEMENTS_URL)

    def test_forms_url(self):
        self.driver.find_element(By.XPATH, "//div[@class='card-body']/*[text()='Forms']").click()
        self.assertEqual(self.driver.current_url, FORMS_URL)

    def test_alerts_windows_url(self):
        self.driver.find_element(By.XPATH, "//div[@class='card-body']/*[text()='Alerts, Frame & Windows']").click()
        self.assertEqual(self.driver.current_url, ALERT_FRAMES_WINDOWS_URL)

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
