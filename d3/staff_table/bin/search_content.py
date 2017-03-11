__author__ = "haozhixin"

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from core.master import *

while True:
    enter = input("(staff)>>> ").strip().split()
    if enter:
        if enter[0] == 'exit':
            exit()
        elif enter[0] == 'select' and enter[2] == 'from':
            message = search1(enter)
        elif enter[0] == 'add':
            add(enter)
        elif enter[0] == 'del':
            id_own = enter[1]
            delete(id_own)
        elif enter[0] == 'update':
            update(enter)
