from threading import Thread, Lock
from time import sleep


def print_alphabet():
    for i in range(65, 91):
        lock1.acquire()
        print(chr(i), end='')
        lock2.release()


def print_digit():
    for i in range(1, 53, 2):
        lock2.acquire()
        print(i, end='')
        print(i + 1, end='')
        lock1.release()


lock1 = Lock()
lock2 = Lock()
lock1.acquire()
t1 = Thread(target=print_alphabet)
t2 = Thread(target=print_digit)
t1.start()
t2.start()
t1.join()
t2.join()
