from multiprocessing import Process
from tools.my_tools import MyTools


def get_prime_sum(l, n):
    s = 0
    for i in range(l, n + 1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            s += i
    print(f"({l},{n})结束")
    return s


@MyTools.get_running_time
def process_n(n):
    jobs = []
    for i in range(n):
        p = Process(target=get_prime_sum, args=(i * (100000 // n), (i + 1) * (100000 // n)))
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()


process_n(10)
