"""
    多态 -- 内置可重写函数
        重写:子类与父类方法相同(名称/参数)
        __str__
"""


# class Commodity(object):
class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return "%s的编号是%d,单价是%d"%(self.name,self.cid, self.price)

kz = Commodity(1001, "口罩", 30)
# <__main__.Commodity object at 0x7f74c5a1f208>
# print(kz)
content = kz.__str__() # 如果儿子没有,将执行爸爸的.
print(content)

