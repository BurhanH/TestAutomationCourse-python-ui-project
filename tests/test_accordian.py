import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://demoqa.com/accordian'


class TestToolsQAAccordian(BaseTest):
    def setUp(self) -> None:
        super(TestToolsQAAccordian, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 8)

    def test_section_1_link_and_text_appearance(self):
        section_1_text = self.driver.find_element(By.XPATH,"//p[contains(text(),'Lorem Ipsum is simply dummy text')]")
        self.assertTrue(section_1_text.is_displayed())
        self.driver.find_element(By.ID, 'section1Heading').click()

    def test_section_2_link_and_text_appearance(self):
        self.driver.find_element(By.ID, 'section2Heading').click()
        section_2_text = self.driver.find_element(By.XPATH, "//p[contains(text(),'Contrary to popular belief')]")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Contrary to popular belief')]")))
        self.assertTrue(section_2_text.is_displayed())

    def test_section_3_link_and_text_appearance(self):
        self.driver.find_element(By.ID, 'section3Heading').click()
        section_3_text = self.driver.find_element(By.XPATH, "//p[contains(text(), 'It is a long established fact')]")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'It is a long established fact')]")))
        self.assertTrue(section_3_text.is_displayed())


if __name__ == '__main__':
    unittest.main()
