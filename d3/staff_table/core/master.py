#_*_coding:utf-8_*_
import json
import os, sys
import time


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
    '''
    add zhixin 23 130427102300 IT
    :param args:
    :return:
    '''
    local_time = time.strftime("%Y-%m-%d")
    data_dic = {
        "staff_id": int(),
        "name": "",
        "age": int(),
        "phone": int(),
        "dept": "",
        "enroll_date": ""
    }
    data = content_file('db')
    phone_list = [x['phone'] for x in data]
    max_id = max([x['staff_id'] for x in data])
    enter_list = args[0][1:]
    try:
        if len(enter_list) == 4:
            print(enter_list)
            if args not in phone_list:
                data_dic['staff_id'] = int(max_id+1)
                data_dic['name'] = str(enter_list[0])
                data_dic['age'] = int(enter_list[1])
                data_dic['phone'] = int(enter_list[2])
                data_dic['dept'] = str(enter_list[3])
                data_dic['enroll_date'] = local_time
                data.append(data_dic)
        print(data)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        enter = input("(staff)>>> ").strip().split()
        # enter = raw_input("(staff)>>> ").split()
        if enter:
            if enter[0] == 'exit':
                exit()
            elif enter[0] == 'select' and enter[2] == 'from':
                message = search1(enter)
            elif enter[0] == 'add':
                add(enter)


            #elif enter[6] == 'like':
            #    print('like')
            #    like(enter[3], enter[7])

