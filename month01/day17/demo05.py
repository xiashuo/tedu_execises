"""
    内置生成器
        enumerate
            for 索引, 元素 in enumerate(可迭代对象):
"""
list01 = [4, 5, 5, 6, 76, 87]

# for i in range(len(list01)):
#     if list01[i] < 10:
#         list01[i] = 0

for i, item in enumerate(list01):
    if item < 10:  # 判断元素是否满足条件
        list01[i] = 0  # 通过修改元素

print(list01)


