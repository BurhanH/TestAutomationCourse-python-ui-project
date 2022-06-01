import os
import sys
from datetime import datetime


def get_delimiter():
    if sys.platform == 'win32':
        return r'\\'
    else:
        return '/'


def save_screenshot(driver, test_case_id):
    project_path = os.path.abspath(os.getcwd())
    delimiter = get_delimiter()
    folder_name = 'screenshots'
    screenshots_folder_path = f'{project_path}{delimiter}{folder_name}'
    if not os.path.exists(screenshots_folder_path):
        os.mkdir(folder_name)
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_file_path = f'{screenshots_folder_path}{delimiter}{test_case_id}_{now}.png'
    driver.get_screenshot_as_file(screenshot_file_path)
