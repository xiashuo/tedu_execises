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

print("打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.")
for cid, commodity_info in dict_commodity_infos.items():
    print(f"商品编号{cid},商品名称{commodity_info['name']},商品单价{commodity_info['price']}.")

print("打印所有订单信息,格式：订单编号xx,数量:xx.")
for order in list_orders:
    print(f"订单编号{order['cid']},数量:{order['count']}.")

print("打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.")
for order in list_orders:
    for cid, commodity_info in dict_commodity_infos.items():
        if cid == order['cid']:
            print(f"商品名称{commodity_info['name']},商品单价:{commodity_info['price']},数量{order['count']}.")

print("计算订单总价格：累加商品单价 * 数量")
total_orders_count = 0
for order in list_orders:
    for cid, commodity_info in dict_commodity_infos.items():
        if cid == order['cid']:
            total_orders_count += commodity_info['price'] * order['count']
print(f"订单总价格：{total_orders_count}元")

print("查找数量最少的订单(使用自定义算法,不使用内置函数)")
min_count_order = list_orders[0]
for i in range(1, len(list_orders)):
    if list_orders[i]['count'] < min_count_order['count']:
        min_count_order = list_orders[i]
print(f"数量最少的订单信息为：订单编号{min_count_order['cid']},数量:{min_count_order['count']}.")

print("根据单价,升序排列商品信息(使用自定义算法,不使用内置函数)")
# list_cids = [cid for cid in dict_commodity_infos.keys()]
# list_commodity_infos = [commodity_info for commodity_info in dict_commodity_infos.values()]
# for i in range(len(list_commodity_infos) - 1):
#     for j in range(i + 1, len(list_commodity_infos)):
#         if list_commodity_infos[j]['price'] < list_commodity_infos[i]['price']:
#             list_commodity_infos[i], list_commodity_infos[j] = list_commodity_infos[j], list_commodity_infos[i]
#             list_cids[i], list_cids[j] = list_cids[j], list_cids[i]
# reversed_dict_commodity_infos = {list_cids[i]: list_commodity_infos[i] for i in range(len(list_cids))}
# print(reversed_dict_commodity_infos)

list_commodity_infos = list(dict_commodity_infos.items())
for r in range(len(list_commodity_infos) - 1):
    for c in range(r + 1, len(list_commodity_infos)):
        if list_commodity_infos[r][1]["price"] > list_commodity_infos[c][1]["price"]:
            list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]
dict_commodity_infos = dict(list_commodity_infos)
print(dict_commodity_infos)


