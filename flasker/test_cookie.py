#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : test_cookie.py
# @Author: QUANLI
# @Date  : 2018/7/5 17:42
# @Desc  : 测试cookie使用设置
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    user_name = request.cookies.get('userName')
    print user_name
    return "index"

@app.route('/login')
def login():
    """默认判断账号和密码正确"""
    response = make_response('success')
    response.set_cookie('userName', 'wangwu', max_age=60)
    return response

if __name__ == '__main__':
    app.run(debug=True)
