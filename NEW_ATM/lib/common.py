from core import src
import logging
from conf import setting
import os




def login_auth(func):
    def inner(*args, **kwargs):
        if src.user_info['name']:
            res = func(*args, **kwargs)
            return res
        print('请先去登陆...')
    return inner


def log(file_name):
    path = os.path.join(setting.BASE_LOG, file_name)
    file_handler = logging.FileHandler(path, 'a', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s'))
    logger1 = logging.Logger('A', level=30)
    logger1.addHandler(file_handler)
    return logger1

