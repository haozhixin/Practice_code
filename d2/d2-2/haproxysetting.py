#!/usr/bin/python3

import json
import os
import time


'''
HA proxy配置文件操作
1. 根据用户输入输出对应的backend下的server信息
2. 可添加backend 和sever信息
3. 可修改backend 和sever信息
4. 可删除backend 和sever信息
5. 操作配置文件前进行备份
6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
'''

option = '''
1. 获取ha记录
2. 增加ha记录
3. 删除ha记录
4. 退出(按q)
'''


def search(webadd):
    status = False
    fetch_list = []
    with open('haproxy.conf', 'r', encoding='utf-8') as f:
        for line in f:
            con = line.strip()
            if con == "backend %s"%webadd:
                status = True
                continue
            if con.startswith('backend'):
                status = False
            if status and con:
                fetch_list.append(con)
    return fetch_list


# 格式化输入字符串
def par(content):
    try:
        init = json.loads(content)
        webadd_title, server_title = init['backend'], init['record']
        web = search(webadd_title)
        return webadd_title, server_title, web
    except Exception as e:
        print(e)
        return 'error'


def add(add_content):
    new_time = time.strftime("%Y%m%d%H%M%S")
    init = par(add_content)
    if init == 'error':
        print('\033[31;1m请检查输入....\033[0m')
    else:
        webadd_title, server_title, web = init[0], init[1], init[2]
        server_content = "server {server} {server} weight {weight} maxconn {max}".format(
            server=server_title['server'], weight=server_title['weight'], max=server_title['maxconn'])
        if web:
            web_list = []
            for i in web:
                a = i.split()
                web_list.append(a[1])
            flag = False
            bi = True
            ai = True
            with open('haproxy.conf', 'r') as read_file, open('haproxy.bak', 'w') as write_file:
                for line in read_file:
                    if line.strip() == "backend %s"% webadd_title:
                        write_file.write(line)
                        flag = True
                        continue
                    if flag and line.startswith('backend'):
                        flag = False

                    if flag and line.strip():
                        line_list = line.split()
                        if line_list[1] == server_title['server']:
                            if ai and bi:
                                new_str = line.replace(line, "%s%s\n" % (' '*8, server_content))
                                write_file.write(new_str)

                                ai = False
                        else:
                            write_file.write(line)
                            if bi and ai:
                                write_file.write("%s%s\n" %(' '*8, server_content))
                                bi = False
                    else:
                        write_file.write(line)

        else:
            with open('haproxy.conf', 'r') as read_file, open('haproxy.bak', 'w') as write_file:
                for line in read_file:
                    write_file.write(line)
                write_file.write("\n\nbackend %s" % webadd_title)
                write_file.write("\n%s %s" % (' '*7, server_content))

        if os.path.isfile('haproxy.bak'):
            os.rename('haproxy.conf','haproxy.conf.%s'% new_time)
            os.rename('haproxy.bak','haproxy.conf')


def delete(del_content):
    init = par(del_content)
    if init == 'error':
        print('\033[31;1m请检查输入....\033[0m')
    else:
        webadd_title, server_title, web = init[0], init[1], init[2]
        server_content = "server {server} {server} weight {weight} maxconn {max}".format(
            server=server_title['server'], weight=server_title['weight'], max=server_title['maxconn'])

    web_title = search(webadd_title)
    if web_title:
        if server_content in web_title:
            web_title.remove(server_content)
        else:
            print("您删除的内容不存在")
            return
        with open('haproxy.conf', 'r', encoding='utf-8') as read_file, \
                open('haproxy.conf.bak', 'w', encoding='utf-8')as write_file:
            flag = False
            bi = False
            for line in read_file:
                if line.strip() == "backend %s" % webadd_title:
                    write_file.write(line)
                    flag = True
                    continue
                if flag and line.startswith('backend'):
                    flag = False

                if flag:
                    if not bi:
                        print(web_title)
                        for new_line in web_title:
                            write_file.write("%s%s\n" % (" "*8,new_line))
                        bi = True
                else:
                    write_file.write(line)

        if os.path.isfile('haproxy.conf.bak'):
            os.rename('haproxy.conf','haproxy.conf.2016')
            os.rename('haproxy.conf.bak','haproxy.conf')


if __name__ == "__main__":
    while True:
        print(option)
        input_enter = input("请输入编号: ").strip()
        message = '%s格式为: {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}'
        if input_enter == '1':
            web_add = input("请输入backend: ").strip()
            server = search(web_add)
            if server:
                for i in server:
                    print('\033[32;1m%s\033[0m'%i)
            else:
                print('\033[31;1m没有这条记录\033[0m')

        elif input_enter == '2':
            print(message%'添加')
            add_content = input("请输入添加内容: ").strip()
            add(add_content)

        elif input_enter == '3':
            print(message%'删除')
            del_content = input("请输入删除内容: ").strip()
            delete(del_content)

        elif input_enter == '4' or input_enter == 'q':
            print('谢谢使用')
            exit()
        else:
            print('输入错误,退出')




