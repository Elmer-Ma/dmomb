# _*_ coding: utf-8 _*_
import os
import tornado.gen
import tornado.concurrent

from app.api.html_common import HtmlHandler
from app.configs import configs
class DataHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()
    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(configs['templates_path'],'data/data.html'))
