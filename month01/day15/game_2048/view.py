from controller import GameController


class Game2048View:
    def __init__(self):
        self.__controller = GameController()

    def __display_menu(self):
        print("2048游戏：")
        print("1) 开始游戏")
        print("2) 退出")
        print("游戏说明：w,s,a,d分别代表上下左右")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__start_game()
        elif item == "2":
            exit()
        else:
            self.__select_menu()

    def __start_game(self):
        print("游戏开始。。。")
        self.__controller.init_game()
        self.__controller.print_map()
        while True:
            move_direction=input("请输入移动方向：")
            if move_direction=='w':
                if not self.__controller.move_up():
                    continue
            elif move_direction=='s':
                if not self.__controller.move_down():
                    continue
            elif move_direction=='a':
                if not self.__controller.move_left():
                    continue
            elif move_direction=='d':
                if not self.__controller.move_right():
                    continue
            else:
                continue
            self.__controller.generate_random_block()
            self.__controller.print_map()
            if self.__controller.is_game_over():
                print("游戏结束！")
                break



    def main(self):
        self.__display_menu()
        self.__select_menu()
