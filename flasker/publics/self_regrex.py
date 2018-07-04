#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : self_regex.py
# @Author: QUANLI
# @Date  : 2018/7/4 17:49
# @Desc  : 自定义正则表达式匹配
from werkzeug.routing import BaseConverter

class PasswordRegexConverter(BaseConverter):
    regex = '[0-9a-zA-Z]+'

class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split(',')