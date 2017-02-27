__author__ = "haozhixin"

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from core import master
print(master.content_file('db'))
#
# master.loggin()