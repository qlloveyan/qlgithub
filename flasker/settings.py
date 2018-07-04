#-*- coding:utf-8 -*-
class Config(object):
    debug = False
    MYSQL_DATABASE_URI = 'mysql+mysqlconnector://root:123456@localhost:3306/flasker'

class DevConfig(Config):
    debug = True
    MYSQL_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flasker'