'''
编写一个函数求100000以内质数之合 --》 统计函数执行时间（装饰器）
'''
import time
def get_running_time(func):
    def wraper(*args,**kwargs):
        start_time=time.time()
        s=func(*args,**kwargs)
        end_time=time.time()
        print(f"函数执行时间为：{end_time-start_time:.2f}秒")
        return s
    return wraper

@get_running_time
def get_prime_sum(n):
    s = 0
    for i in range(2, n + 1):
        for j in range(2, i//2+1):
            if i % j == 0:
                break
        else:
            s += i
    return s

n=100000
print(f"{n}以内的所有质数之和为：{get_prime_sum(n)}")
