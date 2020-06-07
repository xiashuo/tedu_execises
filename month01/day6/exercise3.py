'''
将列表中所有元素转换为一个字符串
   列表:["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
   结果:我爱你python666
'''
list1=["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
str1="".join([str(char) for char in list1])
print(str1)
