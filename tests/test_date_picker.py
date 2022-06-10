import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utils.base_test import BaseTest

BASE_URL = 'https://demoqa.com/date-picker'


class TestToolsQADatePicker(BaseTest):
    def setUp(self) -> None:
        super(TestToolsQADatePicker, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

    def test_select_date_picking(self):
        self.driver.find_element(By.ID, 'datePickerMonthYearInput').click()  # opens datepicker
        self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]').click()
        select_month = Select(self.driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]'))
        select_month.select_by_visible_text('January')
        self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").click()
        self.driver.find_element(By.XPATH, '//option[@value="2021"]').click()
        self.driver.find_element(By.XPATH, '//*[@aria-label="Choose Friday, January 1st, 2021"]').click()

        actual_result = self.driver.find_element(By.ID, 'datePickerMonthYearInput').get_property('value')
        expected_result = '01/01/2021'

        self.assertEqual(expected_result, actual_result, 'Entered date is not as shown!')


if __name__ == '__main__':
    unittest.main()
