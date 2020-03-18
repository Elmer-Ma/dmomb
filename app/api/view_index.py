# _*_ coding: utf-8 _*_
import time
import os
import tornado.gen
import tornado.concurrent
from app.api.html_common import HtmlHandler
from app.configs import configs
from tornado.escape import utf8
from tornado.util import unicode_type
from concurrent.futures import ThreadPoolExecutor
# from tornado.template import Template


class IndexHandler(HtmlHandler):
    # executor = ThreadPoolExecutor(50)
    # get
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        # loader = Template
        print("view_index.py")
        time.sleep(5)
        self.html(os.path.join(configs['templates_path'], 'shouye/index.html'))
