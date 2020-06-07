'''
通过属性限制数据范围,体会属性的继承
    父类：车(品牌，速度)
                 0-280
    创建子类：电动车(电池容量,充电功率)
                  0 - 50000  200 - 250
'''


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 280:
            self.__speed = value
        else:
            raise Exception("速度超过范围！")


class Electrocar(Car):
    def __init__(self, brand, speed, battery_capacity, charge_power):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charge_power = charge_power

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if 0 <= value <= 50000:
            self.__battery_capacity = value
        else:
            raise Exception("电池容量超过范围！")

    @property
    def charge_power(self):
        return self.__charge_power

    @charge_power.setter
    def charge_power(self, value):
        if 200 <= value <= 250:
            self.__charge_power = value
        else:
            raise Exception("充电功率超过范围！")


electrocar01 = Electrocar("艾玛", 200, 30000, 200)
print(electrocar01.__dict__)
