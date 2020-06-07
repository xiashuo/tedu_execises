'''
    在商品列表中,判断是否存在单价为12000的商品信息  False
    在商品列表中,判断是否存在编号1005的商品信息    True
'''
from common.iterable_tools import IterableHelper
from model import *


class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50),
]

# 在商品列表中,判断是否存在单价为12000的商品信息
print(IterableHelper.is_exist(list_commodity_infos, lambda commodity: commodity.price == 12000))

# 在商品列表中,判断是否存在编号1005的商品信息
print(IterableHelper.is_exist(list_commodity_infos, lambda commodity: commodity.cid == 1005))
