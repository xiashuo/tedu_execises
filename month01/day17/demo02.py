"""
    迭代器 --> yield
    中午练习:参照demo02,修改exercise01,02
    练习:exercise03,04
"""


class SkillManager:  # 可迭代对象
    def __init__(self):
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def __iter__(self):
        # 生成代码的大致逻辑:
        # 1. 将yield以前的代码放到__next__方法体中
        # 2. 将yield后面的数据作为__next__方法返回值

        # # ...
        # yield "乾坤大挪移"
        # # ...
        # yield "九阳神功"
        # # ...
        # yield "降龙十八掌"
        for skill in self.skills:
            yield skill


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
