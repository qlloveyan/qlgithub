#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : matplotlib_demo.py
# @Author: QUANLI
# @Date  : 2018/11/1 20:11
# @Desc  : matplotlib学习
import matplotlib.pyplot as plt
import numpy as np

# from matplotlib.font_manager import FontManager
# fonts = set(f.name for f in FontManager().ttflist)
# print ('可用字体:')
# for f in sorted(fonts):
#     print('\t' + f)

# 设置编码中文以及负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = np.arange(10)
plt.plot(data)


# 显示图例
plt.legend(u"数量")
plt.title(u"测试matplotlib使用")

plt.xlabel("x")
plt.ylabel("y")


plt.show()