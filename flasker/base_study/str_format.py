#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : str_format.py
# @Author: QUANLI
# @Date  : 2018/9/1 11:13
# @Desc  : 字符串格式化
# simple case
print("My name is: %s " %("quanli"))
print("..%(name)-8s.." %{"name": "test"})

# dict format
students = []
student1 = {"name": "quanli", "age": 25, "money": 1002121.21}
student2 = {"name": "zqh", "age": 27, "money": 123423.21}
student3 = {"name": "wxj", "age": 26, "money": 888.21}
student4 = {"name": "ww", "age": 100, "money": 9888.21}
students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)

# students.sort(key=lambda student:student.get("age"), reverse=True)
students = sorted(students, key=lambda student:student.get("age"), reverse=True)

for temp in students:
    print("|name: %(name)-8s |money: %(money)-20.2f| age: %(age)-3d" %temp)

d1 = dict()
d1["name"] = "d1"

d2 = dict()
d2["name"] = "d2"
d2["age"] = 18
d2.update(d1)
print(d2)