#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : tushare_test.py
# @Author: QUANLI
# @Date  : 2018/10/12 10:42
# @Desc  : 测试tushare的使用,范例：https://mp.weixin.qq.com/s/Nn9y8CySS7mgxGwqQ3Hb5A

import tushare as ts

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 基本用法，根据股票代码，打印基本信息
# print(ts.get_hist_data('600848'))

# 股票涨跌信息做可视化
df = ts.get_hist_data(code='000001', start='2018-10-01', end='2018-10-12') # DataFrame
df.head(10)

sz = df.sort_index(axis=0 ,ascending=True)
sz_return = sz[['p_change']]
train=sz_return[0:255]
test=sz_return[255:]
plt.figure(figsize=(10,5))
train['p_change'].plot()
plt.legend(loc='best')
plt.show()
plt.figure(figsize=(10,5))
test['p_change'].plot(color='red')
plt.legend(loc='best')
plt.show()