# ATM-Shop_Cart

conf:
    setting.py:配置文件
core:
    src.py:核心逻辑
db:
    db_handler.py:数据保存与提取
interface:与src的连接，通过interface来操作db中的数据
    bank.py:关于钱的
    shop.py:关于钱的
    user.py:关于用户信息的
lib:
    common.py:一些共用的配置
    goods.py:商品列表
log:
    相关的日志文件

start.py是项目的启动文件，ATM-Shop_Cart项目还在不断更新中...
