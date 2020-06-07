"""
    模块相关知识点
"""
# from module01 import *
#
# func01()
# 1. __all__ 和 隐藏成员,都不管用.
from module01 import func02# 没有加入到可导出列表
from module01 import _func03# 隐藏成员

func02()# 都能使用
_func03()# 都能使用

# 2. 可以获取模块文档字符串
import module01
print(module01.__doc__)

# 3. 获取模块的完整路径
print(module01.__file__)