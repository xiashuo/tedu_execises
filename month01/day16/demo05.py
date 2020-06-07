"""
    标准库模块
        time 对时间的处理
        文档: https://www.runoob.com/python3/python3-date-time.html
"""
import time

# 1. 计算机时间 -- 时间戳(从1970年1月1日0:0:0 UTC到现在经过的秒数)
# 1590117446.6454408
print(time.time())

# 2. 人类时间 --- UTC(世界世界)
# 今天: 2020年
# 秦始皇同一中国:公元前221年   -221
# 时间元组(年,月,日,时,分,秒,一周第几天,一年的第几天,夏令时)
tuple_time = time.localtime()
print(tuple_time)
print(tuple_time[0])  # 年份
print(tuple_time[6])  # 星期
print(tuple_time[-3])  # 星期

# 3. 时间戳 --> 时间元组
# 语法:时间元组 = time.localtime(时间戳)
tuple_time = time.localtime(1590117446.6454408)
print(tuple_time)

# 4. 时间元组 --> 时间戳
# 语法:时间戳 = time.mktime(时间元组)
print(time.mktime(tuple_time))
# 5. 时间元组 --> str
# 语法:字符串 = time.strftime(格式, 时间元组)
message = time.strftime("%y/%m/%d %H:%M:%S", tuple_time)
print(message)  # 20/05/22 11:17:26

# 6.  str --> 时间元组
# 语法: 时间元组 = time.strptime(需要转换的字符串,格式)
print(time.strptime("20/05/22 11:17:26", "%y/%m/%d %H:%M:%S"))
