#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : blue_print_learn.py
# @Author: QUANLI
# @Date  : 2018/7/11 19:29
# @Desc  : 蓝图学习

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/flasker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Author(object):
    """作者信息表"""
    # 表名称
    __tablename__ = 'TB_AUTHOR'

    # 表字段
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(64), unique = True)

    # 定义属性，以便作者模型可以通过该属性访问多的一方的数据
    # backref 给book也添加一个author的属性，可以通过book.author获取book所对应的作者信息
    books = db.relationship('Book', backref='author')

class Book(object):
    """书籍信息表"""
    # 表名称
    __tablename__ = 'TB_BOOK'

    # 表字段
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(64), unique = True)
    #记录一的一方的id作为外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))

@app.route('/')
def index():
    return "index"

if __name__ == '__main__':
    # 删除数据库表
    db.drop_all()
    # 创建所有的表
    db.create_all()

    author1 = Author(name = u'老王')
    author2 = Author(name = u'张三')

    book1 = Book(name = u'mysql 从删除到跑路', author_id=1)
    book2 = Book(name = u'python 大法好', author_id=1)
    book3 = Book(name = u'颈椎病康复室', author_id=2)
    book4 = Book(name = u'oracle 从删除到跑路', author_id=2)
    book5 = Book(name = u'java从入门到放弃', author_id=2)

    db.add_all(author1)
    db.add_all(author2)
    db.add_all(book1)
    db.add_all(book2)
    db.add_all(book3)
    db.add_all(book4)
    db.add_all(book5)

    app.run(debug=True)