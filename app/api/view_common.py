# _*_ coding: utf-8 _*_
import datetime
import json
import  tornado.web
from concurrent.futures import ThreadPoolExecutor
# from app.common.ip2Addr import ip2addr
class CommonHandler(tornado.web.RequestHandler):
    #定义线程池
    executor = ThreadPoolExecutor(50)

    #前缀地址
    @property
    def site_url(self):
        return 'http://127.0.0.1:8003'

    @property
    def md(self):
        return self.application.md

    #客户端向服务端发送给请求并处理
    @property
    def params(self):
        data = self.request.body
        #包含字节型类型，转化为python数据类型
        data = {
            k:v
            for k,v in json.loads(data.decode('utf-8')).items()
        }
        return data

    #时间属性
    @property
    def dt(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #公共参数
    @property
    def common_params(self):
        data = dict(
            createAt = self.dt,
            ip = self.request.remote_ip, #获取IP地址
            # addr = ip2addr(self.request.remote_ip)['region'].decode('utf-8'),
            headers = dict(self.request.headers)
        )
        return data


if __name__ == "__main__":
    print(
        CommonHandler.common_params

    )

