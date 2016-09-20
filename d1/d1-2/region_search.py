#/usr/bin/python3

'''
1. 运行程序输出第一级菜单

2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单

3. 菜单数据保存在文件中

4. 地区写文件中,使用json格式存放
'''

import json

title = '''
***************************************
*                                     *
*     地区查询系统                      *
*                                     *
*                                     *
*                                     *
*                                     *
***************************************
'''
def json1():
    with open('region_list.json','r') as f:
        js = json.load(f)
    return js

#第一层列表
def one(data):

    print(title)
    print('-'*10,'省级目录','-'*10)
    dic_list = {}
    for k,v in enumerate(data[0],1):
        print('%s.%s'%(k,v))
        dic_list[k] = v
    user_enter = input('\n请选择省份,退出请输入q: ').strip()

    #输入数字时判断
    if user_enter.isdigit():
        user_enter = int(user_enter)
        if user_enter in dic_list:
            dic_user = dic_list[user_enter]
            if data[0].get(dic_user,0):
                two(dic_user,data)

    if data[0].get(user_enter,0):
        two(user_enter,data)
    elif user_enter == 'q':exit()
    elif user_enter == 'b':
        print('\n已经在第一层了')
    elif user_enter not in data[0]:
        print('\n省份不存在,请从新输入....')

#第二层列表
def two(name1,data):
    while True:
        print('-'*10,'市级目录','-'*10)
        dic_list = {}
        for k,v in enumerate(data[0][name1],1):
            print('%s.%s'%(k,v))
            dic_list[k] = v

        user_enter = input('\n请选择市,退出请输入q,返回上级目录请按b: ').strip()

        #判断数字
        if user_enter.isdigit():
            user_enter = int(user_enter)
            if user_enter in dic_list:
                dic_user = dic_list[user_enter]
                if data[1].get(dic_user,0):
                    three(name1,dic_user,data)

        if user_enter == 'q':
            exit()
        elif user_enter == 'b':
            one(data)
        elif data[1].get(user_enter,0):

            three(name1,user_enter,data)
        else:
            print('市不存在,请检查输入....')
#第三层列表
def three(name1,name, data):
    while True:
        print('-'*10,'县级乡级目录','-'*10)
        for k,v in enumerate(data[1][name],1):
            print('%s.%s'%(k,v))
        user_enter = input('\n退出请输入q,返回上级目录请按b: ').strip()
        if user_enter == 'q':
            exit()
        elif user_enter == 'b':
            two(name1,data)
        else:
            print('输入有误，请重新输入....')


if __name__ == '__main__':
    js = json1()
    while 1:
        one(js)
