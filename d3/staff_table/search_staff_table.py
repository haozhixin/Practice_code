#_*_ coding:utf-8 _*_

import json
import os

with open('staff_table.json', 'r') as f:
    data = json.load(f)


def search_age(age):
    for k,v in data.items():
        if v['age'] > age:
            yield 'name: %s, message: %s'%(k,v)


message = search_age(22)
# print(message)
# for i in message:
#     print(i)
# print(os.path.dirname(os.path.abspath(__file__)))
# if __name__ == '__main__':
# 	while True:
# 		enter = input("(staff)>>>").strip()
# 		if enter == 'exit':
# 			exit()

import shutil

f1 = open('file_name.py')
f2 = open('file_new.py','w')
shutil.copyfileobj(f1,f2)