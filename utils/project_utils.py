import os
from resources.data import PROJECT_NAME


def get_project_path():
    return os.getcwd().split(PROJECT_NAME)[0] + PROJECT_NAME

