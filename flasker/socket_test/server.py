#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : server.py
# @Author: QUANLI
# @Date  : 2018/7/5 11:59
# @Desc  : 服务端示例代码
import socket
import threading
import time
from multiprocessing import Process

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定IP端口
server.bind(('127.0.0.1', 8080))
server.listen(5)
print 'Server created ! Waiting for connection……'

def read_client_msg(sock, addr):
    """
    读取客户端传递过来的消息
    """
    print 'Access new connection from %s:%s...' %addr
    sock.send('Welcome connection……')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello , %s' % data.decode('utf-8')).encode("utf-8"))
    sock.close()
    print 'Connection from %s' %addr

while True:
    sock, addr = server.accept()
    t = threading.Thread(target=read_client_msg, args=(sock, addr))
    t.start()
    t.join()