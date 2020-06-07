"""
    2048 游戏核心算法
"""

list_merge = [2, 0, 2, 0]


# 1. 定义函数　zero_to_end()
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# zero_to_end()
# print(list_merge)


# 2. 定义函数　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
# [2,2,4,8]  --> [4,4,8,0]
def merge():
    """
        合并
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):  # -1：只需要前三个与下一个比较
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# merge()
# print(list_merge)

# (选做)day13作业
# 1. 创建全局变量二维列表作为2048地图
map = [
    [2, 0, 0, 2],
    [4, 4, 0, 8],
    [4, 0, 4, 2],
    [8, 2, 2, 0],
]


# 按行打印map
def print_map():
    for line in map:
        print(line)


print_map()


# 矩阵转置
def transpose_map():
    # global map
    # map = [[map[i][j] for i in range(len(map))] for j in range(len(map[0]))]
    for i in range(len(map) - 1):
        for j in range(i + 1, len(map)):
            map[i][j], map[j][i] = map[j][i], map[i][j]


# print_map()
# transpose_map()
# print_map()


# 2. 创建函数,向左移动
# 将map中的每行,赋值给全局变量list_merge
# 调用merge函数
# list_merge[0] = 1  # 读取全局变量
# list_merge = 2  # 修改全局变量
def move_left():
    global list_merge
    for i in range(len(map)):
        list_merge = map[i]
        merge()


print("向左移动：")
move_left()
print_map()


# 3. 创建函数，向右移动
# 提示：调用merge实现
def move_right():
    global list_merge
    for i in range(len(map)):
        list_merge = map[i][::-1]
        merge()
        map[i] = list_merge[::-1]


print("向右移动：")
move_right()
print_map()


# 向上移动
def move_up():
    # global list_merge
    # for j in range(len(map[0])):
    #     list_merge = [map[i][j] for i in range(len(map))]
    #     merge()
    #     for i in range(len(map)):
    #         map[i][j] = list_merge[i]
    transpose_map()
    move_left()
    transpose_map()


print("向上移动：")
move_up()
print_map()


# 向下移动
def move_down():
    # global list_merge
    # for j in range(len(map[0])):
    #     list_merge = [map[i][j] for i in range(len(map) - 1, -1, -1)]
    #     merge()
    #     for i in range(len(map)):
    #         map[i][j] = list_merge[-i - 1]
    transpose_map()
    move_right()
    transpose_map()


print("向下移动：")
move_down()
print_map()
