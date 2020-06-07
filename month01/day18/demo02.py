"""
    函数式编程应用
        与面向对象思想异曲同工
            封装     --    分(变化)
            继承     --    隔(变化)
            多态     --    做(变化)



"""


# 需求:
# (1)定义函数,对列表进行操作,找出所有大于10的数字
def find01(list_target):
    for item in list_target:
        if item > 10:
            yield item


# (2)定义函数,对列表进行操作,找出所有小于5的数字
def find02(list_target):
    for item in list_target:
        if item < 5:
            yield item


for number in find01([134, 432, 54, 5, 56, 67, 78, 8]):
    print(number)


# 分 -- 将多个函数的核心变化点(条件)单独定义到函数
def condition01(item):  # condition01 相当于火车
    return item > 10


def condition02(item):  # condition02 相当于飞机
    return item < 5


# 隔 -- 使用参数隔离需要调用的具体/变化/核心的函数

# 万能查找(在什么数据中,根据什么条件,都是参数)
def find(list_target, func):  # find 相当于老张
    for item in list_target:
        # if item > 10:
        # if condition01(item):  # 老张 调用 汽车 去东北
        if func(item):  # 老张 调用 交通工具 去东北
            yield item


# 后续无限增加新条件
def condition03(item):
    return item % 2 != 0


# 做 --  不变(变化)
for item in find([34, 32, 4, 54, 65, 76], condition03):
    print(item)
