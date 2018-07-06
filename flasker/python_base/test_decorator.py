#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : test_decorator.py
# @Author: QUANLI
# @Date  : 2018/7/6 10:33
# @Desc  : 测试装饰器模式，模拟csrf防护
import base64
import datetime
import random

g_dict = {'csfr_token': None}

def csrf_decora(func):
    def wrapper(*args, **kw):
        print 'csrf protect begin……'
        csrf_token = g_dict['csfr_token']
        if csrf_token and csrf_token == args[0]:
            print u'csrf 验证通过'
        else:
            print u'csrf 验证失败'

        return func(*args, **kw)
    return wrapper

@csrf_decora
def now(csrf_arg = None):
    print datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    csrf_str = generator_csrf()
    g_dict['csfr_token'] = csrf_str


def generator_csrf():
    string_seed = 'abcdefghijklmnopqrsuvtwxyz1234567890!@#$%^&*()_+=-'
    string_arr = []
    index = 0
    while index < 9 :
        index += 1
        string_arr.append(random.choice(string_seed))
    csrf_str = "".join(string_arr)
    return csrf_str

if __name__ == '__main__':
    #模拟用户初次访问
    now()
    #获取登录crsf_token
    csrf_token = g_dict['csfr_token']
    now(csrf_token)