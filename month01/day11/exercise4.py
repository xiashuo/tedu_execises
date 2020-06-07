'''
(选做)定义函数,从列表中删除多个元素(有坑)
        -- 定义函数,将列表中奇数设置为1
        -- 定义函数,将列表中奇数删除
        测试数据:[3,4,5,6,7,8,9]
'''

list01 = [3, 4, 5, 6, 7, 8, 9]


def delete_multiple_elements_of_list(list_, *value):
    print("从列表中删除多个元素")
    for v in value:
        if v in list_:
            list_.remove(v)
    return list_


print(delete_multiple_elements_of_list(list01, 4, 7, 1))

list01 = [3, 4, 5, 6, 7, 8, 9]


def set_odd_number_to_1(list_):
    for i in range(len(list_)):
        if list_[i] % 2 == 1:
            list_[i] = 1
    return list_


print(set_odd_number_to_1(list01))

list01 = [3, 4, 5, 6, 7, 8, 9]


def delete_odd_number(list_):
    # list01=list_[:]
    # for val in list01:
    #     if val % 2 == 1:
    #         list_.remove(val)
    # return list_
    for i in range(len(list_) - 1, -1, -1):
        if list_[i] % 2 == 1:
            del list_[i]
    return list_


print(delete_odd_number(list01))
