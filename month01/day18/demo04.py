"""
    需求:
        在商品列表中,查找金额大于等于10000的商品数量
        在商品列表中,查找名称大于2个字的商品数量
        .....
        查找满足条件的元素数量

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


def get_count01():
    count = 0
    for item in list_commodity_infos:
        if item.price > 10000:
            count += 1
    return count


def get_count02():
    count = 0
    for item in list_commodity_infos:
        if len(item.name) > 2:
            count += 1
    return count


"""
# 提取不变的
def get_count(list_target, func):
    count = 0
    for item in list_target:
        # if item.price > 10000:
        if func(item):  # 使用参数(传入的函数 lambda)代替具体的逻辑判断
            count += 1
    return count

# 脑补
# def xxx(item):
#     return item.price > 10000

# lambda 参数是列表的每个元素，函数体是对每个元素的判断逻辑.
result = get_count(list_commodity_infos, lambda commodity: commodity.price >= 10000)
print(result)

result = get_count(list_commodity_infos, lambda commodity: len(commodity.name) > 2)
print(result)

"""
result = IterableHelper.get_count(list_commodity_infos, lambda commodity: commodity.price >= 10000)
print(result)
result = IterableHelper.get_count(list_commodity_infos, lambda commodity: len(commodity.name) >= 3)
print(result)
