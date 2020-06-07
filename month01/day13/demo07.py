"""
    面向对象 设计思想
"""


# -------------------架构----------------------
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle, pos):
        print(self.name, "去", pos)
        # 先用:交通工具
        vehicle.transport()


class Vehicle:
    """
        交通工具
    """

    def transport(self):
        pass


# -------------------程序员----------------------
# 后做:继承交通工具,重写方法
class Car(Vehicle):
    def transport(self):
        print("汽车在行驶")


class Airplane(Vehicle):
    # 快捷键:ctrl + o
    def transport(self):
        print("飞机在飞行")


lz = Person("老张")
c01 = Car()
lz.go_to(c01, "东北")
lz.go_to(Airplane(), "东北")
