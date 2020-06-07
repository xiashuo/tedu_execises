"""
    需求:
        在商品列表中,查找编号是1002的商品对象
        在商品列表中,查找名称是金箍棒的商品对象
        .....
        查找满足条件的单个对象

    步骤:
        1. 实现完整功能
        2. 使用函数式编程思想(分,隔,做),拆分完整功能.
                编写不变的/变化的/连接的代码
        3. 将不变的定义到IterableHelper类中
        4. 在当前模块中调用IterableHelper类中代码
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


def find01():
    for item in list_commodity_infos:
        if item.cid == 1002:
            return item


def find02():
    for item in list_commodity_infos:
        if item.name == "金箍棒":
            return item


# def condition01(item):
#     return item.cid == 1002

# def condition02(item)
#     return item.name == "金箍棒"

# re = IterableHelper.find_single(list_commodity_infos, condition02)
# print(re.__dict__)


re = IterableHelper.find_single(list_commodity_infos,
                                lambda item:item.name == "金箍棒")
print(re.__dict__)