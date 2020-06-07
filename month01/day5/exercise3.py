'''
将列表中整数的个位不是5和3的数字存入另外一个列表
    list03 = [25, 63, 27, 75, 70, 83, 27]
    结果:[27, 70, 27]
'''
list01 = [25, 63, 27, 75, 70, 83, 27]
list02 = []
for val in list01:
    if val % 10 != 5 and val % 10 != 3:
        list02.append(val)
print(list02)
