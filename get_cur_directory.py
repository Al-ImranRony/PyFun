#  Get the base path of Python working directory

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('Base directory: ', BASE_DIR)


# Get the active working directory

# CUR_DIR = os.path.dirname(os.path.realpath(__file__))
CUR_DIR = os.getcwd()
print('Current directory: ', CUR_DIR)