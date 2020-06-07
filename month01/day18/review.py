"""
    复习
        迭代:每次重复都在上一次的基础上进行.
            可迭代对象:__iter__
            迭代器:__next__

        生成器:可迭代对象 + 迭代器
            价值:循环一次计算一次返回一次
                推算数据的对象
                day17/exercise02.py

                传统思想:使用容器存储所有结果
                def 函数():
                    结果 = []
                    循环向结果中添加数据
                    return 结果

                生成器思想: 使用 yield 返回数据
                def 函数():
                    循环 yield 数据

                函数()  # 直接调用不执行

                for 变量 in 函数(): # for的内部循环调用__next__让函数逐步执行.
                    ....

                容器名称(函数()) # 将生成器转换为容器,内部让生成器生成所有数据

                总结:函数返回单个结果使用return,返回多个结果使用yield
"""


def func01():
    yield 10


result = func01()
print(result)  # 返回值是生成器对象(负责推算数据的对象)

for item in result:
    print(item)  # 10
