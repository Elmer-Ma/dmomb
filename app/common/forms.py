# _*_ coding: utf-8 _*_
from wtforms import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.common.check import Check
# 添加账号表单验证模型


class AccountAddForm(Form):
    name = StringField(
        '账号名称',
        validators=[
            DataRequired('账号不能为空!')
        ]
    )
    number = StringField(
        '手机号码',
        validators=[
            DataRequired('手机号码不能为空!')
        ]
    )
    mail = StringField(
        '邮箱',
        validators=[
            DataRequired('邮箱不能为空!')
        ]
    )
    password = PasswordField(
        '密码',
        validators=[
            DataRequired('账号密码不能为空!')
        ]
    )
    repassword = PasswordField(
        '重复密码',
        validators=[
            DataRequired('确认密码不能为空!'),
            EqualTo('password', message="两次输入的密码不一致!")
        ]
    )
# 登录表单验证模型


class LoginForm(Form):
    # name = StringField(
    #     'name',
    #     validators=[
    #         DataRequired("账号名称不能为空!")
    #     ]
    # )
    mail = StringField(
        'mail',
        validators=[
            DataRequired("mail不能为空!")
        ]
    )
    password = StringField(
        '账号密码',
        validators=[
            DataRequired("密码不能为空!")
        ]
    )
    # 验证名称

    # def validate_name(self, field):
    #     data = field.data
    #     c = Check()
    #     match_user = c.check_name(data)
    #     print("forms.py check name")
    #     if match_user:
    #         raise ValidationError("账号名称不存在!!")
    # mail

    def validate_mail(self, field):
        data = field.data
        print("form.py 76", data)
        c = Check()
        match_user = c.check_mail(data)
        print("forms.py check name")
        if match_user < 1:
            raise ValidationError("mail不存在!!")

    # 验证密码

    def validate_password(self, field):
        data = field.data
        print("form.py 87", data)
        mail = self.mail.data
        c = Check()
        match_user = c.check_pwd(mail, data)
        print("match_user zzz",match_user)
        if match_user == None or match_user==False:
            raise ValidationError("账号密码不正确!")




class DataForm(Form):
    # 'name', 'file', 'markdown'
    name = StringField(
        '数据名称',
        validators=[
            DataRequired("数据名称不能为空!")
        ]
    )
    # file = StringFuield(
    #     '文件数据',
    #     validators=[
    #         DataRequired("文件不能为空!")
    #     ]
    # )
    markdown = StringField(
        '相关说明',
        validators=[
            DataRequired("相关说明不能为空!")
        ]
    )


class ModelForm(Form):
    # 'name', paper, data_url, 'file', 'markdown'
    name = StringField(
        '数据名称',
        validators=[
            DataRequired("数据名称不能为空!")
        ]
    )
    paper = StringField(
        '论文地址',
        validators=[
            DataRequired("论文地址不能为空!")
        ]
    )
    data_url = StringField(
        '数据地址',
        validators=[
            DataRequired("数据地址不能为空!")
        ]
    )

    # file = StringFuield(
    #     '文件数据',
    #     validators=[
    #         DataRequired("文件不能为空!")
    #     ]
    # )
    markdown = StringField(
        '说明建议',
        validators=[
            DataRequired("说明建议不能为空!")
        ]
    )
