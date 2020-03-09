# _*_ coding: utf-8
import os
import tornado.gen
import tornado.concurrent
from app.api.html_common import HtmlHandler
from app.configs import configs
#添加账号视图
class AccountAddHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self,*args,**kwargs):
        yield self.get_response()
    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(configs['templates_path'],'userInfo/addAccount.html'))