"""
文件偏移量细节示例
"""
f = open("file.txt",'wb+')


f.write(b"Hello world\n")
f.flush() # 内容写入文件

print("文件偏移量位置:",f.tell())

# 重置文件偏移量位置
f.seek(-3,2)

data = f.read()
print(data)

f.close()