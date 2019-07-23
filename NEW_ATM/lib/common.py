from core import src
import logging
from conf import setting
import os
import logging.config
from conf import setting



def login_auth(func):
    def inner(*args, **kwargs):
        if src.user_info['name']:
            res = func(*args, **kwargs)
            return res
        print('请先去登陆...')
    return inner


def admin_login_auth(func):
    def inner(*args, **kwargs):
        if src.admin_user_info['name']:
            res = func(*args, **kwargs)
            return res
        print('请先去登陆...')
    return inner()


# 日志功能
def get_logger(type_name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(type_name)
    return logger
