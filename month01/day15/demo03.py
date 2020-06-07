"""
    包

文件夹(根目录)
    包
        模块
            类
                函数
                    语句
"""
# 方式1: import 路径.模块 as 别名
import package01.package02.m01 as m

m.func01()

# 方式2: from  路径.模块 import 内容
from package01.package02.m01 import func01

func01()

# 方式3: from  路径.模块 import 内容
from package01.package02.m01 import *

func01()
