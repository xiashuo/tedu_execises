'''
创建技能类(技能名称,攻击比率,消耗法力,持续时间)
  保证数据范         0 - 2  0 - 80  0 - 120
  不要全部使用快捷键
  零基础同学,还可以尝试员工类限制工资不能小于0
                     部门类限制名称不能大于10个字符
'''


class Skill:
    def __init__(self, skill_name, attack_rate, mana_cost, time):
        self.skill_name = skill_name
        self.attack_rate = attack_rate
        self.mana_cost = mana_cost
        self.time = time

    @property
    def attack_rate(self):
        return self.__attack_rate

    @attack_rate.setter
    def attack_rate(self, value):
        if 0 < value < 2:
            self.__attack_rate = value
        else:
            raise Exception("攻击比率超出范围！")

    @property
    def mana_cost(self):
        return self.__mana_cost

    @mana_cost.setter
    def mana_cost(self, value):
        if 0 < value < 80:
            self.__mana_cost = value
        else:
            raise Exception("消耗法力超出范围！")

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        if 0 < value < 120:
            self.__time = value
        else:
            raise Exception("持续时间超出范围！")


skill01 = Skill("裂波斩", 1, 20, 3)
print(skill01.__dict__)
print(skill01.attack_rate)
print(skill01.mana_cost)
print(skill01.time)
