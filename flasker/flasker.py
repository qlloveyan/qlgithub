#-*- coding:utf-8 -*-

import os
import sqlite3
from flask import Flask, request, session, g, url_for, abort, render_template, flash, json, jsonify, redirect
from conn_result import ResultObj
import settings

from db.models import Users, Role
#from publics.self_regrex import PasswordRegexConverter

import publics.self_regrex

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import psycopg2

app = Flask(__name__, static_url_path='/resources', static_folder='static', template_folder='templates')

app.config.from_object(settings.DevConfig)

#注册自定义转换器类
app.url_map.converters['mre'] = publics.self_regrex.PasswordRegexConverter
app.url_map.converters['listre'] = publics.self_regrex.ListConverter

@app.errorhandler(404)
def not_found_page(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error_page(error):
    return render_template('500.html'), 500

@app.route('/index')
def indexPage():
    return 'index'

@app.route('/test_redirect')
def test_redirect():
    return redirect(url_for('indexPage'))

@app.route('/test_regrex/<mre:pass_str>')
def test_regrex(pass_str = None):
    return jsonify({'regex_pass': pass_str})

@app.route('/test_converter/<listre:pass_str>')
def test_param_converter(pass_str=None):
    return "参数：%s" %pass_str

@app.route('/insert', methods=['POST', 'GET'])
def user_add():
    conn = sqlite3.connect('flasker.db')
    cur = conn.cursor()

    userName = request.args['name']
    age = request.args['age']

    sql = 'INSERT INTO TB_USER(USER_NAME, AGE) VALUES (\'%s\', %s)' %(userName ,age)
    cur.execute(sql)
    conn.commit()
    conn.close()
    return json.dumps({
            'name': userName,
            'age': age
        })

@app.route('/service/get_all_users', methods=['GET'])
def get_all_users():
    conn = sqlite3.connect('flasker.db')
    cur = conn.cursor()

    sql = 'SELECT ID, USER_NAME, AGE FROM TB_USER'
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    resultList = []

    for resultTemp in result:
        resultList.append({'id': resultTemp[0],'name': resultTemp[1],'age': resultTemp[2]})
    return json.dumps(resultList)

@app.route("/test_json/<string:name>/<string:password>")
def test_json(name, password):
    """
    :param name:
    :param password:
    :return:

    return jsonify({
        'name': name,
        'password': password
    })
    """
    return jsonify({'name': name, 'password': password})

@app.route('/testpg', methods=['GET'])
def postgre_test():
    if request.method != 'GET':
        return json.dumps({'flag': False, 'descrption': '请求方法不是get请求!'})

    conn = psycopg2.connect(database='testpg', user='postgres', password='123456', host='127.0.0.1', port='5432')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE TB_USER
        (
          ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL
        );''')
    conn.commit()
    conn.close()
    return json.dumps({'flag': True, 'descrption': '数据库 表创建成功!'})

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/flasker')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

@app.route('/test_orm', methods=['POST'])
def orm_test():
    """
    通过flask orm框架做数据库入库处理
    :return: 入库提示json字符串
    """
    print(app.config['MYSQL_DATABASE_URI'])
    username = request.form['userName']
    age = request.form['age']

    session = DBSession()
    new_user = Users(username, age)
    session.add(new_user)
    session.commit()
    print('user id : %s' %new_user.id)
    session.close()
    return json.dumps({'flag': True, 'descrption': 'orm测试成功!'})

""""""
@app.route('/test_relation')
def test_relation():
    session = DBSession()
    user_list = session.query(Users, Role).filter(Users.role_id == Role.id).all()
    for listItem in user_list:
        # print listItem
        print(listItem.Users)
        print(listItem.Role)
    session.close()
    return jsonify({'flag': True})

@app.route('/query_users')
def query_users():
    session = DBSession()
    user_list = session.query(Users).all()
    session.close()
    for i in user_list:
        print(i.serialize)
    return jsonify({'flag': True, 'data': [i.serialize for i in user_list]})


@app.before_request
def before_request():
    print('请求执行!')
    ip = request.remote_addr
    print(ip)

if __name__ == '__main__':
    app.run()