"""
    内置生成器
        zip
    练习:exercise09
"""
list01 = ["张无忌", "赵敏", "周芷若"]
list02 = [1001, 1002, 1003]
# 同时获取多个可迭代对象中的元素
for item in zip(list01, list02):
    print(item)

