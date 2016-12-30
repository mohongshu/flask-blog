#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Config(object):
    '''基本配置类'''
    pass

class ProdConfig(Config):
    '''生产配置类'''
    pass

class DevConfig(Config):
    '''开发配置类'''
    DEBUG = True
    #MySQL 连接
    SQLALCHEMY_DATABASE_URL = 'mysql://blog:blog@127.0.0.1:3306/blog'
