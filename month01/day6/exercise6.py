'''
(选做)斐波那契数列：从第三项开始,每一项都等于前两项之和。
        在终端中获取长度,创建斐波那契数列。
        演示：
            请输入斐波那契数列长度：8
            [1, 1, 2, 3, 5, 8, 13, 21]
        提示: 列表初始值: [1,1]
'''
fibonacci_list = [1, 1]
fibonacci_length = int(input("输入斐波拉契数列长度："))
if fibonacci_length==1:
    fibonacci_list=[1]
for i in range(2, fibonacci_length):
    fibonacci_list.append(fibonacci_list[i - 2] + fibonacci_list[i - 1])

print(fibonacci_list)
