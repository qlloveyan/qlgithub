#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : blue_print_learn.py
# @Author: QUANLI
# @Date  : 2018/7/11 19:29
# @Desc  : 蓝图学习

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flasker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Author(db.Model):

    def __init__(self, name):
        self.name = name

    """作者信息表"""
    # 表名称
    __tablename__ = 'TB_AUTHOR'

    # 表字段
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(64), unique = True)

    # 定义属性，以便作者模型可以通过该属性访问多的一方的数据
    # backref 给book也添加一个author的属性，可以通过book.author获取book所对应的作者信息
    books = db.relationship('Book', backref='author')

class Book(db.Model):

    def __init__(self, name, author_id):
        self.name = name
        self.author_id = author_id


    """书籍信息表"""
    # 表名称
    __tablename__ = 'TB_BOOK'

    # 表字段
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(64), unique = True)
    #记录一的一方的id作为外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))

    # @classmethod
    # def to_json(self):
    #     return {'id': self.id, 'name': self.name, 'author_id': self.author_id}

@app.route('/')
def index():
    return "index"


@app.route('/book/list_all',  methods=['POST'])
def list_all_book():
    book_list = Book.query.all()
    books = list()
    for book_temp in book_list:
        dic_temp = book_temp.__dict__
        dic_temp.pop('_sa_instance_state')
        books.append(dic_temp)
    return jsonify({'flag': 'false', 'data': books})

@app.route('/book/add', methods=['POST'])
def add_book():
    book_name = request.form.get('book_name')
    author_name = request.form.get('author_name')

    # 通过书籍名称查询书籍是否存在
    book_info = Book.query.filter(Book.name==book_name).first()
    if book_info:
        return jsonify({'flag': 'false', 'msg': '该书籍信息已存在!'})

    # 通过作者姓名查询作者信息
    author_info = Author.query.filter(Author.name==author_name).first()
    if not author_info:
        return jsonify({'flag': 'false', 'msg': '该作者信息不存在!'})

    book = Book(name=book_name, author_id=author_info.id)
    db.session.add(book)
    db.session.commit()
    return jsonify({'flag': 'true', 'msg': '该书籍信息已经入库成功!'})

@app.route('/book/delete/<int:id>')
def delete_book_by_id(id):
    try:
        Book.query.filter(Book.id==int(id)).delete()
        db.session.commit()
        return jsonify({'flag': 'true', 'msg': '书籍信息删除成功!'})
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.close()
        return jsonify({'flag': 'false', 'msg': '书籍信息删除失败!'})

@app.route('/book/edit', methods=['POST'])
def book_edit():
    try:
        id = request.form.get('book_id')
        book_name = request.form.get('book_name')
        author_id = request.form.get('author_id')

        book = Book(book_name, author_id)
        if id:
            book.id = id
        db.session.merge(book)
        db.session.commit()
        return jsonify({'flag': 'true', 'msg': '书籍信息编辑成功!'})
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({'flag': 'false', 'msg': '书籍信息编辑失败!'})
    finally:
        db.session.close()

if __name__ == '__main__':
    # # 删除数据库表
    # db.drop_all()
    # # 创建所有的表
    # db.create_all()
    #
    # author1 = Author(name='老王')
    # author2 = Author(name='张三')
    #
    # book1 = Book(name=u'mysql 从删除到跑路', author_id=1)
    # book2 = Book(name=u'python 大法好', author_id=1)
    # book3 = Book(name=u'颈椎病康复室', author_id=2)
    # book4 = Book(name=u'oracle 从删除到跑路', author_id=2)
    # book5 = Book(name=u'java从入门到放弃', author_id=2)
    #
    # # db.session.add(author1)
    # db.session.add_all([author1, author2])
    # # db.session.commit()
    #
    # # db.session.add_all([book1, book2, book3, book4, book5])
    # db.session.add(book1)
    # db.session.add(book2)
    # db.session.add(book3)
    # db.session.add(book4)
    # db.session.add(book5)
    # db.session.commit()

    app.run(debug=True)