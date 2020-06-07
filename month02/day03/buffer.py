"""
缓冲区细节示例
"""

# f = open("file.txt",'w+',buffering=1) # 行缓冲 ，换行刷新缓冲区
f = open("file.txt",'wb+',buffering=10) # 缓冲区大小10字节

# 循环输入内容，写入文件
while True:
    msg = input(">>")
    if not msg:
        break
    f.write(msg.encode()) # 转换为字节串

    # f.write(msg+'\n')
    # f.flush() # 刷新缓冲

f.close()