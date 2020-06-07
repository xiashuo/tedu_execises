
'''
参照下列代码,定义函数,打印矩形
    side_length = int(input("输入边长:"))  # 5
    for item in range(1, side_length + 1):
        # 第一行 或者 最后一行
        if item == 1 or item == side_length:
            print("*" * side_length)
        else:  # 中间行
            #  " " * (side_length - 2)  空格重复多次
            print("*%s*" % (" " * (side_length - 2)))
            # print(f"*{' ' * (side_length - 2)}*")
'''
def print_rectangle(side_length):
    for item in range(1, side_length + 1):
        # 第一行 或者 最后一行
        if item == 1 or item == side_length:
            print("*" * side_length)
        else:  # 中间行
            #  " " * (side_length - 2)  空格重复多次
            print("*%s*" % (" " * (side_length - 2)))
            # print(f"*{' ' * (side_length - 2)}*")
print_rectangle(5)