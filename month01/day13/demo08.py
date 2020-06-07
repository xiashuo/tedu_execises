'''
手雷爆炸,伤害了玩家(碎屏)和敌人(掉装备)
要求:当增加其他事物,不影响手雷的代码.
可能:鸭子(上天)....
体会:开闭原则
依赖倒置
继承价值
'''


class Grenades:
    def blast(self, attack_object):
        attack_object.damage()


class AttackObject:
    def damage(self):
        pass


class Player(AttackObject):
    def damage(self):
        print("碎屏幕")


class Enemy(AttackObject):
    def damage(self):
        print("掉装备")


grenades1 = Grenades()
grenades1.blast(Player())
grenades1.blast(Enemy())
