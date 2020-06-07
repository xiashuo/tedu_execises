"""
      yield --> 生成器函数
"""
"""
class Generator:＃ 生成器 = 可迭代对象 + 迭代器
    def __iter__(self):＃　可迭代对象
        return self
    
    def __next__(self):＃　迭代器
        ...
        return ...
"""


def my_range(end):
    index = 0
    while index < end:
        yield index
        index += 1

# 延迟/惰性操作(函数不执行,等待__next__方法被调用)
range = my_range(100) # 内部在创建生成器对象  Generator(5)
print(range)
for number in range:  # 0 1 2 3 4
    print(number)

iterator = range.__iter__() # 返回生成器对象地址
while True:
    # 2. 获取下一个元素
    try:
        item = iterator.__next__() #
        print(item)
    # 3. 如果抛出停止迭代异常,则跳出循环
    except StopIteration:
        break
