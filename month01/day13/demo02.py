"""
    多态 -- 内置可重写函数
        重写:子类与父类方法相同(名称/参数)
"""


class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price

    # 对象 --> 字符串 : 没有语法限制,根据需求灵活自由的选择字符串格式
    # 适用性：　给人看
    # def __str__(self):
    #     return "%s的编号是%d,单价是%d"%(self.name,self.cid, self.price)

    # 对象 --> 字符串 : 有语法限制,按照创建对象的Python语法格式
    # 适用性：　机器干(执行)　
    def __repr__(self):
        return 'Commodity(%d, "%s", %d)' % (self.cid, self.name, self.price)


# 创建对象
kz1 = Commodity(1001, "口罩", 30)
# 与eval函数配合

# eval函数: 将字符串作为Python代码执行
# re = eval("1+2*3")
# print(re)# 7

# 在终端中输入的内容,将作为代码执行.  "无所不能"
# eval(input())

# 获取该对象的实例化代码
str_code = kz1.__repr__() # 'Commodity(1001, "口罩", 30)'
kz2 = eval(str_code)

# 拷贝
kz1.price = 50
print(kz2.price)