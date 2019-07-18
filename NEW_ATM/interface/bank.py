from db import db_handler


# 查询当前余额的接口
def check_balance_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['balance']


def account_recharge_interface(name, money):
    user_dic = db_handler.select(name)
    user_dic['balance'] += money
    user_dic['rivers'].append('%s充值了%s' % (user_dic['name'], money))
    db_handler.save(user_dic)
    return True, '充值成功...'


def account_withdraw_interface(name, money):
    user_dic = db_handler.select(name)
    user_dic['balance'] -= money
    user_dic['rivers'].append('%s提现了%s' % (user_dic['name'], money))

    db_handler.save(user_dic)
    return True, '提现成功...'


def check_rivers_interface(name):
    return db_handler.select(name)['rivers']


def clean_shop_cart_interface(name, money):
    user_dic = db_handler.select(name)
    user_dic['balance'] -= money
    user_dic['shopping_cart'].clear()
    db_handler.save(user_dic)
    return True, '购买成功'


if __name__ == '__main__':
    account_recharge_interface('william', 1)
