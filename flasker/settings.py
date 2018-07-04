#-*- coding:utf-8 -*-
class Config(object):
    DEBUG = True
    DATABASE_URI = 'defaultDb.db'

class DevConfig(Config):
    DATABASE_URI = 'flasker.db'