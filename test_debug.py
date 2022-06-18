import os
import pytest
import seedir as sd
from tests.test_download_upload_file import DOWNLOAD_FOLDER_PATH
from utils.project_utils import get_project_path


def test_debug_dir_structure():
    sd.seedir(os.getcwd())
    print(f"current directory: {os.getcwd()}")
    print(f"DOWNLOAD_FOLDER_PATH: {DOWNLOAD_FOLDER_PATH}")
    resources_folder_path = os.path.join(get_project_path(), 'resources')
    print(f"'resources' folder exists ({resources_folder_path}) : {os.path.exists(resources_folder_path)}")
    downloads_folder_path = os.path.join(get_project_path(), 'resources', 'downloads_folder')
    print(f"'downloads_folder' folder exists  ({downloads_folder_path}) : {os.path.exists(downloads_folder_path)}")


def test_fail():
    assert False
