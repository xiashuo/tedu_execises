'''
使用面向对象思想,描述下列情景.
    玩家攻击敌人(掉装备)
    敌人攻击玩家(碎屏)
    考虑:玩家和敌人还可能被其他目标攻击,也可能攻击其他目标.
    要求:增加新攻击目标,攻击方代码不变.
'''


class Person:
    def __init__(self, name):
        self.name = name

    def attack(self, attack_target):
        print(f"{self.name}打{attack_target.name}")
        attack_target.damage()

    def damage(self, attacker):
        pass


class Player(Person):
    def __init__(self, name):
        super().__init__(name)

    def damage(self):
        print("碎屏")


class Enemy(Person):
    def __init__(self, name):
        super().__init__(name)

    def damage(self):
        print("掉装备")


player1 = Player("玩家1")
enemy1 = Enemy("敌人1")
player1.attack(enemy1)
enemy1.attack(player1)
