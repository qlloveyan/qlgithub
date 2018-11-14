#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : thread_example_pool.py
# @Author: QUANLI
# @Date  : 2018/11/13 18:28
# @Desc  : 线程池的概念

"""
线程池与 multiprocess多线程的区别, 线程池可返回对象值
"""

import multiprocessing as mp

def job(x):
    return x * x

def pool_test():
    # 可以通过processes参数指定使用几个系统内核
    pool = mp.Pool(processes=2)
    result_map = pool.map(job, range(10000000))
    print(result_map)

if __name__ == "__main__":
    pool_test()