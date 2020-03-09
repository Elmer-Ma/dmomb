# _*_ coding: utf-8 _*_
import os
from app.common.ip2Region import Ip2Region


#将IP转化为地址的函数4

def ip2addr(ip):
    #找到Ip地址库的路径
    ip_db_path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        'static/ip2region/ip2region.db'
    )
    #实例化
    ip_to_addr = Ip2Region(ip_db_path)
    #地址信息
    addr_info = ip_to_addr.memorySearch(ip)
    return addr_info

if __name__ == "__main__":
    addr1 =  ip2addr('61.135.169.121')
    print(
        "城市ID：{},地址信息:{}".format(
            addr1['city_id'],
            addr1['region'].decode('utf-8')
        )
    )
    addr2 = ip2addr('222.134.66.167')
    print(
        "城市ID：{},地址信息:{}".format(
            addr2['city_id'],
            addr2['region'].decode('utf-8')
        )
    )
