#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : python_reflex.py
# @Author: QUANLI
# @Date  : 2018/8/3 15:00
# @Desc  : python 反射机制学习

class TestClass(object):

    def tesFun(self):
        print("测试")


def min_length_check(self, min_length, check_value):
    if len(check_value) < min_length:
        return False


if __name__ == '__main__':
    # dd = __import__("base_study.python_reflex", fromlist=True)
    # check_value = input('请输入密码：')
    # f = getattr(dd, "min_length_check", None)
    # print(f(f, 6, check_value))

    tc = getattr(TestClass(), "tesFun")
    tc()
