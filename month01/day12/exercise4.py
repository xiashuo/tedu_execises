'''
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
        Commodity(1005, "酒精", 30)
        Commodity(1006, "屠龙刀", 10000),
        Commodity(1007, "口罩", 50),
    ]
    -- 定义函数,删除列表中价格大于1w的商品
    -- (选做) 定义函数,删除列表中商品名称相同的商品(不使用其他容器,自定义算法)
'''


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


# 定义函数,删除列表中价格大于1w的商品
def delete_price_more_than_1w(list_target):
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i].price > 10000:
            del list_target[i]
    return list_target


result_list = delete_price_more_than_1w(list_commodity_infos)
for commodity in result_list:
    print(commodity.__dict__)


# 定义函数,删除列表中商品名称相同的商品(不使用其他容器,自定义算法)
def delete_the_same_name_commodity(list_target):
    for i in range(len(list_target) - 1, 0, -1):
        for j in range(i):
            if list_target[i].name == list_target[j].name:
                del list_target[i]
                break
    return list_target


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50),
]
result_list = delete_the_same_name_commodity(list_commodity_infos)
for commodity in result_list:
    print(commodity.__dict__)
