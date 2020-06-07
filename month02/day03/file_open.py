"""
打开文件示例
"""

# 打开文件
# f = open("4.txt","r") # 默认 r 

# f = open("file.txt","w") # 写 文件不存在创建存在情况

f = open("file.txt",'a') # 追加 文件存在追加

# 对文件读写
print(f)

# 关闭对象
f.close()  
