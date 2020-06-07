import copy
import random


class GameController:
    def __init__(self):
        self.__map = [[0 for i in range(4)] for i in range(4)]
        self.__list_merge = []

    def print_map(self):
        print()
        for line in self.__map:
            for val in line:
                print(f"{val:5d}", end="")
            print()
        print()

    # 矩阵转置
    def transpose_map(self):
        # map = [[map[i][j] for i in range(len(map))] for j in range(len(map[0]))]
        for i in range(len(self.__map) - 1):
            for j in range(i + 1, len(self.__map)):
                self.__map[i][j], self.__map[j][i] = self.__map[j][i], self.__map[i][j]

    # 在空格子中随机生成一个数字2
    def generate_random_block(self):
        i, j = random.randint(0, 3), random.randint(0, 3)
        if self.__map[i][j] == 0:
            self.__map[i][j] = 2
        else:
            self.generate_random_block()

    # 将list_merge的零元素移动到末尾
    def zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    # 将list_merge的相同元素合并
    def merge(self):
        self.zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    # 向左移动
    def move_left(self):
        map_temp = copy.deepcopy(self.__map)
        for line in self.__map:
            self.__list_merge = line
            self.merge()
        if map_temp == self.__map:
            return False
        return True

    # 向右移动
    def move_right(self):
        map_temp = copy.deepcopy(self.__map)
        for i in range(len(self.__map)):
            self.__list_merge = self.__map[i][::-1]
            self.merge()
            self.__map[i] = self.__list_merge[::-1]
        if map_temp == self.__map:
            return False
        return True

    # 向上移动
    def move_up(self):
        map_temp = copy.deepcopy(self.__map)
        self.transpose_map()
        self.move_left()
        self.transpose_map()
        if map_temp == self.__map:
            return False
        return True

    # 向下移动
    def move_down(self):
        map_temp = copy.deepcopy(self.__map)
        self.transpose_map()
        self.move_right()
        self.transpose_map()
        if map_temp == self.__map:
            return False
        return True

    # 初始化游戏
    def init_game(self):
        self.generate_random_block()
        self.generate_random_block()

    # 判断所有格子是否都有数字了
    def block_is_full(self):
        for line in self.__map:
            for val in line:
                if val == 0:
                    return False
        return True

    # 判断是否游戏结束
    def is_game_over(self):
        if not self.block_is_full():
            return False
        map_temp = copy.deepcopy(self.__map)
        if not self.move_left() and not self.move_right() and not self.move_up() and not self.move_down():
            return True
        self.__map = map_temp
        return False
