"""
练习1 ：
从一个文本中查找单词： 编写一个而程序，input输入一个单词
获取这个单词的解释，打印出来。

提示 ： dict.txt
      每行一个单词
      单词与解释之间有空格
      单词有序排列 (后面的大于前面的)
"""

# 输入单词
word = input("单词:")

f = open("dict.txt") # 默认读方式

# 查单词
for line in f:
    w = line.split(' ') # 使用空格切割字符串 得到列表
    if w[0] > word:
        # 如果逐行查找到的单词已经比目标大来了，则不必再找了
        print("没有该单词")
        break
    elif word == w[0]:
        print(line)
        break
else:
    print("没有该单词")


f.close()








