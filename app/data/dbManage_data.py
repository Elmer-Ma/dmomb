# _*_ coding: utf-8 _*_
from app.common.MDConnector import MDConnector


class dbManage(MDConnector):  # 继承公共数据库连接器
    # 将数据字典插入,如果插入成功返回True,如果插入失败,返回False
    def insert(self, dict_form):
        print(dict_form)
        self.co = self.db.data_info
        inser_flag = self.co.insert_one(
            dict_form
        )
        if not inser_flag:
            return True
        return False
