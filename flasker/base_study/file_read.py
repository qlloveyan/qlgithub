#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : file_read.py
# @Author: QUANLI
# @Date  : 2018/9/3 11:14
# @Desc  : 动手写一个文件流式读取

import json

file_path = "C:\\Users\\quanli\\Desktop\\test.py"

print(open(file_path).read())
print("================================")
for line in open(file_path):
    print(line)

users = json.loads(open("C:\\Users\\quanli\\Desktop\\users.json").read())
print(type(users[0].get("age")))

print("2 * 4")
print(eval("2*4"))