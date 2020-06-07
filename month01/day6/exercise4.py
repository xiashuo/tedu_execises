'''
彩票模拟器 双色球：
        红球：6个,1-33之间（包含）,不能重复
        蓝色：1个,1--16之间（包含）
    -- (1) 创建随机彩票(一个列表,前六个是红球,最后一个是蓝球)    考点:如何产生多个不重复的随机数
    -- (2) 在终端中"购买"彩票(提示：号码已经存在,号码超过范围)
    -- (3) ..玩..
'''
import random

j = 1
while j > 0:
    print(f"第{j}次投注：")
    j += 1
    # 随机生成开奖号码
    list_ball = []
    while len(list_ball) < 6:
        red_ball = random.randint(1, 33)
        if red_ball not in list_ball:
            list_ball.append(red_ball)
    blue_ball = random.randint(1, 16)
    list_ball.append(blue_ball)
    # print(f"本期开奖号码为：{list_ball}")
    # 机器自动随机生成下注
    list_bet_number = []
    while len(list_bet_number) < 6:
        red_ball = random.randint(1, 33)
        if red_ball not in list_bet_number:
            list_bet_number.append(red_ball)
    blue_ball = random.randint(1, 16)
    list_bet_number.append(blue_ball)
    # i = 1
    # while i < 7:
    #     bet_red_number = int(input(f"投注第{i}个红球号码："))
    #     if bet_red_number < 1 or bet_red_number > 33:
    #         print("号码超过范围,重新下注")
    #         continue
    #     if bet_red_number in list_bet_number:
    #         print("号码已经存在，重新下注")
    #         continue
    #     else:
    #         list_bet_number.append(bet_red_number)
    #         i += 1
    # print("")
    # while True:
    #     bet_blue_number = int(input("投注第篮球号码："))
    #     if bet_blue_number < 1 or bet_blue_number > 16:
    #         print("号码超过范围,重新下注")
    #         continue
    #     list_bet_number.append(bet_blue_number)
    #     break

    print(f"本期开奖号码为：{list_ball}")
    print(f"你的下注号码为：{list_bet_number}")

    winning_numbers_red = len([val for val in list_bet_number[:-1] if val in list_ball[:-1]])
    blue_is_true = True if list_bet_number[-1] == list_ball[-1] else False
    if winning_numbers_red == 6 and blue_is_true == True:
        print("恭喜你中了一等奖！喜提500万")
        break
    elif winning_numbers_red == 6 and blue_is_true == False:
        print("恭喜你中了二等奖！喜提150万")
        # break
    elif winning_numbers_red == 5 and blue_is_true == True:
        print("恭喜你中了三等奖！喜提3000元")
        # break
    elif (winning_numbers_red == 5 and blue_is_true == False) or (winning_numbers_red == 4 and blue_is_true == True):
        print("恭喜你中了四等奖！喜提200元")
        # break
    elif (winning_numbers_red == 4 and blue_is_true == False) or (winning_numbers_red == 3 and blue_is_true == True):
        print("恭喜你中了五等奖！喜提10元")
        # break
    elif (winning_numbers_red == 2 and blue_is_true == True) or (winning_numbers_red == 1 and blue_is_true == True) \
            or (winning_numbers_red == 0 and blue_is_true == True):
        print("恭喜你中了六等奖！喜提5元")
        # break
    else:
        print("很遗憾，你没有中奖！")
