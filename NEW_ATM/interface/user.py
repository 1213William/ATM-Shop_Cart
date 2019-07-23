import os
from db import db_handler
from conf import setting
import time


def register_interface(name, pwd, balance=15000):
    path = os.path.join(setting.BASE_DB, '%s.json' % name)
    if os.path.exists(path):
        return False, '当前用户已存在...'
    user_dic = {
        'name': name,
        'password': pwd,
        'balance': balance,
        'lock': False,
        'time': time.strftime('%d'),
        'rivers': [],
        'shopping_cart': []
    }
    db_handler.save(user_dic)
    return True, '注册成功...'


def login_interface(name, pwd):
    user_dic = db_handler.select(name)
    if user_dic:
        if user_dic['name'] == name and user_dic['password'] == pwd:
            return True, '登陆成功'
        return False, '登陆失败'
    else:
        return False, '当前用户不存在...'


def account_switch_interface(my_account, to_account):
    to_dic = db_handler.select(to_account)
    # my_dic = db_handler.select(my_account)
    if to_dic:
        return True, '账户切换成功'
    else:
        return False, '账户不存在'


def check_lock_interface(name):
    user_dic = db_handler.select(name)
    if user_dic['lock']:
        return False, f'{name}用户已被冻结'
    else:
        return True, f'{name}可以登录'


