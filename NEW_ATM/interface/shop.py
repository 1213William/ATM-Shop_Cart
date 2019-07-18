from db import db_handler


def add_shop_cart_interface(shopping_cart, name):
    user_dic = db_handler.select(name)
    for i in shopping_cart:
        user_dic['shopping_cart'].append(i)
    db_handler.save(user_dic)


def clean_shop_cart_interface(name):
    money_num = 0
    user_dic = db_handler.select(name)
    for i in user_dic['shopping_cart']:
        money_num += i['price']
    return money_num
    # print(money_num)
    # pass


def del_shop_good_interface(name, good_name):
    user_dic = db_handler.select(name)
    for i in user_dic['shopping_cart'][::]:
        if i['name'] == good_name:
            user_dic['shopping_cart'].remove(i)
    db_handler.save(user_dic)
    return True, '删除成功...'


def check_shopping_cart_interface(name):
    return db_handler.select(name)['shopping_cart']


if __name__ == '__main__':
    # clean_shop_cart_interface('william')
    del_shop_good_interface('william', '贵')
