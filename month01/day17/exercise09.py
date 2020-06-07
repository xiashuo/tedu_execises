# 练习:通知zip实现矩阵转职(行 --> 列)
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# for item in zip(list01[0], list01[1], list01[2], list01[3]):
#     print(item)# (1, 5, 9, 13)

# 复习函数参数
# for item in zip(*list01):    # 拆
#     print(item)

# [(1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15), (4, 8, 12, 16)]
# list02 = list(zip(*list01))

list03 = [list(item) for item in zip(*list01)]
print(list03)
