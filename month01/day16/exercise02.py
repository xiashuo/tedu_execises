"""
    调用get_score方法,一定能够返回成绩,不能报错.
    如果输入错误,重新输入.
"""


def get_score():
    while True:
        try:
            score = float(input("请输入成绩:"))
            return score
        except:
            print("输入有误")


print(get_score())
