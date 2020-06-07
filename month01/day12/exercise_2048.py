'''
2048游戏，控制台版
'''
import random
import copy


class Game_2048:

    def __init__(self):
        self.map = [[0 for i in range(4)] for i in range(4)]
        self.list_merge = [0] * 4

    def print_map(self):
        for line in self.map:
            print(line)
        print()

    # 矩阵转置
    def transpose_map(self):
        # global map
        # map = [[map[i][j] for i in range(len(map))] for j in range(len(map[0]))]
        for i in range(len(self.map) - 1):
            for j in range(i + 1, len(self.map)):
                self.map[i][j], self.map[j][i] = self.map[j][i], self.map[i][j]

    # 在空格子中随机生成一个数字2
    def generate_random_block(self):
        i, j = random.randint(0, 3), random.randint(0, 3)
        if self.map[i][j] == 0:
            self.map[i][j] = 2
        else:
            self.generate_random_block()

    def play_game(self):
        self.generate_random_block()
        self.generate_random_block()
        self.print_map()
        while True:
            move_direction = input("输入移动方向：")
            map1 = copy.deepcopy(self.map)
            if move_direction == 'a':
                self.move_left()
            elif move_direction == 'd':
                self.move_right()
            elif move_direction == 'w':
                self.move_up()
            elif move_direction == 's':
                self.move_down()
            map2 = copy.deepcopy(self.map)
            if map1 == map2:
                continue
            self.generate_random_block()
            self.print_map()
            if self.block_is_full() and self.is_game_over():
                print("game over!")
                break




    # 将list_merge的零元素移动到末尾
    def zero_to_end(self):
        for i in range(len(self.list_merge) - 1, -1, -1):
            if self.list_merge[i] == 0:
                del self.list_merge[i]
                self.list_merge.append(0)

    # 将list_merge的相同元素合并
    def merge(self):
        self.zero_to_end()
        for i in range(len(self.list_merge) - 1):
            if self.list_merge[i] == self.list_merge[i + 1]:
                self.list_merge[i] += self.list_merge[i + 1]
                del self.list_merge[i + 1]
                self.list_merge.append(0)

    # 向左移动
    def move_left(self):
        for line in self.map:
            self.list_merge = line
            self.merge()

    # 向右移动
    def move_right(self):
        for i in range(len(self.map)):
            self.list_merge = self.map[i][::-1]
            self.merge()
            self.map[i] = self.list_merge[::-1]

    # 向上移动
    def move_up(self):
        self.transpose_map()
        self.move_left()
        self.transpose_map()

    # 向下移动
    def move_down(self):
        self.transpose_map()
        self.move_right()
        self.transpose_map()

    def block_is_full(self):
        for line in self.map:
            for val in line:
                if val == 0:
                    return False
        return True

    def is_game_over(self):
        map_temp = copy.deepcopy(self.map)
        self.move_left()
        self.move_right()
        self.move_up()
        self.move_down()
        if self.map == map_temp:
            return True
        self.map = map_temp
        return False


game = Game_2048()
game.play_game()
# print(game.zero_to_end([4,4,0,0]))
