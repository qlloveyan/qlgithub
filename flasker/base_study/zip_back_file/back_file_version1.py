#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : back_file_version1.py
# @Author: QUANLI
# @Date  : 2018/7/17 10:36
# @Desc  : zip文件夹备份重要文件

import os
import time

# 1.指定需要备份的文件夹地址
source_path = ['E:/test_path/source']

backup_path = 'E:/test_path/backup'

backup = backup_path + os.sep + time.strftime('%Y-%m-%d_%H-%M-%S') + '.zip'

zip_command = 'zip -r {0} {1}'.format(backup, ''.join(source_path))

print('zip command is: {0}'.format(zip_command))
print('Running……')
try:
    if os.system(zip_command) == 0:
        print('Successful running……')
    else:
        print('Backup failed!')
except Exception as e:
    print(e)
