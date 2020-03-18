# _*_ coding: utf-8 _*_
import os
import uuid
import datetime
import tornado.gen
import tornado.concurrent

from app.api.html_common import HtmlHandler
from app.configs import configs
from app.common.forms import DataForm


class DataHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(configs['templates_path'], 'data/data.html'))


# 上传文件
class DataUploadHandler(HtmlHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(
            configs['templates_path'], 'data/upload_data.html'))

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        file_metas = self.request.files.get('file', None)
        # if not file_metas:
        #     res['result'] = 'Invalid Args'
        #     print("没有文件返回了了")
        #     return res
        file_uuid = 'nothing'
        file_path = 'nothing'
        if file_metas is not None:
            res['file_flag'] = 1
            for meta in file_metas:
                filename = meta['filename']
                file_uuid = uuid.uuid4()
                file_path = os.path.join(self.upload_path, filename)

                with open(file_path, 'wb') as up:
                    up.write(meta['body'])

        print(self.form_params)
        form = DataForm(self.form_params)
        if form.validate():
            # 根据文件名称生成唯一的uuid,并将这个当做标识
            print("验证成功")
            # 写入数据库
            db = self.md.dmomb
            co = db.data_info
            co.insert_one(
                dict(
                    name=form.data['name'],
                    file_uuid=file_uuid,
                    userId="应该标识是那个用户",
                    file_path=file_path,
                    markdown_info=form.data['markdown'],
                    createAt=datetime.datetime.now(),
                    updatedAt=datetime.datetime.now()
                )
            )
            # 返回成功数据
            # 定义成功接口格式
            res['code'] = 1
            res['msg'] = '成功'
        else:
            # 定义失败接口格式
            res['data'] = form.errors
        self.write(res)

    def check_xsrf_cookie(self):
        # 非常有用的在单页面禁用xsrf_cookie的检查
        return True
