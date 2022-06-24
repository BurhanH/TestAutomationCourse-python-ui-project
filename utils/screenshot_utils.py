import os
from datetime import datetime
from utils.project_utils import get_project_path


def save_screenshot(driver, test_case_id):
    project_path = get_project_path()
    folder_name = 'screenshots'
    screenshots_folder_path = os.path.join(project_path, folder_name)
    if not os.path.exists(screenshots_folder_path):
        if os.getcwd() != project_path:
            os.chdir(project_path)
        os.mkdir(folder_name)
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_file_path = os.path.join(screenshots_folder_path, f'{test_case_id}_{now}.png')
    driver.get_screenshot_as_file(screenshot_file_path)
