#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : time_test.py
# @Author: QUANLI
# @Date  : 2018/7/5 10:45
# @Desc  : 测试时间函数运行
import base64
import hashlib
import hmac
from datetime import datetime

"""
print datetime.now().strftime('%Y-%m-%d %H-%M-%S')

print base64.b64encode("123456")
print base64.b64decode("MTIzNDU2")

md5 = hashlib.md5()
md5.update('123456')
print md5.hexdigest()

"""

secerty_pass = hmac.new('123456', '1234567890abcDEF', hashlib.md5)
print secerty_pass.hexdigest()