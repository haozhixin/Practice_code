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
# 查询
def search1(*args):
    '''
    :param args:select * from db where name = tt
    :return:
    {'age': 22, 'phone': 3243254354, 'staff_id': 6, 'name': 'tt', 'dept': 'oo', 'enroll_date': '2017-03-11'}
    共查询到： 1 条信息!
    '''
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
    :param args:add zhixin 23 130427102300 IT
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
            if int(args[0][3]) not in phone_list:
                data_dic['staff_id'] = int(max_id+1)
                data_dic['name'] = str(enter_list[0])
                data_dic['age'] = int(enter_list[1])
                data_dic['phone'] = int(enter_list[2])
                data_dic['dept'] = str(enter_list[3])
                data_dic['enroll_date'] = local_time
                data.append(data_dic)
                print('成功插入一条记录')
            else:
                print('phone 已经存在')
        with open('%s/db.json' % (BASE_DIR + '/dbfile'), 'w') as f:
            json_data = json.dumps(data)
            f.write(json_data+'\n')
    except Exception as e:
        print(e)

# 删除
def delete(id):
    '''
    :param id: del id
    :return:
    '''
    content = content_file('db')
    app_list = []
    try:
        if not isinstance(id, int):
            id = int(id)
        for i in content:
            if i['staff_id'] == id:
                print('删除的内容如下: \n%s'%i)
            else:
                app_list.append(i)
        with open('%s/db.json' % (BASE_DIR + '/dbfile'), 'w') as f:
            json_data = json.dumps(app_list)
            f.write(json_data)
    except Exception as e:
        print(e)


def update(*args):
    '''UPDATE staff_table SET dept="Market" where dept = "IT"'''
    db_date = content_file('db')
    enter_list = args[0]
    if len(enter_list) == 6:
        if enter_list[1] == 'db' and enter_list[2] == 'set' and enter_list[4] == 'where':
            search_condition = enter_list[5].split('=')
            change_con = enter_list[3].split('=')
            new_data = []
            for i in db_date:
                j = i[search_condition[0]]
                enter_value = search_condition[1]
                if enter_value.isdigit():
                    enter_value = int(enter_value)
                if type(j) == str and j.isdigit():
                    j = int(j)
                if j == enter_value and change_con[0] in i.keys():
                    i[change_con[0]] = change_con[1]
                new_data.append(i)
            with open('%s/db.json' % (BASE_DIR + '/dbfile'), 'w') as f:
                json_data = json.dumps(new_data)
                f.write(json_data + '\n')

# if __name__ == '__main__':
#     while True:
#         enter = input("(staff)>>> ").strip().split()
#         # enter = raw_input("(staff)>>> ").split()
#         if enter:
#             if enter[0] == 'exit':
#                 exit()
#             elif enter[0] == 'select' and enter[2] == 'from':
#                 message = search1(enter)
#             elif enter[0] == 'add':
#                 add(enter)
#             elif enter[0] == 'del':
#                 id_own = enter[1]
#                 delete(id_own)
#             elif enter[0] == 'update':
#                 update(enter)


