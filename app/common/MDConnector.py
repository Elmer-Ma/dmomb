# _*_ coding: utf-8 _*_
from pymongo import MongoClient
from app.configs import mongodb_configs


class MDConnector:
    def __init__(self):
        self.md = MongoClient(
            host=mongodb_configs['db_host'],
            port=mongodb_configs['db_port'],
        )
        self.db = self.md.dmomb

    # def judge_connection(self):
    #     try:
    #         self.client.admin.command('ismaster')
    #     except pymongo.errors.PyMongoError as e:
    #         print("DB ERROR!")
