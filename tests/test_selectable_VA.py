import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSelectable(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://demoqa.com/selectable')
        self.assertEqual(self.driver.current_url, "https://demoqa.com/selectable")

    def test_selectable_list(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Selectable')]")
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Cras justo odio')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Dapibus ac facilisis in')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Morbi leo risus')]").click()
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Porta ac consectetur ac')]").click()
        self.driver.find_element(By.ID, "demo-tab-grid").click()
        time.sleep(2)

    def test_selectable_grid(self):
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Nine')]")
        self.driver.find_element(By.XPATH, "//li[contains(text(),'Five')]")
        self.driver.find_element(By.XPATH, "//li[contains(text(),'One')]")
        #driver.find_element(By.XPATH, "//img[@alt='Katalon Acedemy']").click() // trying to open this link in the end
        #of this test but it doens't go quite as well as I expect it, need to figure it out
        #time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
    