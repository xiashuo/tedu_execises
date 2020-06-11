'''
1. 输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。
例如，输入”They are students.”和”aeiou”，
则删除之后的第一个字符串变成”Thy r stdnts.”
'''


def delete_one_from_one(str_target, str_sub):
    list_target = list(str_target)
    for val in str_sub:
        for i in range(len(list_target) - 1, -1, -1):
            if val == list_target[i]:
                del list_target[i]
    return ''.join(list_target)


# res=delete_one_from_one("They are students.","aeiou")
# print(res)

'''
2. 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，
写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，
有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，
这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”
。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''


def reverse_word(str_target):
    list_target = str_target.split()
    i, j = 0, len(list_target) - 1
    while i < j:
        list_target[i], list_target[j] = list_target[j], list_target[i]
        i += 1
        j -= 1
    return ' '.join(list_target)


# print(reverse_word("student. a am I"))

'''
3. LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,
2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,
想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票
,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,
“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以
看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以
变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,
然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，
否则就输出false。为了方便起见,你可以认为大小王是0。
'''


def is_continuous(numbers):
    num_zoro = numbers.count(0)
    numbers.sort()
    numbers = numbers[num_zoro:]
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            return False
        num_zoro -= (numbers[i + 1] - numbers[i] - 1)
        if num_zoro < 0:
            return False
    return True


# print(is_continuous([1,0,0,5,0]))

'''
4. 4. 某产品的用户注册邀请码为一串有小写字母和数字组成的字符串，
字符串长度为16，当用户数据邀请码的时候，系统需要对邀请码做有效性验证，
假设验证规则如下

1、从序列号最后一位字符开始，逆向将奇数位（1、3、5等等）相加；

2、从序列号最后一位数字开始，逆向将偶数位数字，先乘以2
（如果乘积为两位数，则将其减去9），再求和；

3、将奇数位总和加上偶数位和，结果可以被10整除；

4、小写字母对应数值，可由下面键值对确定；

[(a,1),(b,2),(c,3).....(i,9),(j,1),(k2).....],按照字母排序，
1-9循环

输入：输入16位字符串，表示邀请码

输出：输出‘ok’或者‘error’
'''


def trans_letter_to_digit(code):
    list_code = list(code)
    for i in range(len(list_code)):
        if list_code[i].isalpha():
            list_code[i] = (ord(list_code[i]) - ord("a")) % 9 + 1
        elif list_code[i].isdigit():
            list_code[i] = int(list_code[i])
    return list_code


def verification_code(code):
    sum_odd_order, sum_even_order = 0, 0
    list_code = trans_letter_to_digit(code)
    for i in range(len(list_code) - 1, -1, -2):
        sum_odd_order += list_code[i]
    for j in range(len(list_code) - 2, -1, -2):
        temp = list_code[j] * 2
        sum_even_order += temp - 9 if temp > 9 else temp

    if (sum_odd_order + sum_even_order) % 10 == 0:
        return True
    return False


# print(verification_code("afdsg26451223112"))
import random


def random_number():
    numbers = []
    for i in range(5):
        number = random.randint(0, 13)
        numbers.append(number)
    return numbers


if __name__ == '__main__':
    count=0
    while True:
        count+=1
        numbers = random_number()
        if is_continuous(numbers):
            print(numbers,count)
            break
