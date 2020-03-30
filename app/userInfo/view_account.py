# _*_ coding: utf-8
import os
import datetime
import tornado.gen
import tornado.concurrent
from app.api.html_common import HtmlHandler
from app.api.view_common import CommonHandler
from app.configs import configs
from app.common.forms import AccountAddForm, LoginForm
from werkzeug.security import generate_password_hash  # 生成hash加密
# 添加账号视图


class AccountAddHandler(CommonHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(
            configs['templates_path'], 'userInfo/addAccount.html'))

    # post chuandi param
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        print("进去view_account")
        form = AccountAddForm(self.form_params)
        print("self.form_params", self.form_params)
        if form.validate():
            # 验证通过
            # 保存数据
            db = self.md.dmomb
            co = db.account
            # 'name','number','mail','password','repassword'
            co.insert_one(
                dict(
                    name=form.data['name'],
                    number=form.data['number'],
                    mail=form.data['mail'],
                    password=generate_password_hash(form.data['password']),
                    createAt=datetime.datetime.now(),
                    updatedAt=datetime.datetime.now()
                )
            )
            # 定义成功接口格式
            res['code'] = 1
            res['msg'] = '成功'
        else:
            # 定义失败接口格式
            res['data'] = form.errors
        self.write(res)
# 处理登录操作


class LoginHandler(CommonHandler):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html(os.path.join(
            configs['templates_path'], 'shouye/index.html'))

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()

    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0, msg='失败')
        print("进去LoginHandler")
        form = LoginForm(self.form_params)
        print("form", form)
        # field = form.mail
        if form.validate():
            # 设置安全会话,实现权限管理
            self.set_secure_cookie('name', form.data['mail'])
            # 定义成功接口格式
            res['code'] = 1
            res['msg'] = '成功'
            res['user'] = self.form_params
        else:
            # 定义失败接口格式
            res['data'] = form.errors
        print("res", res)
        self.write(res)
