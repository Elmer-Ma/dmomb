#_*_ coding: utf-8 _*_
from app.admin.view_admin_index import IndexHandler as admin_index
from app.api.view_index import IndexHandler as api_index
from app.userInfo.view_account import AccountAddHandler as user_add_account
from app.data.view_data import DataHandler as data_index
from app.models.view_model import ModelHandler as models_index
import tornado
from app.configs import configs
#api接口
api_urls=[
    (r'/',api_index),
    (r'/data',data_index),
    (r'/models',models_index)
]

#静态文件
# static_urls = [
#     (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler,dict(path=configs['static_path']))
#      ]

#后台系统
admin_urls = [
    (r'/admin_fucker',admin_index)
]

user_urls = [
    (r'/user/add/',user_add_account)
]

urls = api_urls + admin_urls + user_urls

print(urls)