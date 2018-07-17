#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : about_net.py
# @Author: QUANLI
# @Date  : 2018/7/16 17:01
# @Desc  : 学习python网络相关信息

import whois

whois_result = whois.whois('baidu.com')

for key in whois_result.keys():
    print(key, " : ", whois_result.get(key))