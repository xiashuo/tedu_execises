"""
    重写　算数运算符
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 自定义对象可以使用+符号
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)


pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
pos03 = pos01 + pos02  # 本质: pos01.__add__(pos02)
print(pos03.x)  # 4
print(pos03.y)  # 6
