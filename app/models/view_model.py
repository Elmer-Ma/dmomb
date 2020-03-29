# _*_ coding: utf-8 _*_
import os
import datetime
import json
import markdown
import codecs
import tornado.gen
import tornado.concurrent

from bson.objectid import ObjectId
from app.api.html_common import HtmlHandler
from app.configs import configs
from app.common.forms import ModelForm
# 显示model相关信息


class ModelHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):

        db = self.md.dmomb
        co = db.model_info
        collections = co.find()
        data = dict(
            collections=collections
        )
        print(data)
        self.html(os.path.join(
            configs['templates_path'], 'models/model.html'), data=data)

    @tornado.gen.coroutine
    def post(self):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        self.write(res)

    def check_xsrf_cookie(self):
        # 非常有用的在单页面禁用xsrf_cookie的检查
        return True

# 添加model相关信息


class AddModelHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(
            configs['templates_path'], 'models/add_model.html'))

    @tornado.gen.coroutine
    def post(self):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        file_metas = self.request.files.get('file', None)  # 获取post提交的文件
        form = ModelForm(self.form_params)  # 获取表单的其他参数
        file_path = ''
        if form.validate():
            res = dict(code=1, msg='成功')
            # 写入文件
            if file_metas is not None:
                res['file_flag'] = 1
                for meta in file_metas:
                    filename = meta['filename']
                    # file_uuid = uuid.uuid4()
                    file_path = os.path.join(self.upload_path, filename)
                    file_db_path = os.path.join(self.file_db_path, filename)
                    with open(file_path, 'wb') as up:
                        up.write(meta['body'])
            # 写入数据库
            db = self.md.dmomb
            co = db.model_info
            co.insert_one(
                dict(
                    name=form.data['name'],
                    paper=form.data['paper'],
                    data_url=form.data['data_url'],
                    file_path=file_db_path,
                    markdown_info=form.data['markdown'],
                    createAt=datetime.datetime.now(),
                    updatedAt=datetime.datetime.now()
                )
            )
        self.write(res)

    def check_xsrf_cookie(self):
        # 非常有用的在单页面禁用xsrf_cookie的检查
        return True
# 模型相信信息显示渲染


class ModelDetail(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        _id = str(self.get_argument('_id'))
        print(_id)
        db = self.md.dmomb
        co = db.model_info
        collections = co.find({'_id': ObjectId(_id)}, {'markdown_info': 1})
        # 加一步将markdown转化为html文件.
        css = '''<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <style type="text/css">
            <!-- 此处省略掉markdown的css样式，因为太长了 -->
            </style>
            '''
        html = markdown.markdown(collections[0]['markdown_info'])
        #################
        data = dict(
            markdown_info=html
        )
        print(data)
        self.html(os.path.join(
            configs['templates_path'], 'models/model_detail.html'), data=data)

    @tornado.gen.coroutine
    def post(self):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        self.write(res)

    def check_xsrf_cookie(self):
        # 非常有用的在单页面禁用xsrf_cookie的检查
        return True
