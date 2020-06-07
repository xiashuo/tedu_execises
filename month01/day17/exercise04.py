"""

"""


# class MyRangeIterator:# 迭代器
#     def __init__(self,data_end):
#         self.data_end = data_end
#         self.index = -1
#
#     def __next__(self):
#         # 数据如果到了最大值,则停止迭代.
#         if self.index > self.data_end - 2:
#             raise StopIteration()
#         self.index += 1
#         return self.index

class MyRange:  # 可迭代对象
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        index = 0
        while index < self.end:
            yield index
            index += 1


for number in MyRange(5):  # 0 1 2 3 4
    print(number)

# iterator = MyRange(5).__iter__()
# while True:
#     # 2. 获取下一个元素
#     try:
#         item = iterator.__next__()
#         print(item)
#     # 3. 如果抛出停止迭代异常,则跳出循环
#     except StopIteration:
#         break
