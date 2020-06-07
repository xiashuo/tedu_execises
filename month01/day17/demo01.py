"""
    迭代器
    练习:exercise01,02
"""


# 需求:迭代自定义对象

class SkillIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        # (3) 因为迭代过程需要通过__next__方法获取"乾坤大挪移"
        #     所以SkillManager在创建SkillIterator对象时,还需要提供数据("乾坤大挪移")
        try:
            self.index += 1
            return self.data[self.index]
        except IndexError:
            # (4) 因为迭代过程需要__next__抛出停止迭代异常
            #     所以检测IndexError,抛出停止迭代异常
            raise StopIteration()


class SkillManager:# 可迭代对象
    def __init__(self):
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    # (1)因为迭代过程首先是调用__iter__,所以在自定义类中添加__iter__方法.
    def __iter__(self):
        # (2)因为迭代过程需要通过__iter__返回值调用__next__方法
        # 所以__iter__方法要返回能够具有__next__方法的对象
        return SkillIterator(self.skills)


manager = SkillManager()
manager.add_skill("乾坤大挪移")
manager.add_skill("九阳神功")
manager.add_skill("降龙十八掌")

for item in manager:
    print(item)

# 1. 获取迭代器
iterator = manager.__iter__()
while True:
    # 2. 获取下一个元素
    try:
        item = iterator.__next__()
        print(item)
    # 3. 如果抛出停止迭代异常,则跳出循环
    except StopIteration:
        break
