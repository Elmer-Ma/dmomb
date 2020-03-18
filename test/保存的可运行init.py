#_*_ coding:utf-8 _*_
import os
from  tornado.web import Application
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import  options,define
from app.configs import configs
from app.urls import urls
from app.api.view_index import IndexHandler
define('port',type=int,default=8003,help="运行端口")
define('host',type=str,default="127.0.0.1",help="运行端口")
#application
# class CustomApplication(tornado.web.Application):
#     def __int__(self,urls,configs):
#         static_handlers = configs
#         # handlers = urls
#         handlers = [
#             (r'/',IndexHandler),

#         ]
#         settings = dict(
#             static_path = os.path.join(root_path,"static"),
#             templates_path = os.path.join(root_path,"templates"),
#             debug = True
#             )
#         super(CustomApplication,self).__init__(handlers=handlers,  **settings)


#create server
def create_server():
    tornado.options.parse_command_line()
    #create http server
    print(configs)
    # print(**configs)
    custom = Application(urls,**configs)
    print(custom.settings)
    http_server = tornado.httpserver.HTTPServer(
        custom,
        xheaders = True
    )
    #监听端口
    # print(options.port)
    http_server.listen(options.port,address=options.host)
    tornado.ioloop.IOLoop.current().start()
    # IOLoop.current().start()
    print("服务启动")
   

    