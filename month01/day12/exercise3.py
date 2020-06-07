'''
list01 = [6,2,3,4,5,6,7,3,2,4,8]
    定义函数,删除列表中重复元素.(不使用其他容器,自定义算法)
'''
list01 = [6, 2, 3, 4, 5, 6, 7, 3, 2, 4, 8]


def delete_duplicate_elements(list_target):
    for i in range(len(list_target) - 1, 0, -1):
        for j in range(i):
            if list_target[i] == list_target[j]:
                del list_target[i]
                break
    return list_target


delete_duplicate_elements(list01)
print(list01)
