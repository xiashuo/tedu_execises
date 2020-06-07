'''
练习 ： 编写一个程序，列出指定目录（input输入）下所有大小超过 1024字节的普通文件文件名
'''
import os

res = []
path = "../day03"
for dir in os.listdir(path):
    is_file = os.path.isfile(path + "/" + dir)
    size = os.path.getsize(path + "/" + dir)
    if is_file and size > 1024:
        res.append(dir)
print(res)
