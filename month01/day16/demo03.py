"""
    导入包
"""
# from 路径.模块 import 成员
# from package01.module01 import func01

# func01()

# from 包 import 模块
# from package01 import module01
# module01.func01()

# from 包 import *
# 注意:必须要在包的__init__.py文件中,设置__all__.
from package01 import *

module01.func01()
