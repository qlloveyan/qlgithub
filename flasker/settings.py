#-*- coding:utf-8 -*-
class Config(object):
    # 基本配置信息
    debug = False
    MYSQL_DATABASE_URI = 'mysql+mysqlconnector://root:123456@localhost:3306/flasker'

class DevConfig(Config):
    # 本地开发环境配置
    # 本地开发环境配置
    debug = True
    MYSQL_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flasker'

class TestConfig(Config):
    # 测试环境配置信息
    debug = False
    MYSQL_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flasker'
