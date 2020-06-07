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

def get_commodity_over1004():
    for val in list_commodity_infos:
        if val.cid > 1004:
            yield val

for val in tuple(get_commodity_over1004()):
    print(val.__dict__)


