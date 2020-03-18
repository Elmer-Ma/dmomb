# _*_ coding: utf-8 _*_

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import options, define
from app.configs import configs, mongodb_configs
from app.urls import urls

from pymongo import MongoClient  # mongodb的客户端，链接工具
# 配置一个服务启动端口
define('port', type=int, default=8003, help='运行端口')


# 自定义应用
class CustomApplication(tornado.web.Application):
    def __init__(self, urls, configs):
        settings = configs
        handlers = urls
        self.md = MongoClient(
            host=mongodb_configs['db_host'],
            port=mongodb_configs['db_port'],

        )
        super(CustomApplication, self).__init__(handlers=handlers, **settings)


# 创建服务

def create_server():
    tornado.options.parse_command_line()
    # 创建http服务
    http_server = tornado.httpserver.HTTPServer(
        CustomApplication(urls, configs),
        xheaders=True
    )

    # 监听端口
    print(options.port)
    http_server.listen(options.port, address="127.0.0.1")
    tornado.ioloop.IOLoop.instance().start()
    print("服务启动成功")
