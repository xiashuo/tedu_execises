"""
    生成器应用
        在容器中,根据条件,返回结果.
        传统函数:return 容器
            缺点:占用内存过多
            优点:获取数据灵活(索引/切片)

        生成器函数:yield 元素
            优点: 节省内存
            缺点:获取数据不灵活(只能从头到尾使用一次)

        函数返回结果
            使用return  返回单个结果
            使用yield   返回多个结果
"""
list01 = [4,43,5,546,456,56,75,678]
# 练习1: 定义函数,创建列表存储所有偶数,并且返回列表.
def get_evens01():
    list_result = []
    for item in list01:
        if item % 2 == 0:
            list_result.append(item)
    return list_result

# 练习2: 定义函数,判断偶数,通过yield返回.
def get_evens02():
    for item in list01:
        if item % 2 == 0:
            yield item

# 调试,体会程序的差异性.
result01 = get_evens01()
for item in result01:
    print(item)
for item in result01: # 可以重复使用
    print(item)

result02 = get_evens02()
for item in result02:# 只能使用一次
    print(item)
for item in result02:
    print(item)

# 需求:获取第一个,最后一个结果
print(result01[0])
print(result01[-1])

print(result02[0])
print(result02[-1])