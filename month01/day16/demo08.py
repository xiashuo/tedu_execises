"""
    迭代iter
        迭代 : 一次次获取下一个元素的过程
        可迭代对象:能够返回迭代器的对象    可迭代对象.__iter__()
        迭代器:
            一次次获取下一个元素的对象
            迭代器 = 可迭代对象.__iter__()
"""
list01 = [2, 43, 4, 5, 6, 1]
for item in list01:
    print(item)

# for 循环原理(迭代过程):
# 1. 获取迭代器
iterator = list01.__iter__()
while True:
    try:
        # 2. 通过迭代器获取下一个元素
        item = iterator.__next__()
        print(item)
        # 3. 如果发现异常StopIteration,停止循环
    except StopIteration:
        break



# 面试题:对象能够被for的条件是?
#      能够获取迭代器的对象
#      (对象具有__iter__函数)
