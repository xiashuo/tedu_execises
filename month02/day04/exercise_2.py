"""
编写一个程序，列出指定目录（input输入）下
所有大小超过 1024字节的普通文件文件名
"""
import os

dir = input(">>") # 要检测的文件夹

for file in os.listdir(dir):
    # 判断文件是否为普通文件 (注意添加路径)
    if os.path.isfile(dir+'/'+file):
        # 判断大小
        if os.path.getsize(dir+'/'+file) > 1024:
            print(file)


