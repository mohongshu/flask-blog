#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from main import app


# INIT the sqlalchemy object
# SQLAlchemy 会自动的从 app 对象中的 DevConfig 中加载连接数据库的配置项
db = SQLAlchemy(app)

class User(db.Model):
    '''users'''

    # 设置表名
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.name = username

    def __repr__(self):
        '''为用户实例定义字符格式'''
        return '<Model User `{}`>'.format(self.username)
