"""
    多继承
        同名方法解析顺序
"""


class A:
    def func01(self):
        print("A -- func01")


class B(A):
    def func01(self):
        print("B -- func01")


class C(A):
    def func01(self):
        print("C -- func01")


class D(B, C):
    def func01(self):
        print("D -- func01")
        super().func01() # 只执行继承列表中的第一个同名方法
        # 2. 调用继承列表中指定类型方法
        # C.func01(self)  # 通过类名调用

d = D()
d.func01()
# 1. 解析顺序:类自身 --> 父类继承列表（由左至右）--> 再上层父类
#            以类型的mro函数为准.
print(D.mro())

