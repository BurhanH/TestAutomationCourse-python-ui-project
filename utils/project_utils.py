import os
from resources.data import PROJECT_NAME


def get_project_path():
    cwd = os.getcwd()
    # local setup
    if cwd.count(PROJECT_NAME) == 1:
        return os.path.join(cwd.split(PROJECT_NAME)[0], PROJECT_NAME)
    # GutHub Actions setup
    else:
        return os.path.join(cwd.split(PROJECT_NAME)[0], PROJECT_NAME, PROJECT_NAME)
