'''
    在商品列表中,删除编号是奇数的商品
    在商品列表中,删除单价小于500的商品
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

# 在商品列表中,删除编号是奇数的商品
IterableHelper.delete_by(list_commodity_infos, lambda commodity: commodity.cid % 2 == 1)
for commodity in list_commodity_infos:
    print(commodity.__dict__)

# 在商品列表中,删除单价小于500的商品
IterableHelper.delete_by(list_commodity_infos, lambda commodity: commodity.price < 500)
for commodity in list_commodity_infos:
    print(commodity.__dict__)
