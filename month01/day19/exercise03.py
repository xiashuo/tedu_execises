"""
    使用装饰器，增加打印函数执行时间的功能.
"""
import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        print("执行时间是", stop_time - start_time)
        return result

    return wrapper


@print_execute_time
def func01(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(func01(10))
print(func01(10000000))
