"""
    需求1:
        在商品列表中,查找最便宜的商品
        在商品列表中,查找商品编号最小的商品
        根据条件获取最小值

    需求2:
        在商品列表中,根据单价对商品列表升序排列
        在商品列表中,根据商品名称字符长度升序排列
        根据条件对列表进行升序排列

    步骤:
        1. 实现完整功能
        2. 将不变的定义到IterableHelper类中
        3. 在当前模块中调用IterableHelper类中代码
               不变的 + 变化的(lambda)
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

# 练习1：
re = IterableHelper.get_min(list_commodity_infos, lambda item: item.price)
print(re.__dict__)


# 练习2:
def order_by01():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].price > list_commodity_infos[c].price:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


def order_by02():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].cid > list_commodity_infos[c].cid:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


def order_by(list_target, func):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            # if list_commodity_infos[r].cid > list_commodity_infos[c].cid:
            if func(list_target[r]) > func(list_target[c]):
                list_target[r], list_target[c] = list_target[c], list_target[r]


# def xxx(item):
#     return item.cid


order_by(list_commodity_infos, lambda item: item.cid)

# re = [item.__dict__ for item in list_commodity_infos]
# print(re)

for item in list_commodity_infos:
    print(item.__dict__)
