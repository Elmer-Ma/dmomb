# _*_ coding: utf-8 _*_
from app.data.dbManage_data import dbManage


class Servlet_data:
    def __init__(self, data):
        self.db = dbManage()
        self.data = data
    # 将form转化为字典
    @property
    def dict_data(self):
        return dict(
            self.data
        )

    # 处理数据,并插入数据库
    def process_data(self):
        print(self.dict_data)
        # 插入数据库
        return self.db.insert(
            self.dict_data
        )
    # 将打批量的文件进行处理
