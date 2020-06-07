"""
    需求:
        在商品列表中,查找最贵的商品
        在商品列表中,查找商品编号最大的商品
        .....
        根据条件获取最大值

    步骤:
        1. 实现完整功能
        2. 将不变的定义到IterableHelper类中
        3. 在当前模块中调用IterableHelper类中代码
               不变的 + 变化的(lambda)
"""


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


def get_max01():
    max_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_value.price < list_commodity_infos[i].price:
            max_value = list_commodity_infos[i]
    return max_value


def get_max02():
    max_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_value.cid < list_commodity_infos[i].cid:
            max_value = list_commodity_infos[i]
    return max_value


def get_max(list_target, func):
    max_value = list_target[0]
    for i in range(1, len(list_target)):
        # if max_value.price < list_target[i].price:
        if func(max_value) < func(list_target[i]):
            max_value = list_target[i]
    return max_value


# def xxx(item):
#     return item.price

result =get_max(list_commodity_infos, lambda element: element.price)
print(result.__dict__)
