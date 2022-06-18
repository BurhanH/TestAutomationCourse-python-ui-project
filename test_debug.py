import os
import pytest
import seedir as sd

from utils.project_utils import get_project_path


def test_debug_dir_structure():
    sd.seedir(os.getcwd())
    print(f"current directory: {os.getcwd()}")
    print(f"downloads_folder exists: {os.path.exists(os.path.join(get_project_path(), 'resources', 'downloads_folder'))}")


def test_fail():
    assert False
