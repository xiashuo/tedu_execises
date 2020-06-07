'''
计算给定字符串列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
   字符串列表：words =["qtx","看一看","想啊想","练练"]
'''
words = ["qtx", "看一看", "想啊想", "练练"]
count = 0
for val in words:
    if len(val) > 2 and val[0] == val[-1]:
        count += 1
print(count)
