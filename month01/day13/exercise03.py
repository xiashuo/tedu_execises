class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    # 内容是否相同的依据
    def __eq__(self, other):
        # if type(other) == Commodity:
        return self.cid == other.cid

    # 比较大小的依据
    def __lt__(self, other):
        return self.price < other.price



list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
# 不同类型 比较 无意义
# print(Commodity(1001, "屠龙刀", 10000) == 1001)

# 1. 在商品列表中,查找Commodity(1003)的索引  列表.index
print(list_commodity_infos.index(Commodity(1003)))
# 2. 在商品列表中,判断是否存在Commodity(1005)的商品 Commodity(1005) in 列表
print(Commodity(1003) in list_commodity_infos)
# 3. 在商品列表中,移除Commodity(1002)对象
list_commodity_infos.remove(Commodity(1002))
for val in list_commodity_infos:
    print(val.__dict__)
# 4. 在商品列表中,根据升序排列
list_commodity_infos.sort()
for val in list_commodity_infos:
    print(val.__dict__)
# 5. 在商品列表中,获取单价最高的商品
min_value = min(list_commodity_infos)
print(min_value.__dict__)
