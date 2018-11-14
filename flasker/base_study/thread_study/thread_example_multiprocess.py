#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : thread_example.py
# @Author: QUANLI
# @Date  : 2018/11/13 17:59
# @Desc  : 多线程学习

import multiprocessing as mp

def job(q, a, b):
    """
    :param a:
    :param b:
    :return:
    """
    print("a: %s , b: %s" %(a, b))
    q.put(a+b)

def job2(q, c):
    """
    :param a:
    :param b:
    :return:
    """
    print("value in queue: %s , c: %s" %(q.get(), c))
    q.put(q.get() * c)

if __name__ == "__main__":
    """
    本例中采用的实现方式, 需要在主函数中加载进程启动,否则会报错
    """

    # 进程之间参数传递, 需要用Queue进行参数传递
    value_queue = mp.Queue()
    my_thread = mp.Process(target=job, args=(value_queue, 1, 2))
    my_thread2 = mp.Process(target=job2, args=(value_queue, 3))
    my_thread.start()
    my_thread2.start()
    my_thread.join()
    my_thread2.join()
    print("last value is : %s" %(value_queue.get()))