'''
在终端中循环录入年龄,如果录入空,则退出循环.最后打印平均年龄(总年龄除以人数)
'''
sum_age, count = 0, 0
while True:
    age = input("输入年龄：")
    if age == "":
        break
    sum_age += int(age)
    count += 1
print(f"输入的平均年龄为：{sum_age / count}")
