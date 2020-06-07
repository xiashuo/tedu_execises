"""
    面向对象 设计思想
        封装/继承/多态
"""


# 需求:老张开车去东北
#      还有可能坐飞机/坐船/骑自行车....
# 缺点:违反面向对象设计原则
#   开闭原则: 增加飞机(Airplane)...,不允许修改人(Person)的代码.

#   封装           继承                多态
# 划分变化点

class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle, pos):
        print(self.name, "去", pos)
        # 如果是汽车...
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:  # 如果是飞机....
            vehicle.fly()


class Car:
    def run(self):
        print("汽车在行驶")


class Airplane:
    def fly(self):
        print("飞机在飞行")


lz = Person("老张")
c01 = Car()
lz.go_to(c01, "东北")
lz.go_to(Airplane(), "东北")
