# _*_ coding:utf-8 _*_
import os
root_path = os.path.dirname(__file__)
# 公共信息配置

configs = dict(
    xsrf_cookies=True,
    cookie_secret='e9b83658c980462ca3c844e01c239352',
    static_path=os.path.join(root_path, "static"),
    templates_path=os.path.join(root_path, "templates"),
    debug=True
)

# 数据库注册信息
mongodb_configs = dict(
    db_host='106.14.200.68',
    db_port=27017
)
# print(configs['templates_path'])
# print(configs['static_path'])
# print(configs)
