"""
    lambda 表达式语法: 匿名函数
        变量 = lambda 参数:函数体
        形参 = 实参
    练习:exercise04
"""

# 1. 有参数,有返回值
# def func01(p1, p2):
#     return p1 > p2
#
# result = func01(10,20)
# print(result)

func01 = lambda p1, p2: p1 > p2
result = func01(10, 20)
print(result)

# 2. 有参数,无返回值
# def func02(p1)
#     print("参数是:" + p1)
#
# func02("悟空")

func02 = lambda p1: print("参数是:" + p1)
func02("悟空")

# 3. 无参数,有返回值
# def func03()
#     return 250
#
# result = func03()
# print(result)

func03 = lambda: 250
result = func03()
print(result)

# 4. 无参数,无返回值
# def func04():
#     print("大家好,才是真的好")
#
# func04()
func04 = lambda: print("大家好,才是真的好")
func04()


# 注意: def 定义的传统函数,但是不能用lambda.
#  (1) lambda 表达式,不支持赋值语句.
def func05(p1):
    p1[0] = 10


list01 = [1]
func05(list01)
print(list01)  # [10]


# func05 = lambda p1: p1[0] = 10
# (2) lambda 表达式,不支持多行语句
def func06():
    for number in range(5):
        print(number)


func06()

# func06 = lambda : for number in range(5):
#                      print(number)
