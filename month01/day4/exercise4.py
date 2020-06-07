'''
赌大小游戏
    玩家的身家初始10000，实现下列效果：
        少侠请下注: 30000
        超出了你的身家，请重新投注。
        少侠请下注: 8000
        你摇出了5点,庄家摇出了3点
        恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
        少侠请下注: 18000
        你摇出了6点,庄家摇出了6点
        打平了，少侠，在来一局？
        少侠请下注: 18000
        你摇出了4点,庄家摇出了6点
        少侠,你输了，身家还剩 0
        哈哈哈，少侠你已经破产，无资格进行游戏
'''

import random

principal = 10000
print(f"当前本金：{principal}")
while True:
    bet_amount = int(input("少侠请下注："))
    if bet_amount > principal:
        print("超出了你的身家，请重新投注。")
        continue
    my_points = random.randint(0, 6)
    banker_points = random.randint(0, 6)
    print(f"你摇出了{my_points}点，庄家摇出了{banker_points}点")
    if my_points > banker_points:
        principal += bet_amount
        print(f"恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩{principal}")
    elif my_points == banker_points:
        print("打平了，少侠，在来一局？")
    else:
        principal -= bet_amount
        print(f"少侠,你输了，身家还剩{principal}")
        if principal == 0:
            print("哈哈哈，少侠你已经破产，无资格进行游戏")
            break
