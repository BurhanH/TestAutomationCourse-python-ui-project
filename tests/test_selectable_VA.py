import time
import unittest
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--start-maximized")

BASE_URL = 'https://demoqa.com/selectable'


class TestSelectable(BaseTest):
    def setUp(self) -> None:
        self._setUp(BASE_URL)
        self.assertEqual(self.driver.current_url, "https://demoqa.com/selectable")

    def test_selectable_header_is_displayed(self):
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, "main-header"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[contains(text(),'Selectable')]"))

    def test_selectable_list_is_displayed(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Selectable')]")
        demo_tab_list = self.driver.find_element(By.ID, "demo-tab-list")
        self.assertTrue(demo_tab_list.is_displayed())

    def test_selectable_text_is_displayed(self):
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Cras justo odio')]").is_displayed()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Cras justo odio')]").click()

        self.driver.find_element(By.XPATH, "//li[contains(text(),'Dapibus ac facilisis in')]").is_displayed()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Dapibus ac facilisis in')]").click()

        self.driver.find_element(By.XPATH, "//li[contains(text(),'Morbi leo risus')]").is_displayed()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Morbi leo risus')]").click()

        self.driver.find_element(By.XPATH, "//li[contains(text(),'Porta ac consectetur ac')]").is_displayed()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Porta ac consectetur ac')]").click()

    def test_grid_is_displayed(self):
        demo_tab_grid = self.driver.find_element(By.ID, "demo-tab-grid")
        self.assertTrue(demo_tab_grid.is_displayed())

    def test_selectable_grid(self):
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Nine')]").is_displayed()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Five')]").is_displayed()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'One')]").is_displayed()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()