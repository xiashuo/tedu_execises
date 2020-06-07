'''
在终端中录入疫情地区名称，如果输入空字符串，则停止。
    如果录入的名称已经存在不要再次添加.
    最后倒序打印所有省份名称(一行一个)
    考点:如何记录不重复的地区
'''
list1=[]
while True:
    outbreak=input("输入疫情地区：")
    if outbreak=="":
        break
    if outbreak not in list1:
        list1.append(outbreak)
    else:
        print("录入的名称已经存在")
for i in range(len(list1)-1,-1,-1):
    print(list1[i])