#-*- coding:utf-8 -*-

import os
import sqlite3
from flask import Flask, request, session   , g, url_for, abort, render_template, flash, json
from conn_result import ResultObj
import jsonify

from db.models import Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import psycopg2

app = Flask(__name__, static_url_path='/resources', static_folder='static', template_folder='templates')

@app.errorhandler(404)
def not_found_page(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found_page(error):
    return render_template('500.html'), 500

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
    return json.dumps({'name': name, 'password': password})

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
    return json.dumps({'flag': True, 'descrption': '数据库表创建成功!'})

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/flasker')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

@app.route('/test_orm', methods=['POST'])
def orm_test():
    username = request.form['userName']
    age = request.form['age']

    session = DBSession()
    new_user = Users(username, age)
    session.add(new_user)
    session.commit()
    session.close()
    return json.dumps({'flag': True, 'descrption': 'orm测试成功!'})


if __name__ == '__main__':
    app.run()