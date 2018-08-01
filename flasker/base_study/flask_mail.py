#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : flask_mail.py
# @Author: QUANLI
# @Date  : 2018/7/24 18:48
# @Desc  : flask-mail发送邮件信息

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = '587'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '731733090@qq.com'
app.config['MAIL_PASSWORD'] = 'rgiwpzlsdrdnbbah'

@app.route('/')
def index():
    return "index"

if __name__ == '__main__':
    mail = Mail(app)
    msg = Message('test subject', sender=app.config['MAIL_USERNAME'], recipients = ['731733090@qq.com'])
    msg.body = 'test body'
    msg.html = '<b>Html </b>'
    with app.app_context():
        mail.send(msg)
    app.run(debug=True)
