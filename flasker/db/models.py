#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : models.py
# @Author: QUANLI
# @Date  : 2018/7/4 10:17
# @Desc  : 数据库实体映射

from sqlalchemy import Column, String,Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

class Users(Base):

    def __init__(self, userName=None, age=None):
        self.user_name = userName
        self.age = age

    #表名称
    __tablename__ = 'TB_USERS'

    #表字段
    id = Column('ID', Integer, primary_key=True, nullable=False, autoincrement=True)
    user_name = Column('USER_NAME', String(50))
    age = Column('AGE', Integer)

