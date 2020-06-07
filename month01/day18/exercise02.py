"""
    在商品列表中,查找编号是1002的商品对象
    在商品列表中,查找名称是金箍棒的商品对象
"""
from common.iterable_tools import IterableHelper


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __add__(self, other):
        self.price += other
        return self

    def __eq__(self, other):
        return self.price >= other.price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50),
]

for item in IterableHelper.find_by_condition(list_commodity_infos, lambda item: item.cid > 1001):
    print(item.__dict__)

print(IterableHelper.find_counts_by_condition(list_commodity_infos, Commodity(price=10000)))
