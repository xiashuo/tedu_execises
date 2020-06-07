"""
    模块
        创建文件夹作为项目根目录student_manager_system
            创建bll.py文件,业务business 逻辑logic 层layer,负责存储XXController
            创建usl.py文件,用户user 显示show 层layer,负责存储XXView
            创建model.py文件,负责存储XXModel
            [主模块]  创建main.py文件,负责存储入口代码
                主模块不会生成pyc文件,被导入的模块才会生成.
                pyc文件是源代码到机器码中间的语言,可以加快程序的执行速度.
"""
# 在pycharm中设置根目录:
# 右键 --> mark directory --> Sources roots

# 导入写法1: import 文件名
#    使用: 文件名.成员
# 适合面向过程的技术
import module01

module01.func01()

c01 = module01.MyClass()
c01.func02()

# 导入写法2: from  文件名 import 成员名
#    使用: 成员名
# 适合面向对象的技术
# from module01 import func01
# from module01 import MyClass
from module01 import func01, MyClass

func01()

c01 = MyClass()
c01.func02()

# 导入写法3: from  文件名 import *
#    使用: 成员名
# 适合面向对象的技术
# 小心: 导入的成员命名冲突
from module01 import *

func01()

c01 = MyClass()
c01.func02()
