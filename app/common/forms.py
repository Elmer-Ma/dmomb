# _*_ coding: utf-8 _*_
from wtforms import Form
from wtforms.fields import StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo

#添加账号表单验证模型
class AccountAddForm(Form):
    name = StringField(
        '账号名称',
        validators = [
            DataRequired('账号不能为空!')
        ]
    )
    pwd = PasswordField(
        '账号名称',
        validators = [
            DataRequired('账号密码不能为空!')
        ]
    )
    repwd = PasswordField(
        '账号名称',
        validators = [
            DataRequired('确认密码不能为空!'),
            EqualTo('pwd',message="两次输入的密码不一致!")
        ]
    )
