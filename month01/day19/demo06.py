"""
    装饰器 -- 语法细节
        内部函数返回值是旧功能的返回值
        装饰器可以拦截任意参数的函数
            合 + 拆
"""
def verif_permissions(func):
    def wrapper(*args,**kwargs): # 让实参数量无限  合一
        print("验证权限")# 新功能
        # (2)内部函数返回值是旧功能的返回值
        return func(*args,**kwargs) # 旧功能          拆多
    return wrapper

@verif_permissions
def delete_order(oid):
    print(f"删除{oid}订单")

result = delete_order(1001,1002,1003)
print(result)

@verif_permissions
def enter_background():
    print("进入后台")
    return "进入"

# (1)调用的是内部函数，接收到的返回值，是内部函数返回值.
# (3)因为(1)(2),所以result存储的是旧功能返回值
result = enter_background()
print(result)


