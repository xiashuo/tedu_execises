"""
文件写操作示例
"""

# 写打开
f = open("file.txt","w")

# 追加 不清除原有内容
# f = open("file.txt",'ab')

# n = f.write("感恩白衣死战，龙魂不死\n".encode())
# print("写入了%d个字节"%n)
# n = f.write("此生无悔入华夏，来世还做中国人\n".encode())
# print("写入了%d个字节"%n)

# 写入列表内容 也需要自己添加换行
l = ["哈喽，死鬼\n",'哎呀，干啥\n']
f.writelines(l)


f.close()