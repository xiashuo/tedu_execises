'''
(选做) 2048 核心算法
    1. 定义全局变量
        list_merge = [2,0,2,0]

    2. 定义函数,将list_merge的零元素移动到末尾　zero_to_end()
         [2,0,2,0]  -->  [2,2,0,0]
         [2,0,0,2]  -->  [2,2,0,0]
         [2,4,0,2]  -->  [2,4,2,0]

    3. 定义函数,将list_merge的相同元素合并 merge()
         [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
         [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
         [4,4,4,4]  -->  [8,8,0,0]
         [2,0,4,2]  -->  [2,4,2,0]
         [2,2,4,8]
'''
# 定义全局变量
list_merge = [2, 0, 0, 8]


# 定义函数,将list_merge的零元素移动到末尾
def zero_to_end():
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


zero_to_end()
print(list_merge)


# 定义函数,将list_merge的相同元素合并
def merge():
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


list_merge = [4, 2, 2, 0]
merge()
print(list_merge)
