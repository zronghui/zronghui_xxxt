#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 2:39 PM
# @Author  : zhangronghui
# @File    : qq邮件发送.py
# @Software: PyCharm
from __future__ import print_function
import argparse
import smtplib
import subprocess  # Python 2中，将subprocess替换为commands
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from config import qq_mail_pass as my_pass

my_sender = '825503975@qq.com'
# my_user = '825503975@qq.com'
to_reciver = ['825503975@qq.com']
# my_pass = ''

def mail(MyName, head, content, to=to_reciver, _type = 'html'):
    assert _type in ['plain', 'html']
    try:
        msg = MIMEText(content, _type, 'utf-8')
        msg['From'] = formataddr((MyName, my_sender))
        # msg['To'] = formataddr(("", my_user))
        if isinstance(to_reciver, list):
            msg['To'] = ';'.join(to_reciver)
        elif isinstance(to_reciver, str):
            msg['To'] = to_reciver
        msg['Subject'] = head

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, to_reciver, msg.as_string())
        server.quit()
    except Exception as e:
        print('[error!]', e)


def getTime(seconds):
    from datetime import datetime, timedelta
    sec = timedelta(seconds=seconds)
    d = datetime(1, 1, 1) + sec
    return "%dh %dmin %dsec" % (d.hour, d.minute, d.second)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--command', required=True)
    args = parser.parse_args()
    start = time.time()
    status, result = subprocess.getstatusoutput(args.command)
    end = time.time()
    if not status:
        mail(args.command, args.command + '执行成功', 'run for ' + getTime(end - start))
    else:
        mail(args.command, args.command + '执行失败', result)
