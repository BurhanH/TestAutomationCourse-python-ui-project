import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest
from selenium.webdriver import ActionChains
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = 'https://demoqa.com/elements'
TEXT_BOX_URL = 'https://demoqa.com/text-box'
CHECKBOX_URL = 'https://demoqa.com/checkbox'
RADIOBUTTON_URL = 'https://demoqa.com/radio-button'
WEBTABLES_URL = 'https://demoqa.com/webtables'
BUTTONS_URL = 'https://demoqa.com/buttons'
LINKS_URL = 'https://demoqa.com/links'
DOWNLOAD_URL = 'https://demoqa.com/upload-download'

class TestDemoqaRedirection(BaseTest):
    def setUp(self) -> None:
        super(TestDemoqaRedirection, self).setUp(BASE_URL)
        self.wait = WebDriverWait(self.driver, 7)

    def test_textbox_element(self):
        user_name = 'Full Name'
        email = 'fullname@gmail.com'
        current_address = '2222 S Fairy Ave'
        permanent_address = '1111 E Exposition Ave'
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Text Box')]").click()
        self.assertEqual(self.driver.current_url, TEXT_BOX_URL)
        name_box = self.driver.find_element(By.ID, 'userName')
        name_box.click()
        name_box.send_keys(user_name)
        email_box = self.driver.find_element(By.ID, "userEmail")
        email_box.click()
        email_box.send_keys(email)
        current_address_box = self.driver.find_element(By.ID, 'currentAddress')
        current_address_box.click()
        current_address_box.send_keys(current_address)
        permanent_address_box = self.driver.find_element(By.ID, 'permanentAddress')
        permanent_address_box.click()
        permanent_address_box.send_keys(permanent_address)
        self.driver.find_element(By.ID, 'submit').click()
        actual_result_name = self.driver.find_element(By.XPATH, "//p[@id='name']").text
        expected_result_name = f'Name:{user_name}'
        actual_result_email = self.driver.find_element(By.XPATH, "//p[@id='email']").text
        expected_result_email = f'Email:{email}'
        actual_result_current_address = self.driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
        expected_result_current_address = f'Current Address :{current_address}'
        actual_result_permanent_address = self.driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text
        expected_result_permanent_address = f'Permananet Address :{permanent_address}'
        self.assertEqual(expected_result_name, actual_result_name)
        self.assertEqual(expected_result_email, actual_result_email)
        self.assertEqual(expected_result_current_address, actual_result_current_address)
        self.assertEqual(expected_result_permanent_address, actual_result_permanent_address)

    def test_checkbox_element(self):
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Check Box')]").click()
        self.assertEqual(self.driver.current_url, CHECKBOX_URL)
        home_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, 'tree-node-home')))
        self.assertFalse(home_checkbox.is_selected())
        self.driver.find_elegment(By.CSS_SELECTOR, 'label[for=tree-node-home] span.rct-checkbox').click()
        self.assertTrue(home_checkbox.is_selected())


    def test_radio_button_element(self):
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Radio Button')]").click()
        self.assertEqual(self.driver.current_url, RADIOBUTTON_URL)
        yes_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#yesRadio")))
        self.assertFalse(yes_button.is_selected())
        yes_element = self.driver.find_element(By.XPATH, "//input[@id='yesRadio']//following-sibling::label")
        yes_element.click()
        self.assertTrue(yes_button.is_selected())
        impressive_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#impressiveRadio")))
        self.assertFalse(impressive_button.is_selected())
        impressive_element = self.driver.find_element(By.XPATH, "//input[@id='impressiveRadio']//following-sibling::label")
        impressive_element.click()
        self.assertTrue(impressive_button.is_selected())
        no_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#noRadio")))
        if no_button.is_enabled():
            print("the button is enable")
        else:
            print("the button is disable")
        self.assertFalse(no_button.is_enabled())


    def test_web_tables_element(self):
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Web Tables')]").click()
        self.assertEqual(self.driver.current_url, WEBTABLES_URL)
        rows_el = self.driver.find_elements(By.CSS_SELECTOR, 'div.rt-tbody  [role=row]')
        row_count = 0
        for element in rows_el:
            print(f'text: "{element.text}"')
            if element.text.strip():
                row_count += 1
        self.assertEqual(row_count, 3, 'Record have not been added.')
        self.driver.find_element(By.CSS_SELECTOR, "#addNewRecordButton").click()
        actual_result_regform = self.driver.find_element(By.XPATH, "//div/*[contains(text(), 'Registration Form')]").text
        self.assertEqual('Registration Form', actual_result_regform)
        first_name = 'Larisa'
        last_name = 'Larisa'
        email = 'larisa@ggg.tj'
        age = '55'
        salary = '120'
        department = 'IT'
        input_first_name = self.driver.find_element(By.CSS_SELECTOR, "#firstName")
        input_first_name.send_keys(first_name)
        input_last_name = self.driver.find_element(By.CSS_SELECTOR, "#lastName")
        input_last_name.send_keys(last_name)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "#userEmail")
        input_email.send_keys(email)
        input_age = self.driver.find_element(By.CSS_SELECTOR, "#age")
        input_age.send_keys(age)
        input_salary = self.driver.find_element(By.CSS_SELECTOR, "#salary")
        input_salary.send_keys(salary)
        input_department = self.driver.find_element(By.CSS_SELECTOR, "#department")
        input_department.send_keys(department)
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
        self.driver.find_element(By.XPATH, "//div[@class='header-wrapper']/*[text()='Elements']").click()
        chrome_options = Options()
        p = {'download.default_directory': 'C:\\Users\\Desktop'}
        chrome_options.add_experimental_option('prefs', p)
        self.driver.execute_script("window.scrollBy(0,925)", "")
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Upload and Download')]").click()
        self.assertEqual(self.driver.current_url, DOWNLOAD_URL)
        self.driver.find_element(By.CSS_SELECTOR, "#downloadButton").click()
        while not os.path.exists('C:\\Users\\Desktop'):
            time.sleep(2)
        # check file
        if os.path.isfile('C:\\Users\\Desktop\\sampleFile (1).jpeg'):
            print("File download is completed")
        else:
            print("File download is not completed")










if __name__ == '__main__':
    unittest.main()
