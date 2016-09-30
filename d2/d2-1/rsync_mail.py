#!/usr/bin/python
#_*_ coding:utf-8 _*_

'''
1. 当rsync同步报错后，发邮件通知
2. 邮件内容为'具体报错信息'
3. rsync同步停止后,重新启动同步
'''

import os
import smtplib
from email.mime.text import MIMEText
import logging
import time
import subprocess
now_time = time.strftime('%Y-%m-%d %H:%M:%S')

mail_list = ['xxxx@xxx.com']

def log_info(filename):
    logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=filename,
        filemode='a')
    return logging

stdout_info = log_info('rsync.log')


def send_mail(to_list,sub,content):
    mail_host="smtp.xxx.com"             #设置服务器
    mail_user="xxx@xxx.com"    #用户名
    mail_pass="123345"                         #口令
    me=mail_user
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

def rsync_cmd(SRC,DEST):
    r_cmd = subprocess.Popen('/usr/bin/rsync -apzvrPtl {SRC} {DEST}'.format(SRC=SRC,DEST=DEST),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    for line in r_cmd.stdout:
        stdout_info.info(line.strip())

    if r_cmd.stderr:
        cmd = "ps -ef|grep rsync|grep -v rsync_mail.py|grep -v grep|grep -v rsync.log"
        rsync_status = os.system(cmd)
        rsync_res = os.popen(cmd).read()
        with open('rsync_error.log','w+') as errorfile:
            for error_line in r_cmd.stderr:
                stdout_info.warn(error_line.strip())
                errorfile.write("%s %s"%(now_time,error_line))
            if rsync_status:
                errorfile.write('%s %s \n rsync is exit'%(now_time,rsync_res))
            else:
                errorfile.write('%s %s \n rsync is not exit'%(now_time,rsync_res))

        with open('rsync_error.log','r') as f:

            for mailto in mail_list:
                if send_mail(mailto,'rsync 报错日志', f.read()):
                    stdout_info.info("%s,邮件发送成功"%mailto)
                else:
                    stdout_info.info("%s,邮件发送失败"%mailto)
        if rsync_res:
            return True
        else:
            return False




if __name__ == '__main__':
    src_path = '/home/zzz/backup2'
    dest_path = '/home/zzz/backup1'
    while rsync_cmd(src_path,dest_path) == False:
        rsync_cmd(src_path,dest_path)

