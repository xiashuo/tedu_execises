"""
    异常处理
        不是针对语法错误(编码的时候),针对逻辑错误(运行的时候)
        逻辑错误:数据操作有效范围引发的错误.
"""


# 写法1:包治百病
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))  # ValueError
#         result = apple_count / person_count  # ZeroDivisionError
#         print("每人分%d个苹果" % result)
#     except:  # 相当于 except: Exception
#         print("程序出错啦")

# 写法2:对症下药
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))  # ValueError
#         result = apple_count / person_count  # ZeroDivisionError
#         print("每人分%d个苹果" % result)
#     except ValueError:
#         print("输入错误")
#     except ZeroDivisionError:
#         print("人数不能是零")

# 写法3:不做异常处理,但一定将某些逻辑执行.
# def div_apple(apple_count):
#     try:# 2  开门
#         person_count = int(input("请输入人数:"))  # ValueError
#         result = apple_count / person_count  # ZeroDivisionError
#         print("每人分%d个苹果" % result)
#     finally:# 3   关门
#         print("无论是否发生异常,都会执行的逻辑")
#
#
# try:
#     div_apple(10) # 1
# except:# 4
#     print("出错")

# 写法4:没有错误执行的逻辑
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))  # ValueError
        result = apple_count / person_count  # ZeroDivisionError
        print("每人分%d个苹果" % result)
    except:
        print("程序出错啦")
    else:
        print("没有错误执行的逻辑")


div_apple(10)
print("后续逻辑")
