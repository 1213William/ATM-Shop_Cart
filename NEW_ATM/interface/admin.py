from db import db_handler
from lib import common


admin_logger = common.get_logger('admin')


def lock_account_interface(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['lock'] = True
        db_handler.save(user_dic)
        return True, f'{name}账户已被冻结'
    else:
        return False, f'{name}账户不存在'


def unlock_account_interface(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['lock'] = False
        db_handler.save(user_dic)
        return True, f'{name}账户已被解冻'
    else:
        return False, f'{name}账户不存在'


def change_bal_interface(name, money):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['balance'] = money
        db_handler.save(user_dic)
        return True, f'{name}账户额度修改为{money}'
    else:
        return False, f'{name}当前账户错误'


def check_uname_interface(name):
    admin_user_dic = db_handler.admin_select(name)
    if admin_user_dic:
        return False, '当前用户已注册...'
    else:
        return True, ''


def save_register_interface(name, pwd):
    user_dic = {
        'name': name,
        'pwd': pwd
    }
    db_handler.admin_save(user_dic)
    return True, f'{user_dic["name"]}管理员注册成功...'


def admin_login_interface(name, pwd):
    admin_user_dic = db_handler.admin_select(name)
    print(admin_user_dic)
    if admin_user_dic['name'] == name and admin_user_dic['pwd'] == pwd:
        return True, f'{name}管理员登陆成功...'



