'''
# 商品列表
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 2},
]
# (1). 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
# (2). 定义函数,打印商品单价小于2万的商品信息
# (3). 定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
# (4). 定义函数,计算订单总价格：累加 (商品单价 * 数量)
# (5). 查找数量最多的订单(使用自定义算法,不使用内置函数)
# (6). 根据购买数量对订单列表降序排列

'''

# 商品列表
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 2},
]

print("(1). 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.")


def print_all_commodity_infos(dict_commodity_infos):
    for cid, commodity_info in dict_commodity_infos.items():
        print(f"商品编号:{cid},商品名称:{commodity_info['name']},商品单价:{commodity_info['price']}.")


print_all_commodity_infos(dict_commodity_infos)

print()
print("(2). 定义函数,打印商品单价小于2万的商品信息")


def print_commodity_price_less_than_2w(dict_commodity_infos):
    for cid, commodity_info in dict_commodity_infos.items():
        if commodity_info['price'] < 20000:
            print(f"商品编号:{cid},商品名称:{commodity_info['name']},商品单价:{commodity_info['price']}.")


print_commodity_price_less_than_2w(dict_commodity_infos)

print()
print("(3). 定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.")


def print_all_orders_info(list_orders, dict_commodity_infos):
    for order in list_orders:
        for cid, commodity_info in dict_commodity_infos.items():
            if order['cid'] == cid:
                print(f"商品名称:{commodity_info['name']},商品单价:{commodity_info['price']},数量:{order['count']}.")


print_all_orders_info(list_orders, dict_commodity_infos)

print()
print("(4). 定义函数,计算订单总价格：累加 (商品单价 * 数量)")


def calculate_total_order_price(list_orders, dict_commodity_infos):
    sum = 0
    for order in list_orders:
        for cid, commodity_info in dict_commodity_infos.items():
            if cid == order['cid']:
                sum += commodity_info['price'] * order['count']
    return sum


print(f"定单总价格为：{calculate_total_order_price(list_orders, dict_commodity_infos)}元。")

print()
print("(5). 查找数量最多的订单(使用自定义算法,不使用内置函数)")


def find_most_count_orders(list_orders, dict_commodity_infos):
    cid_max_count, max_count = list_orders[0]['cid'], list_orders[0]['count']
    for i in range(1, len(list_orders)):
        if list_orders[i]['count'] > max_count:
            cid_max_count = list_orders[i]['cid']
            max_count = list_orders[i]['count']

    for cid, commodity_info in dict_commodity_infos.items():
        if cid == cid_max_count:
            print(f"商品名称:{commodity_info['name']},商品单价:{commodity_info['price']},数量:{max_count}.")


find_most_count_orders(list_orders, dict_commodity_infos)

print()
print("(6). 根据购买数量对订单列表降序排列")


def sort_orders_by_count(list_orders):
    for i in range(len(list_orders) - 1):
        for j in range(i + 1, len(list_orders)):
            if list_orders[i]['count'] < list_orders[j]['count']:
                list_orders[i], list_orders[j] = list_orders[j], list_orders[i]
    return list_orders

print(sort_orders_by_count(list_orders))
