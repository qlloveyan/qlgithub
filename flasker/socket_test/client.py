#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : client.py
# @Author: QUANLI
# @Date  : 2018/7/5 11:59
# @Desc  : 客户端示例代码
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
client.connect(('127.0.0.1', 8080))
#获取服务器端传值
print client.recv(1024).decode('utf-8')

for data in ['zhangsan', 'wangwu', 'lisi']:
    client.send(data)
    print client.recv(1024).decode('utf-8')
client.send('Bye……')
client.close()