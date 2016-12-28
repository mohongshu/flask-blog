#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask.ext.script import Manager, Server
import main
import models

#初始化manager对象 via app object
manager = Manager(main.app)

#创建新命令：server，用于运行Flask开发环境
manager.add_command('server', Server())

@manager.shell
def make_shell_context():
    ''' 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return: Default import object
    type: Dict
    '''
    return dict(app=main.app,
                db=models.db,
                User=models.User)

if __name__ == '__main__':
    manager.run()
