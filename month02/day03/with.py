"""
with 语句块使用
"""

# 产生文件对象，简单使用
with open('file.txt','r+') as f:
    data = f.read(4)
    print(data)
    f.write("Hello world")

# 语句块结束自动关闭f