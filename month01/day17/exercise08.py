# 练习:打印字典中所有键值对的同时,打印索引.
dict01 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# for item in enumerate(dict01.items()):
#     # print(item)# (0, (1, 1))
#     print(f"编号是{item[0]},键是{item[1][0]},值是{item[1][1]}")

for i, (key, value) in enumerate(dict01.items()):
    print(f"编号是{i},键是{key},值是{value}")
