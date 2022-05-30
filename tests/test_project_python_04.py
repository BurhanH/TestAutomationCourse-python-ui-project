import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPleeease(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

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