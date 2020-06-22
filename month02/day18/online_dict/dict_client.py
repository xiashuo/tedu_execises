from socket import *
import sys


class Client:
    ADDR = ("127.0.0.1", 8888)

    def __init__(self):
        self.sock = socket()
        self.sock.connect(Client.ADDR)
        self.user_name = None

    def login(self):
        while True:
            print("*" * 10 + "用户登录" + "*" * 10)
            print("*" + " " * 9 + "1.登录" + " " * 10 + "*")
            print("*" + " " * 9 + "2.注册" + " " * 10 + "*")
            print("*" + " " * 9 + "3.退出" + " " * 10 + "*")
            print("*" * 26)
            try:
                cmd = input("请输入指令：")
            except KeyboardInterrupt:
                cmd = "3"
            if cmd == "1":
                while True:
                    user_name = input("用户名：")
                    password = input("密码：")
                    self.sock.send(f"login {user_name} {password}".encode())
                    res = self.sock.recv(1024).decode()
                    if res == "ok":
                        print(f"登录成功，欢迎{user_name}")
                        self.user_name = user_name
                        self.login_in()
                        break
                    else:
                        print("用户名或者密码错误，请重新输入！")
            elif cmd == "2":
                user_name = input("用户名：")
                while not user_name or " " in user_name:
                    print("用户名不能为空且不能包含空格！")
                    user_name = input("用户名：")
                while True:
                    password1 = input("密码：")
                    while not password1 or " " in password1:
                        print("密码不能为空且不能包含空格!")
                        password1 = input("密码：")
                    password2 = input("重复密码：")
                    if password1 != password2:
                        print("两次密码不一样，请重新输入！")
                        continue
                    self.sock.send(f"register {user_name} {password1}".encode())
                    data = self.sock.recv(128).decode()
                    if data == "ok":
                        print("注册成功！")
                    else:
                        print("用户已存在，注册失败！")
                    break
            elif cmd == "3":
                self.sock.send(b"quit")
                self.sock.close()
                sys.exit("你已退出。")
            else:
                print("输入指令错误！")

    def login_in(self):
        while True:
            print("*" * 10 + "在线词典" + "*" * 10)
            print(" " * 10 + "1.查单词")
            print(" " * 10 + "2.历史记录")
            print(" " * 10 + "3.注销")
            print("*" * 27)
            try:
                cmd = input("输入指令：")
            except KeyboardInterrupt:
                self.sock.send(b"quit")
                return
            if cmd == "1":
                print("提示：输入空（回车）退出查单词。")
                while True:
                    word_input = input("输入单词：")
                    if not word_input:
                        break
                    self.sock.send(f"query_word {word_input} {self.user_name}".encode())
                    data = self.sock.recv(2048).decode()
                    if data == "false":
                        print("未查到该单词含义！")
                    else:
                        print(data)
            elif cmd == "2":
                self.sock.send(f"history {self.user_name}".encode())
                data = self.sock.recv(2048).decode()
                if data == "false":
                    print("没有历史查询记录!")
                else:
                    print(data)

            elif cmd == "3":
                break

    def main(self):
        self.login()


if __name__ == '__main__':
    client = Client()
    client.main()
