#!/usr/bin/python3

'''
使用python3.5执行
1. 模拟用户登陆
2. 验证用户输入的用户名及密码
3. 同一个用户输错三次锁定用户
4. password.txt读取文件格式为 username,password
'''

import sys
import getpass
import os

#读取用户并验证登陆
def user_list(username,password):
    #需要文件本身就存在
    file_txt = open('password.txt')
    while 1:
        line = file_txt.readline()
        if not line:
            break
        line1 = line.split('\n')[0].split(',')
        if username == line1[0] and password == line1[1]:
            return 'login'
        else:
            print('用户名或密码错误')
        break
    file_txt.close()

#黑名单写入
def write_blacklist(username):
    with open('blacklist.txt','a') as f:
        f.write('%s\n'%username)

#读取黑名单
def Blacklist(username):
    if not os.path.exists(r'blacklist.txt') :
        os.system('touch blacklist.txt')

    with open('blacklist.txt','r+') as f:
        if username in f.read():
            return 'error'

if __name__ == '__main__':
    count = 0
    enter_uesr = []
    while count < 3:
        user = input('请输入用户名: ')
        ent_password = getpass.getpass('请输入密码: ')
        #输入用户名密码后检查黑名单
        if Blacklist(user) == 'error':
            print('%s 用户已经锁定,请联系管理员'%user)
            exit()
        enter_uesr.append(user)
        if user_list(user,ent_password) == 'login':
            print('登陆成功')
            sys.exit(0)

        if count ==2:
            if enter_uesr.count(user) >= 2:
                write_blacklist(user)
                print('%s 用户已经输入三次错误的用户名或者密码,用户名将锁定'%user)
        count += 1


