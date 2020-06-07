"""
    练习: 参照demo02,以函数式编程思想,改写下列代码.
"""
from common.iterable_tools import IterableHelper


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


# 练习1:定义函数,在商品列表中,获取编号大于1004的所有商品信息.
def commodity_cid_over_1004():
    for com in list_commodity_infos:
        if com.cid > 1004:
            yield com


# 练习2:定义函数,在商品列表中,获取价格小于10000的所有商品信息.
def get_commodity_price_less_10000():
    for commodity in list_commodity_infos:
        if commodity.price < 10000:
            yield commodity


# for commodity in get_commodity_price_less_10000():
#     print(commodity.__dict__)

# 变化的
def condition01(com):
    return com.cid > 1004


def condition02(commodity):
    return commodity.price < 10000


"""
# 不变的
def find_all(list_target, func):
    for commodity in list_target:
        # if commodity.price < 10000:
        # if condition02(commodity):
        if func(commodity):
            yield commodity

# 连接的:  不变的(变化的)
for item in find_all(list_commodity_infos, condition01):
    print(item.__dict__)
"""
for item in IterableHelper.find_all(list_commodity_infos, condition01):
    print(item.__dict__)
