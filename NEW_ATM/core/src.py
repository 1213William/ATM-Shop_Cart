from interface import bank, user, shop
from lib import common, goods


user_info = {
    'name': None,
}


def register():
    while 1:
        user_name = input('user_name:>>').strip()
        if user_name == 'q':
            break
        password = input('password:>>').strip()
        again_password = input('again_password:>>').strip()
        if password != again_password:
            print('密码输入不一致，请重新输入...')
            continue
        # user_dic = {
        #     'name': user_name,
        #     'password': password,
        #     'balance': None,
        # }

        flag, msg = user.register_interface(user_name, password)
        if flag:
            print(msg)
            break
        else:
            print(msg)


def login():
    while 1:
        user_name = input('user_name:>>').strip()
        if user_name == 'q':
            break
        password = input('password:>>').strip()
        flag, msg = user.login_interface(user_name, password)
        if flag:
            user_info['name'] = user_name
            # print(user_info['name'])
            print(msg)
            break
        else:
            print(msg)


# 查询余额
@common.login_auth
def check_balance():
    print('当前余额为：%s' % bank.check_balance_interface(user_info['name']))


# 账户充值
@common.login_auth
def account_recharge():
    while 1:
        money = input('充值金额:>>').strip()
        if money == 'q':
            break
        if not money.isdigit():
            print('充值的金额必须为数字类型...')
            print(user_info['name'])
            continue
        money = int(money)
        flag, msg = bank.account_recharge_interface(user_info['name'], money)
        if flag:
            print(msg)
            logger = common.log('recharge.log')
            logger.error('%s 充值了 %s' % (user_info['name'], money))
            break
        else:
            print(msg)


# 账户提现
@common.login_auth
def account_withdraw():
    while 1:
        money = input('请输入要提现的金额:>>').strip()
        if money.isdigit():
            money = int(money)
            flag, msg = bank.account_withdraw_interface(user_info['name'], money)
            if flag:
                print(msg)
                logger = common.log('withdraw.log')
                logger.error('%s 提现了 %s' % (user_info['name'], money))
                break
            else:
                print(msg)
        print('提现的金额必须是数字...')


# 查看流水
@common.login_auth
def check_rivers():
    print(bank.check_rivers_interface(user_info['name']))


# 账户的切换
@common.login_auth
def account_switch():
    while 1:
        to_account = input('请选择要切换的账户:>>').strip()
        if to_account == 'q':
            break
        flag, msg = user.account_switch_interface(user_info['name'], to_account)
        if flag:
            user_info['name'] = to_account
            # print(user_info['name'])
            print(msg)
            break
        else:
            print(msg)


# 退出当前账户
@common.login_auth
def exit_account_now():
    user_info['name'] = None


@common.login_auth
def add_shop_cart():
    # 购物车列表
    shopping_cart = []
    flag = []
    while 1:
        for index, goods_lst in enumerate(goods.books, 1):
            print('%s -->  %s' % (index, goods_lst))
            flag.append(index)
        choice = input('请输入商品序号:>>').strip()
        if choice == 'q':
            break
        elif not choice.isdigit():
            print('请理性输入...')
            continue
        choice = int(choice)
        if choice in flag:
            # print('this is flag')
            choice -= 1
            good_name = goods.books[choice][0]
            good_price = goods.books[choice][1]
            while 1:
                yn = input('是否要添加到购物车中:>>(y/n) --> ').strip()

                if yn == 'y':
                    shop_info = {
                       'name': good_name,
                       'price': good_price,
                       'count': 1
                    }
                    shopping_cart.append(shop_info)
                    break
                elif yn == 'n' or yn == 'q':
                    break
                else:
                    print('请理性输入...')
            if shopping_cart:
                shop.add_shop_cart_interface(shopping_cart, user_info['name'])


@common.login_auth
def clean_shop_cart():
    balance = bank.check_balance_interface(user_info['name'])
    while 1:
        choice = input('是否要清空当前的购物车:>>(y/n) -->').strip()
        if choice == 'y':
            money_num = shop.clean_shop_cart_interface(user_info['name'])
            if balance >= money_num:
                flag, msg = bank.clean_shop_cart_interface(user_info['name'], money_num)
                if flag:
                    print(msg)
                    break
            else:
                print('当前余额不支持此次付款...')
        elif choice == 'n':
            break
    pass


# 删除购物车中某件商品
@common.login_auth
def del_shop_goods():
    while 1:
        good_name = input('请输入你要删除的商品:>>').strip()
        flag, msg = shop.del_shop_good_interface(user_info['name'], good_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 查看当前购物车
@common.login_auth
def check_shopping_cart():
    print(shop.check_shopping_cart_interface(user_info['name']))


func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': account_recharge,
    '5': account_withdraw,
    '6': check_rivers,
    '7': account_switch,
    '8': exit_account_now,
    '9': add_shop_cart,
    '10': clean_shop_cart,
    '11': del_shop_goods,
    '12': check_shopping_cart
    }


def run():
    while True:
        print('''
        1 注册
        2 登录
        3 查看余额
        4 充值
        5 提现
        6 查看流水
        7 账户切换
        8 退出当前账户
        9 添加到购物车
        10 清空购物车
        11 删除shop_cart中某物品
        12 查看购物车
        ''')
        choice = input('请选择>>:').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            continue
        func_dic[choice]()
