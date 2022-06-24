import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest
from selenium.webdriver import ActionChains

BASE_URL = 'https://demoqa.com'
ELEMENTS_URL = f'{BASE_URL}/elements'
TEXT_BOX_URL = f'{BASE_URL}/text-box'
CHECKBOX_URL = f'{BASE_URL}/checkbox'
RADIOBUTTON_URL = f'{BASE_URL}/radio-button'
WEBTABLES_URL = f'{BASE_URL}/webtables'
BUTTONS_URL = f'{BASE_URL}/buttons'
LINKS_URL = f'{BASE_URL}/links'
DOWNLOAD_URL = f'{BASE_URL}/upload-download'


class TestDemoqaRedirection(BaseTest):
    def setUp(self) -> None:
        super(TestDemoqaRedirection, self).setUp(ELEMENTS_URL)
        self.wait = WebDriverWait(self.driver, 7)

    def test_textbox_element(self):
        user_name = 'Full Name'
        email = 'fullname@gmail.com'
        current_address = '2222 S Fairy Ave'
        permanent_address = '1111 E Exposition Ave'

        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Text Box')]").click()
        self.assertEqual(self.driver.current_url, TEXT_BOX_URL)
        self.driver.find_element(By.ID, 'userName').send_keys(user_name)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        self.driver.find_element(By.ID, 'currentAddress').send_keys(current_address)
        self.driver.find_element(By.ID, 'permanentAddress').send_keys(permanent_address)
        self.driver.find_element(By.ID, 'submit').click()

        actual_result_name = self.driver.find_element(By.XPATH, "//p[@id='name']").text
        expected_result_name = f'Name:{user_name}'
        self.assertEqual(expected_result_name, actual_result_name)

        actual_result_email = self.driver.find_element(By.XPATH, "//p[@id='email']").text
        expected_result_email = f'Email:{email}'
        self.assertEqual(expected_result_email, actual_result_email)

        actual_result_current_address = self.driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
        expected_result_current_address = f'Current Address :{current_address}'
        self.assertEqual(expected_result_current_address, actual_result_current_address)

        actual_result_permanent_address = self.driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text
        expected_result_permanent_address = f'Permananet Address :{permanent_address}'
        self.assertEqual(expected_result_permanent_address, actual_result_permanent_address)

    def test_checkbox_element(self):
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Check Box')]").click()
        self.assertEqual(self.driver.current_url, CHECKBOX_URL)
        home_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, 'tree-node-home')))
        self.assertFalse(home_checkbox.is_selected())
        self.driver.find_element(By.CSS_SELECTOR, 'label[for=tree-node-home] span.rct-checkbox').click()
        self.assertTrue(home_checkbox.is_selected())

    def test_radio_button_element(self):
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Radio Button')]").click()
        self.assertEqual(self.driver.current_url, RADIOBUTTON_URL)
        yes_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#yesRadio")))
        self.assertFalse(yes_button.is_selected())
        self.driver.find_element(By.XPATH, "//input[@id='yesRadio']//following-sibling::label").click()
        self.assertTrue(yes_button.is_selected())
        impressive_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#impressiveRadio")))
        self.assertFalse(impressive_button.is_selected())
        self.driver.find_element(By.XPATH, "//input[@id='impressiveRadio']//following-sibling::label").click()
        self.assertTrue(impressive_button.is_selected())
        no_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#noRadio")))
        self.assertFalse(no_button.is_enabled())

    def test_web_tables_element(self):
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Web Tables')]").click()
        self.assertEqual(self.driver.current_url, WEBTABLES_URL)
        rows_el = self.driver.find_elements(By.CSS_SELECTOR, 'div.rt-tbody  [role=row]')
        row_count = 0
        for element in rows_el:
            if element.text.strip():
                row_count += 1
        self.assertEqual(row_count, 3, 'Record have not been added.')
        self.driver.find_element(By.CSS_SELECTOR, "#addNewRecordButton").click()
        actual_result_regform = self.driver.find_element(By.XPATH,
                                                         "//div/*[contains(text(), 'Registration Form')]").text
        self.assertEqual('Registration Form', actual_result_regform)
        first_name = 'Larisa'
        last_name = 'Larisa'
        email = 'larisa@ggg.tj'
        age = '55'
        salary = '120'
        department = 'IT'
        self.driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "#age").send_keys(age)
        self.driver.find_element(By.CSS_SELECTOR, "#salary").send_keys(salary)
        self.driver.find_element(By.CSS_SELECTOR, "#department").send_keys(department)
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        rows_el = self.driver.find_elements(By.CSS_SELECTOR, 'div.rt-tbody  [role=row]')
        row_count = 0
        for element in rows_el:
            print(f'text: "{element.text}"')
            if element.text.strip():
                row_count += 1
        self.assertEqual(row_count, 4, 'Record have not been added.')

    def test_buttons_element(self):
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Buttons')]").click()
        self.assertEqual(self.driver.current_url, BUTTONS_URL)
        a_chains = ActionChains(self.driver)
        double_click_button = self.driver.find_element(By.CSS_SELECTOR, '#doubleClickBtn')
        a_chains.double_click(double_click_button).perform()
        actual_result = self.driver.find_element(By.CSS_SELECTOR, '#doubleClickMessage').text
        self.assertEqual('You have done a double click', actual_result)
        right_click_button = self.driver.find_element(By.CSS_SELECTOR, '#rightClickBtn')
        a_chains.context_click(right_click_button).perform()
        actual_result = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#rightClickMessage'))).text
        self.assertEqual('You have done a right click', actual_result)

    def test_links(self):
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Links')]").click()
        self.assertEqual(self.driver.current_url, LINKS_URL)
        self.driver.find_element(By.CSS_SELECTOR, "#created").click()
        actual_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#linkResponse'))).text
        self.assertEqual('Link has responded with staus 201 and status text Created', actual_text)

    def test_download(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Upload and Download')]").click()
        self.assertEqual(self.driver.current_url, DOWNLOAD_URL)
        self.driver.find_element(By.CSS_SELECTOR, "#downloadButton").click()


if __name__ == '__main__':
    unittest.main()
