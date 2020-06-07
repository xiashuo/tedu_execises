"""
    module01 模块
"""
# 定义可导出成员:  "给你"
# __all__ = ["func01"]

def func01():
    print("func01执行喽")

def func02():
    print("func01执行喽")

# 隐藏成员:如果使用 from xx import *导入模块,不会导入隐藏成员   "不给"
#        以单下划线命名
def _func03():
    print("func03执行喽")
