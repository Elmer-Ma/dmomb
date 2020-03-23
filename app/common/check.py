# _*_ coding: utf-8 _*_
from pymongo import MongoClient
from app.configs import mongodb_configs
from werkzeug.security import check_password_hash
# 验证类


class Check:
    # 定义初始化的方法
    def __init__(self):
        # 实例连接属性
        self.md = MongoClient(
            host=mongodb_configs['db_host'],
            port=mongodb_configs['db_port']
        )
    # 检测账号名称是否存在

    def check_name(self, name):
        db = self.md.dmomb
        co = db.account
        match_user = co.find({'name': name}).count()
        if int(match_user):
            return True
        else:
            return False

    # mail
    def check_mail(self, mail):
        db = self.md.dmomb
        co = db.account
        match_user = co.find({'mail': mail}).count()
        print("find ", match_user, " mail")
        if int(match_user):
            return True
        else:
            return False

    # 检测密码是否正确

    def check_pwd(self, mail, pwd):
        db = self.md.dmomb
        co = db.account
        print("mail",mail)
        match_user = co.find_one({'mail': mail})
        print("match_user",match_user)
        if match_user:
            print("check_password_hash(match_user['password'], pwd)",check_password_hash(match_user['password'], pwd))
            return (check_password_hash(match_user['password'], pwd))
