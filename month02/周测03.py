'''
1.给你一个长度为n的数组，其中只有一个数字出现大于n/2次，
问如何快速找到这个数字
'''


def more_than_half_num(numbers):
    res = numbers[0]
    n = len(numbers)
    count = 1
    for i in range(1, n):
        if numbers[i] == res:
            count += 1
        else:
            count -= 1
        if count == 0:
            count = 1
            res = numbers[i]
    count = numbers.count(res)
    if count * 2 > n:
        return res
    else:
        return 0


'''
2. 假设有100层的阶梯，给你两个完全一样的鸡蛋，请设计一种方法，
能够试出从第几层阶梯开始往下仍鸡蛋鸡蛋会碎
'''


def super_egg_drop(k, n):
    '''
    :param k: 鸡蛋个数
    :param n: 楼梯层数
    :return: 乐观估计 最少需要多少次能求出鸡蛋摔碎的层数
    '''
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    for i in range(1, k + 1):
        for step in range(1, n + 1):
            dp[i][step] = dp[i - 1][step - 1] + dp[i][step - 1] + 1
            if dp[k][step] >= n:
                return step


# 解为14，也就是从14楼开始扔鸡蛋，如果碎了，说明高了，则从第一层刚开始
# 逐层递增，直到第二个蛋碎为止，最多14次；如果第一个蛋没碎，则按照13,12,11，
# 。。2,1的规律逐渐增加楼层，直到第一个蛋碎，然后再从上一次扔鸡蛋的
# 楼层开始逐层递增，直到第二蛋蛋碎，即为最低破碎楼层。

'''
3.输入一个正数n，输出所有和为n 连续正数序列。
例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，
所以输出3 个连续序列1-5、4-6 和7-8。
'''


def all_sum_n(n):
    res = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            s = (i + j) * (j - i + 1) / 2
            if s == n:
                res.append(list(range(i, j + 1)))
                break
            elif s > n:
                break

    return res


'''
如果字符串一的所有字符按其在字符串中的顺序出现在另外一个字符串二中，
则字符串一称之为字符串二的子串。注意，并不要求子串（字符串一）的
字符必须连续出现在字符串二中。
请编写一个函数，输入两个字符串，求它们的最长公共子串，
并打印出最长公共子串。
例如：输入两个字符串BDCABA 和ABCBDAB，字符串BCBA 和BDAB 都是
是它们的最长公共子串，则输出它们的长度4，并打印任意一个子串。
'''


def get_max_len_substr(str1, str2, i, j):
    if i < 0 or j < 0:
        return 0, ""

    if str1[i] == str2[j]:
        lenth, sub_str = get_max_len_substr(str1, str2, i - 1, j - 1)
        return lenth + 1, sub_str + str1[i]
    lenth1, sub_str1 = get_max_len_substr(str1, str2, i - 1, j)
    lenth2, sub_str2 = get_max_len_substr(str1, str2, i, j - 1)
    if lenth1 > lenth2:
        return lenth1, sub_str1
    else:
        return lenth2, sub_str2


def max_len_substr(str1, str2):
    i, j = len(str1) - 1, len(str2) - 1
    max_lenth, sub_str = get_max_len_substr(str1, str2, i, j)
    print(f"最大子串长度：{max_lenth},满足条件的子串：{sub_str}")


if __name__ == '__main__':
    # print(more_than_half_num([1,1,2,2,3,2,2]))
    # print(egg_broken())
    # print(all_sum_n(15))
    # print(super_egg_drop(2,100))
    max_len_substr("BDCABAABDCAABBC", "ABCBDAB")

