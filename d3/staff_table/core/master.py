#_*_coding:utf-8_*_
import json
import os, sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def content_file(table_name):
    try:
        with open('%s/%s.json' % (BASE_DIR + '/dbfile', table_name), 'r') as f:
            data = json.load(f)
            return data
    except :
         return 'error'

def like(table_name, date):
    content = content_file(table_name)
    if content[7].startswith(date):
        print(content)


# 查询命令
def search(*args):
    for i in args:
        if len(i) <= 8:
            data = content_file(i[3])
            print(data)
            if data == 'error':
                print('Database Not Find')
                break
            if i[1] == '*':
                ahb = ['id', 'age', 'phone', 'dept', 'enroll_date']
            else:
                ahb = i[1].split(',')
            dict_name = {}
            try:
                for k, v in data.items():
                    if i[6] == '>':
                        if v[i[5]] > int(i[7]):
                            for j in ahb:
                                dict_name[j] = v[j]
                            yield 'name: %s, message: %s' % (k, dict_name)
                    if i[6] == '<':
                        if v[i[5]] < int(i[7]):
                            for j in ahb:
                                dict_name[j] = v[j]
                            yield 'name: %s, message: %s' % (k, dict_name)
                    if i[6] == '=':
                        if isinstance(i[7], str):
                            if i[7].isdigit():
                                i[7] = int(i[7])
                        if v[i[5]] == i[7]:
                            for j in ahb:
                                dict_name[j] = v[j]
                            yield 'name: %s, message: %s' % (k, dict_name)


            except Exception as e:
                print('error %s'%e)
        else:
            print('输入有误，请重新输入')

# 查询命令
def search1(*args):
    for i in args:
        if len(i) <= 8:
            data = content_file(i[3])
            if data == 'error':
                print('Database Not Find')
                break
            if i[1] == '*':
                ahb = ['staff_id' ,'name', 'age', 'phone', 'dept', 'enroll_date']
            else:
                ahb = i[1].split(',')
            dict_name = {}
            try:
                number_count=0
                for data_dic in data:
                    for z in ahb:
                        dict_name[z] = data_dic[z]
                    if len(i) > 4 and i[4] == 'where':
                        if len(i) >= 5 and i[5] :
                            if i[6] == '=':
                                if data_dic[i[5]] == i[7]:
                                    print (dict_name)
                                    number_count+=1
                            elif i[6] == '>':
                                if data_dic[i[5]] > i[7]:
                                    print (dict_name)
                                    number_count+=1
                    elif len(i) > 4 and i[4] != 'where':
                        print('输入有误请从新输入')
                        break
                    else:
                        print (dict_name)
                        number_count+=1
                print('''共查询到：\033[31;1m %s \033[0m条信息!\n'''%number_count)


            except Exception as e:
                print('error %s'%e)
        else:
            print('输入有误，请重新输入')

# 增加
def add(*args):
    data = content_file('db')
    phone_list = [x['phone'] for x in data]
    print(phone_list)

if __name__ == '__main__':
    while True:
        enter = input("(staff)>>> ").strip().split()
        if enter:
            if enter[0] == 'exit':
                exit()
            elif enter[0] == 'select' and enter[2] == 'from':
                message = search1(enter)
                # if enter[4] and enter[4] == 'where':
            elif enter[0] == 'add':
                add('aa')


            #elif enter[6] == 'like':
            #    print('like')
            #    like(enter[3], enter[7])

