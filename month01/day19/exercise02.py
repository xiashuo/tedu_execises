"""
    练习:使用装饰器，为旧功能增加新功能.
"""

def print_fun(func):# 拦截（调用旧功能，执行内部函数）
    def wrapper(*args, **kwargs):# 包裹（执行新+旧功能）
        print("执行了", func.__name__, "函数")
        return func(*args, **kwargs)
    return wrapper


# 新功能
# def print_func(func):
#     print("执行了", func.__name__, "函数")

# 旧功能
@print_fun
def insert(data):
    # print_func(insert)
    print("插入", data, "成功")

@print_fun
def delete(id):
    # print_func(delete)
    print("删除", id, "成功")

insert("ok")

delete(1001)
