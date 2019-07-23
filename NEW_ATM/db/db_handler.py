import os
import json
from conf import setting


# 通过select来对文件进行查找并返回当中的数据
def select(name):
    path = os.path.join(setting.BASE_DB,'%s.json' % name)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:

            return json.load(f)
    else:
        return None


# save是将用户的所有信息组织称一个字典直接放到文件中
def save(user_dic):
    path = os.path.join(setting.BASE_DB, '%s.json' % user_dic['name'])
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)
        f.flush()


# 管理员账户的查找
def admin_select(name):
    path = os.path.join(setting.BASE_ADMIN_DB, '%s.json' % name)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:

            return json.load(f)
    else:
        return None


# 管理员账户的保存
def admin_save(user_dic):
    path = os.path.join(setting.BASE_ADMIN_DB, '%s.json' % user_dic['name'])
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)
        f.flush()















if __name__ == '__main__':
    # save(user_dic={'name':'william'})
    pass
