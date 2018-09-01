#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : OOP.py
# @Author: QUANLI
# @Date  : 2018/9/1 17:04
# @Desc  : 设置

class User(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    user1 = User("ql", 27)
    print(user1.__getattribute__("name"))
    user1_dict = user1.__dict__
    print(user1_dict)