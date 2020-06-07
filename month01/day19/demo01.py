"""
    内置高阶函数

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

# 1. 过滤器filter：过滤出满足条件的元素
# for item in IterableHelper.find_all(list_commodity_infos,lambda item:item.price > 500 ):
#     print(item.__dict__)
for item in filter(lambda item: item.price > 500, list_commodity_infos):
    print(item.__dict__)

# 2. 映射map:自定义对象(商品)  对应  实例变量(名称)
# for item in IterableHelper.select(list_commodity_infos,lambda item:item.name):
#     print(item)
for item in map(lambda item: item.name, list_commodity_infos):
    print(item)

# 3.获取最大值max/min
# 注意：lambda使用关键字实参传递
# result  =IterableHelper.get_max(list_commodity_infos,lambda item:item.price)

result = max(list_commodity_infos, key=lambda item: item.price)
print(result.__dict__)

# 4. 排序
# 注意：返回排好序的新列表
# IterableHelper.order_by(list_commodity_infos,lambda item: item.price)
# for item in list_commodity_infos:
#     print(item.__dict__)

# 升序
# result = sorted(list_commodity_infos, key=lambda item: item.price)
# 降序
result = sorted(list_commodity_infos, key=lambda item: item.price, reverse=True)
for item in result:
    print(item.__dict__)
