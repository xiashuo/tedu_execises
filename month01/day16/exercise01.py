"""
    定义函数,根据年/月/日三个参数,获取星期.
        星期一
        星期二
        ...
        星期日
"""
import time


def get_week(year, month, day):
    # 语法: 时间元组 = time.strptime(需要转换的字符串,格式)
    tuple_time = time.strptime(f"{year}/{month}/{day}", "%Y/%m/%d")
    tuple_weeks = ("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
    return tuple_weeks[tuple_time[6]]


print(get_week(2020, 5, 22))
