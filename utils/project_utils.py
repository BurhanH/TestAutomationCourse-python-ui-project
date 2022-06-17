import os
import sys


def get_delimiter():
    if sys.platform == 'win32':
        return r'\\'
    else:
        return '/'


def get_project_path():
    return get_delimiter().join(os.getcwd().split(get_delimiter())[:-1])
