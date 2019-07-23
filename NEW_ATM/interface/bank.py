from db import db_handler
from lib import common
from conf import setting
from core import src
import time
import sys


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


# 对于还款时间的设定
def repayment_time_interface(name):
    """
    :param name:
    :return:
    """
    user_dic = db_handler.select(name)
    # 还款日期为20号

    now = int(time.strftime('%d'))
    if now < setting.REPAYMENT_TIME:
        d = 20 - int(now)  # user_dic['time'] = 21
        return '距离还款日期还剩：%s天' % d
    elif now > setting.REPAYMENT_TIME:
        d = 30 - abs((20 - int(now)))  #
        return '距离还款日期还剩：%s天' % d
    else:
        if user_dic['balance'] >= 0:
            return '当前余额充足...'
        else:
            print('请先对当前账户进行充值, 否则自动退出...')
            is_true = True
            while is_true:
                choice = input('是否进行充值(y/n):').strip()
                if choice == 'y':
                    while is_true:
                        money = input('充值金额:>>').strip()
                        if money == 'q':
                            break
                        if not money.isdigit():
                            print('充值的金额必须为数字类型...')
                            # print(user_info['name'])
                            continue
                        money = int(money)
                        flag, msg = account_recharge_interface(name, money)
                        if flag:
                            print(msg)
                            logger = common.log('recharge.log')
                            logger.info('%s 充值了 %s' % (name, money))
                            db_user_dic = db_handler.select(name)
                            if db_user_dic['balance'] >= 0:
                                is_true = False
                                break
                            else:
                                print('当前余额为：%s元，请继续进行充值或退出...' % db_user_dic['balance'])
                                continue
                        else:
                            print(msg)
                    pass
                elif choice == 'n':

                    db_user = db_handler.select(name)
                    if db_user['balance'] >= 0:
                        break
                    else:
                        sys.exit()


def check_user_dic_interface(name):
    user_dic = db_handler.select(name)
    return user_dic


if __name__ == '__main__':
    account_recharge_interface('william', 1)
