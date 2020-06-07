'''
1. 小明家必须要过一座桥。小明过桥最快要１秒，小明的弟弟最快要３秒，小明的爸爸最快要６秒，小明的妈妈最快要８秒，小明的爷爷最快要１２秒。
每次此桥最多可过两人，而过桥的速度依过桥最慢者而定。过桥时候是黑夜，所以必须有手电筒，小明家只有一个手电筒，而且手电筒的电池只剩30秒就将耗尽。
小明一家该如何过桥，请写出详细过程。
'''
import random
import itertools
import copy

a = {"小明": 1, "弟弟": 3, "爸爸": 6, "妈妈": 8, "爷爷": 12}
b = {}
step = []
step_all = []


def xiao_ming_bridge(a, b, step, step_all):
    # 如果a为空,说明已经全部过桥,则返回
    if not a:
        step_all.append(step)
        return step_all
    # 在a中选2个人的所有组合
    all_group = tuple(itertools.combinations(a, 2))
    # 遍历所有组合,进行a到b,b到a的步骤
    for group in all_group:
        # 这里函数a_to_b_to_a返回更新后的a_,b_,step_,而此层函数的
        # a,b,step保持不变.
        a_, b_, step_ = a_to_b_to_a(a, b, group, step)
        # 重复过桥过程:a到b,b到a  这里递归调用自己
        xiao_ming_bridge(a_, b_, step_, step_all)
    return step_all

# 该函数就是模拟a到b,b到a的过程
def a_to_b_to_a(a_raw, b_raw, group, step_raw):
    # 深克隆一份a,b,step,防止原始值跟着发生修改
    a = copy.deepcopy(a_raw)
    b = copy.deepcopy(b_raw)
    step = copy.deepcopy(step_raw)
    # 这里group参数指的是从a到b的一个2人组合
    # 下面的a,b,step的更新过程和第一种方法里原理一样,就不一一注释了
    people1, people2 = group
    cost_time = max(a[people1], a[people2])
    step.append(group)
    step.append(cost_time)
    b[people1] = a[people1]
    b[people2] = a[people2]
    del a[people1], a[people2]
    if not a:
        return a, b, step
    b_to_a = min(b, key=b.get)
    step.append("-->")
    step.append(b_to_a)
    step.append(b[b_to_a])
    a[b_to_a] = b[b_to_a]
    del b[b_to_a]
    return a, b, step

# 获取所有方案,并打印出来,并找出时间最少的方案
def get_xiaoming_bridge_result():
    global step
    all_steps = xiao_ming_bridge(a, b, step, step_all)
    min_time_step = all_steps[0]
    min_time = 100
    print("所有过桥方案：")
    for step in all_steps:
        print(' '.join([str(val) for val in step]))
        total_time = 0
        for val in step:
            if type(val) == int:
                total_time += val
        if total_time < min_time:
            min_time_step = step
            min_time = total_time
    print(f"最快的过桥步骤为：{' '.join(str(val) for val in min_time_step)},花费时间为：{min_time}s")


def xiaoming_guoqiao():
    a = {"小明": 1, "弟弟": 3, "爸爸": 6, "妈妈": 8, "爷爷": 12}
    b = {}
    step = []
    while True:
        # 从a中随机取两个人过桥
        group = random.sample(list(a), 2)
        # 将过桥的两个人加入到step中
        step.append((group[0], group[1]))
        # 添加此趟花费的时间到step中,桥的速度依过桥最慢者而定
        step.append(max(a[group[0]], a[group[1]]))
        # 删除a中的这两个人,添加到b中
        b[group[0]], b[group[1]] = a[group[0]], a[group[1]]
        del a[group[0]], a[group[1]]
        # 如果a为空了,说明已经全部过桥
        if not a:
            # 计算总花费时间
            cost_time = 0
            for val in step:
                if type(val) == int:
                    cost_time += val
            # 如果总时间小于等于30s,则返回结果
            if cost_time <= 30:
                print(f"满足条件的走法为:{' '.join([str(val) for val in step])},花费时间为:{cost_time}")
                break
            # 总时间大于30s,则清空step,a,b还原,从新开始
            step = []
            a = {"小明": 1, "弟弟": 3, "爸爸": 6, "妈妈": 8, "爷爷": 12}
            b = {}
            continue
        # b中派速度最快的人回到a
        person = min(b, key=b.get)
        step.append("-->")
        step.append(person)
        step.append(b[person])
        a[person] = b[person]
        del b[person]


'''
2. 给你一个 n*m 的二维数组，每行元素保证递增，每列元素保证递增，试问如何找到某个数字，或者判断这个数字不存在。
'''


def find(target, key):
    n, m = len(target), len(target[0])
    i, j = 0, m - 1
    while i < n and j >= 0:
        if target[i][j] < key:
            i += 1
        elif target[i][j] > key:
            j -= 1
        else:
            return True
    return False


# for i in range(10):
#     print(find([[1, 2, 3], [4, 5, 6], [7, 8, 9]], i))

'''
3. 给你一个长度为n的数组，其中只有一个数字出现了1次，其他均出现2次，问如何快速的找到这个数字。
'''


# def find_one_number(target):
#     res = target[0] ^ target[1]
#     for i in range(2, len(target)):
#         res = res ^ target[i]
#     return res


def find_one_number(target):
    dict_number = {}
    for val in target:
        if val not in dict_number:
            dict_number[val] = 1
        else:
            dict_number[val] += 1

    return min(dict_number, key=dict_number.get)


# print(find_one_number([10, 2, 2, 3, 3]))

if __name__ == '__main__':
    # 小明过桥
    get_xiaoming_bridge_result()
    # xiaoming_guoqiao()
