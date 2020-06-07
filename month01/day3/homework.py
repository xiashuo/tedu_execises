'''
(1)
'''
'''
input_number = 8
random_number = 8
if input_number == random_number:
    print("猜对了")
else:
    print("猜错了")
'''

'''
(2)
'''
# num = 12
# if num > 3:
#     print("⼤于3")
# elif num > 5:
#     print("⼤于5")
# elif num > 10:
#     print("⼤于10")
# elif num > 15:
#     print("⼤于10")

'''
(3)
'''
# str_value = " "
# new_str = str_value if str_value else "empty"
# print(new_str)

'''
(1) 电梯设置规定：
            如果承载⼈不超过10⼈，且总重量不超过1000千克，可以正常使⽤，否则提示超载。
        步骤:
            终端中获取人数/总重量
            显示电梯正常运行
                电梯超载
'''
# if int(input("输入电梯人数："))<=10 and float(input("输入总重量(千克)："))<=1000:
#     print("电梯正常运行")
# else:
#     print("电梯超载")

'''
(2) 根据年龄，输出对应的人生阶段。
            年龄       ⼈⽣阶段
            0-6 岁      童年
            7-17 岁     少年
            18-40 岁    ⻘年
            41-65 岁    中年
            65 岁之后    ⽼年
        步骤:
            终端中获取年龄
            显示人生阶段
'''
# age = int(input("输入年龄："))
# if 0 <= age <= 6:
#     print("童年")
# elif age <= 17:
#     print("少年")
# elif age <= 40:
#     print("青年")
# elif age <= 65:
#     print("中年")
# else:
#     print("老年")

'''
(3) 如果是vip客户,消费小于等于500,享受85折
                    消费大于500,享受8折
        如果不是vip客户,消费大于等于800,享受9折
                      消费小于800,原价
        在终端中输入账户类型,消费金额,计算折扣.
        循环计算折扣,直到账户输入空字符串结束
'''
# while True:
#     account_type = input("账户类型：")
#     if account_type=='':
#         print("结束")
#         break
#     consumption = float(input("消费金额:"))
#     if account_type == "vip客户":
#         if consumption <= 500:
#             print("折扣为：" + str(consumption * 0.15))
#         else:
#             print("折扣为：" + str(consumption * 0.2))
#     else:
#         if consumption < 800:
#             print("折扣为：0")
#         else:
#             print("折扣为：" + str(consumption * 0.1))

'''
(4) 梯形面积： （上底 + 下底) * 高  / 2
        在终端中获取上底/下底/高
        打印面积
'''
# upper_base = float(input("上底："))
# the_bottom = float(input("下底："))
# height = float(input("高："))
# print("面积为：" + str((upper_base + the_bottom) * height / 2))

'''
(5) 小泽老师很不幸,买了一箱有虫子(1只)的苹果
        虫子吃完一个苹果再吃另外一个苹果
        在终端中输入苹果数量(个),虫子吃苹果的速度(小时/个),经过时间(小时)
        请打印没有被虫子吃过的苹果数量（整数,最小也是0）

'''
# apple_number = int(input("苹果数量（个）："))
# apple_eating_speed = float(input("虫子吃苹果的速度(小时/个)："))
# time = float(input("经过时间(小时)："))
# number_good_apples = (apple_number - time / apple_eating_speed) // 1
# print("没有被虫子吃过的苹果数量为：%d个" % number_good_apples)

'''
(6) while 循环累加练习
        使用while循环累加下列数字：0 + 1 + 2 + 3
        使用while循环累加下列数字：2 + 3 + 4 + 5 + 6
        使用while循环累加下列数字：1 + 3 + 5 + 7
        使用while循环累加下列数字：8 + 7 + 6 + 5 + 4
        使用while循环累加下列数字：-1+  -2 + -3 + -4 + -5
'''
# # 使用while循环累加下列数字：0 + 1 + 2 + 3
# i, s = 0, 0
# while i <= 3:
#     s += i
#     i += 1
# print(s)
# # 使用while循环累加下列数字：2 + 3 + 4 + 5 + 6
# i, s = 2, 0
# while i <= 6:
#     s += i
#     i += 1
# print(s)
# # 使用while循环累加下列数字：1 + 3 + 5 + 7
# i, s = 1, 0
# while i <= 7:
#     s += i
#     i += 2
# print(s)
# # 使用while循环累加下列数字：8 + 7 + 6 + 5 + 4
# i, s = 8, 0
# while i >= 4:
#     s += i
#     i -= 1
# print(s)
# # 使用while循环累加下列数字：-1+  -2 + -3 + -4 + -5
# i, s = -1, 0
# while i >= -5:
#     s += i
#     i -= 1
# print(s)
