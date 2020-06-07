'''
    在商品列表中,删除名称相同的商品
    在商品列表中,删除单价相同的商品
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

# 在商品列表中,删除名称相同的商品
IterableHelper.remove_duplicate(list_commodity_infos,lambda commodity:commodity.name)
for com in list_commodity_infos:
    print(com.__dict__)

# 在商品列表中,删除单价相同的商品
IterableHelper.remove_duplicate(list_commodity_infos,lambda commodity:commodity.price)
for com in list_commodity_infos:
    print(com.__dict__)
