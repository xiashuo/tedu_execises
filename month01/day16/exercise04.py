"""
   写出for元组的原理
   写出for字典的原理(不使用for,获取字典键值对)
"""
tuple01 = (3, 54, 5, 56, 6, 7, 8)
# for item in tuple01:
#     print(item)
iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

dict01 = {"a": "A", "b": "B", "c": "C"}
# for key in dict01:
#     print(key)
#     print(dict01[key])

iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key)
        print(dict01[key])
    except StopIteration:
        break
