"""
    生成器表达式
    练习:exercise07
"""
list01 = [34, 4, 54, 56, 6, 67, 87]
# 创建list02存储,list01中大于10的数字.
# list02 = []
# for item in list01:fdf
#     if item > 10:
#         list02.append(item)
list03 = [item for item in list01 if item > 10]
for item in list03:
    print(item)

# def get_numbers():
#     for item in list01:
#         if item > 10:
#             yield
#
# result = get_numbers()
# for item in result:
#     print(item)

result = (item for item in list01 if item > 10)
for item in result:
    print(item)
