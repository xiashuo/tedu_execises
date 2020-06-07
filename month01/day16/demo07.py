"""
    raise : 人为创造异常
        目的:快速传递错误信息

"""


class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 22 <= value <= 30:
            self.__age = value
        else:
            # 人为创造异常(给24行传递错误消息)
            raise Exception("年龄超过范围", 1001, "if 22 <= value <= 30")  # 抛出


while True:
    try:
        age = int(input("请输入老婆年龄"))
        w01 = Wife(age)
        print(w01.age)
        break
    except Exception as e:  # 接收
        print(e.args)  # ('年龄超过范围', 1001, 'if 22 <= value <= 30')

print("老婆娶到手")
