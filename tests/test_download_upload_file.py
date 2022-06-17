import os
import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest
import http.client as httplib

DOWNLOAD_FOLDER_PATH = os.path.join(os.getcwd(), 'Resources', 'Downloads')


class TestDownloadUploadFile(BaseTest):
    """
    Tests for downloading and uploading files.
    ATTN: Must be ran from command line: pytest -v tests/test_download_upload_file.py
    """

    def setUp(self):
        # delete all files form download target folder
        for file in os.listdir(DOWNLOAD_FOLDER_PATH):
            os.remove(os.path.join(DOWNLOAD_FOLDER_PATH, file))
        # initialize browser instance
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        prefs = {'download.default_directory': DOWNLOAD_FOLDER_PATH}
        chrome_options.add_experimental_option('prefs', prefs)
        if 'CICD_RUN' in os.environ:
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 4)

    @pytest.mark.smoke
    def test_download_file_option_1(self):

        expected_downloaded_file_name = 'SampleForJPG.jpg'

        self.driver.get('https://the-internet.herokuapp.com/download')
        self.driver.find_element(By.CSS_SELECTOR, f'a[href="download/{expected_downloaded_file_name}"]').click()

        self.wait.until(lambda d: len(os.listdir(DOWNLOAD_FOLDER_PATH)) > 0)
        files = os.listdir(DOWNLOAD_FOLDER_PATH)
        print(files)
        self.assertTrue(expected_downloaded_file_name in files)
        self.assertEqual(os.path.getsize(os.path.join(DOWNLOAD_FOLDER_PATH, expected_downloaded_file_name)), 95258,
                         'Downloaded file has incorrect size.')

    @pytest.mark.smoke
    def test_download_file_option_2(self):

        self.driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices')
        self.wait.until(EC.element_to_be_clickable((By.ID, 'accept-cookie-notification'))).click()
        self.driver.find_element(By.CSS_SELECTOR, '.icon-csv').click()

        self.wait.until(lambda d: len(os.listdir(DOWNLOAD_FOLDER_PATH)) > 0)
        files = os.listdir(DOWNLOAD_FOLDER_PATH)
        expected_downloaded_file_name = 'BrowserStack - List of devices to test on.csv'
        self.assertTrue(expected_downloaded_file_name in files)
        self.assertEqual(os.path.getsize(os.path.join(DOWNLOAD_FOLDER_PATH, expected_downloaded_file_name)), 3187,
                         'Incorrect downloaded file size.')

    @pytest.mark.smoke
    def test_download_file_link(self):

        self.driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices')

        csv_download_button_el = self.driver.find_element(By.CSS_SELECTOR, '.icon-csv')
        download_url = csv_download_button_el.get_attribute('href')

        connection = httplib.HTTPConnection('browserstack.com')
        connection.request('HEAD', download_url)
        response = connection.getresponse()

        self.assertEqual(response.status, 301)
        self.assertEqual(response.getheader('content-type'), 'text/html')
        self.assertEqual(response.getheader('content-length'), '134')

    @pytest.mark.smoke
    def test_upload(self):

        upload_file_name = 'SampleForJPG.jpg'
        file_path = os.path.join(os.getcwd(), 'Resources', 'FileSample', upload_file_name)

        self.driver.get('https://the-internet.herokuapp.com/upload')
        self.driver.find_element(By.ID, 'file-upload').send_keys(file_path)
        self.driver.find_element(By.ID, 'file-submit').click()

        successful_upload_message = self.wait.until(EC.visibility_of_element_located((By.ID, 'uploaded-files'))).text
        self.assertEqual(successful_upload_message, upload_file_name)


if __name__ == '__main__':
    unittest.main()
