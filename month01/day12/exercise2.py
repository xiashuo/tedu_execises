'''
使用面向对象思想,描述下列情景.
    -- (1)小明使用手机打电话
    -- (2)小明一次请多个保洁打扫卫生
          效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
          区别:保洁与保洁列表
    -- (3)玩家攻击(攻击力)多个敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
          区别:敌人与敌人列表
    -- (4)
        张无忌教赵敏九阳神功
        赵敏教张无忌玉女心经
        张无忌工作挣了5000元
        赵敏工作挣了10000元
'''


# (1)小明使用手机打电话
class Person:
    def __init__(self, name):
        self.name = name

    def call(self, communication_tool):
        print(f"{self.name}使用{communication_tool.name}打电话")

    def teach_skill(self, person, skill):
        print(f"{self.name}教{person.name}{skill.name}")

    def work(self, money):
        print(f"{self.name}工作挣了{money.value}")


class Communication_tool:
    def __init__(self, name):
        self.name = name


xiaoming = Person("小明")
mobile_phone = Communication_tool("手机")
xiaoming.call(mobile_phone)


# (2)小明一次请多个保洁打扫卫生
#    效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
#    区别:保洁与保洁列表

class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self, household_service):
        print(self.name, "通知")
        for cleaner in household_service:
            cleaner.cleaning()


class Cleaner:
    def __init__(self, name):
        self.name = name

    def cleaning(self):
        print(f"{self.name}打扫卫生")


xm = Client("小明")
cleaners = [
    Cleaner("保洁1"),
    Cleaner("保洁2"),
    Cleaner("保洁3"),
]
xm.notify(cleaners)


# (3)玩家攻击(攻击力)多个敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
#           区别:敌人与敌人列表

class Player:
    def __init__(self, atk=50):
        self.atk = atk

    def attack(self, targets):
        print("玩家攻击")
        for target in targets:
            target.damage(self.atk)


class Enemy:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def damage(self, value):
        print(f"(⊙o⊙)… {self.name}受伤啦")
        self.hp -= value
        if self.hp <= 0:
            print("播放死亡动画")


p01 = Player()
es = [
    Enemy("敌人1"),
    Enemy("敌人2"),
    Enemy("敌人3"),
]
p01.attack(es)
p01.attack(es)


# (4)
#    张无忌教赵敏九阳神功
#    赵敏教张无忌玉女心经
#    张无忌工作挣了5000元
#    赵敏工作挣了10000元

class Skill:
    def __init__(self, name):
        self.name = name


zhang = Person("张无忌")
zhao = Person("赵敏")
skill01 = Skill("九阳神功")
skill02 = Skill("玉女心经")
zhang.teach_skill(zhao, skill01)
zhao.teach_skill(zhang, skill02)


class Money:
    def __init__(self, value):
        self.value = value


money01 = Money(5000)
money02 = Money(10000)
zhang.work(money01)
zhao.work(money02)
