#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : smtp_test.py
# @Author: QUANLI
# @Date  : 2018/7/5 16:26
# @Desc  : SMTP邮件协议发送邮件测试类
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from_addr = '13026148179@163.com'
from_pass = 'qlloveyan3279'

to_addr = '731733090@qq.com'

smtp_server = 'smtp.163.com'

msg = MIMEText('测试 Python code auto send……', 'plain', 'utf-8')
msg['Subject'] = Header('python smtp 测试', 'utf-8')
msg['From'] = from_addr
msg['To'] = to_addr

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, from_pass)
server.sendmail(from_addr, [to_addr], msg.as_string())