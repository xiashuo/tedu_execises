"""
    装饰器
        不改变原函数      增加新功能
"""
def verif_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")# 新功能
        return func(*args, **kwargs) # 旧功能
    return wrapper

# 新功能
# def verif_permissions():
#     print("验证权限")

# 旧功能
@verif_permissions # enter_background = verif_permissions(enter_background)
def enter_background():
    print("进入后台")


def delete_order():
    print("删除订单")

# 调用外函数，返回内函数
# enter_background = verif_permissions(enter_background)
# 调用内函数(新 + 旧)
enter_background()

delete_order()


"""
class Wife:
    def __init__(self,age):
        self.age=age
    
    @property  # age = property(age，None)
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value
"""