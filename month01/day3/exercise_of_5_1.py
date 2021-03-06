'''
给一个不多于 5 位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
# n = int(input("输入一个正整数："))
# count = 0
# n_reversed = ""
# while n:
#     count += 1
#     n_reversed += str(n % 10)
#     n //= 10
# print("该数是%d位数，逆序输出为：%s" % (count, n_reversed))
# 简洁版
# n_list = list(input("输入一个正整数："))
# n_list.reverse()
# print("该数是%d位数，逆序输出为：%s" % (len(n_list), ''.join(n_list)))

'''
定义张三的成绩，显示所获奖励，成绩100，爸爸买辆车，大于90小于100，妈妈买iPhone，大于60小于90，妈妈买参考书，小于60，什么都不买
'''
# score = float(input("输入张三的成绩："))
# if score == 100:
#     print("爸爸买辆车")
# elif score > 90:
#     print("妈妈买iPhone")
# elif score > 60:
#     print("妈妈买参考书")
# else:
#     print("什么都不买")

'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
可可提成7.5%；20万到40万之间时，低于20万元的部分按7.5%提成，高于20万元的部分，可提成5%；40万到60万之间时，低于40万元的部分按5%提成，高于40万元的部分，
可提成3%；60万到100万之间时，低于60万元的部分按3%提成，高于60万元的部分，可提成1.5%，高于100万元时，低于100万元的部分按1.5%提成，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
# I = float(input("输入当月利润I："))
# bonus = 0
# if I <= 10:
#     bonus = I * 0.1
# elif I < 20:
#     bonus = 10 * 0.1 + (I - 10) * 0.075
# elif I < 40:
#     bonus = 20 * 0.075 + (I - 20) * 0.05
# elif I < 60:
#     bonus = 40 * 0.05 + (I - 40) * 0.03
# elif I < 100:
#     bonus = 60 * 0.03 + (I - 60) * 0.015
# else:
#     bonus = 100 * 0.015 + (I - 100) * 0.01
# print("应发放奖金数为：%f万元" % bonus)

'''
输入某年某月某日，判断这一天是这一年的第几天？
'''
# year, month, day = map(int, input("输入年月日，中间以空格隔开：").split())
# '''
# 先按每个月30天算，然后加上有31天的月份，再减去闰年或平年2月份少的。找到规律：
# 除了month为9月和11月时，之前月份中有31天的月会多1个外，其他均为：month//2
# 还有就是要判断month是否大于2，否则不用减掉2月多算的天数。
# '''
# day_of_year = day + (month - 1) * 30 + month // 2
# if month == 9 or month == 11:
#     day_of_year += 1
# if year % 4 == 0 and year % 100 or year % 400 == 0:
#     if month > 2:
#         day_of_year -= 1
# else:
#     if month > 2:
#         day_of_year -= 2
# print("这一天是这一年的第%d天" % day_of_year)

'''
import time

# 字符类型的时间
year_month_day = input("输入年月日，输入格式为：年-月-日：")
# 转为时间数组
timeArray = time.strptime(year_month_day, "%Y-%m-%d")
timeStamp = int(time.mktime(timeArray))
# print(timeStamp)  # 输入时间的时间戳

btime = str(timeArray.tm_year) + "-01-01"
bArray = time.strptime(btime, "%Y-%m-%d")
bStamp = int(time.mktime(bArray))
# print(bStamp)  # 当前年一月一号的时间戳
day_of_year = int((timeStamp - bStamp) / (24 * 60 * 60)) + 1
print("这一天是这一年的第%d天" % day_of_year)
'''
'''
编写一个程序，找到所有可以被7整除但不是5的倍数的数字，2000至3200之间（均包括在内）。
获得的数字应以逗号分隔的顺序打印在一行上。
'''
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5:
        print(i, '', sep=',', end='')
