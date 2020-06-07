"""
    重写　算数运算符
"""

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self # 可变对象,尽量在原有基础上修改(返回原始对象)


pos01 = Vector2(1, 2)
pos01 += Vector2(3, 4) # 本质: pos01.__iadd__(pos02)
print(pos01.x, pos01.y)

# 可变对象+=前后是同一对象
list01 = [1]
print(id(list01))  # 140046617805192
list01 += [2]
print(id(list01))  # 140046617805192
print(list01)  # [1, 2]

# 不可变对象+=前后不是同一对象(创新新对象)
tuple01 = (1,)
print(id(tuple01))  # 140224199621768
tuple01 += (2,)
print(id(tuple01))  # 140224169166984
print(tuple01)  # (1, 2)
