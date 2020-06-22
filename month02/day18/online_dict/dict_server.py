from socket import *
from multiprocessing import Process
import sys
from tools.mysql_tool import MysqlTool

ADDR = ("0.0.0.0", 8888)


class DictServer(Process):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd
        MysqlTool.connect_database("dict")

    def do_register(self, temp):
        user_name, password = temp[1], temp[2]
        result = MysqlTool.query_by(table="users", where="user_name", value=user_name)
        if not result:
            if MysqlTool.insert(table="users", user_name=user_name, password=password):
                self.connfd.send(b"ok")
                return
        self.connfd.send(b"false")

    def do_login(self, temp):
        user_name, password = temp[1], temp[2]
        pwd_res = MysqlTool.query_by(table="users", where="user_name", value=user_name)
        if not pwd_res or pwd_res[0][2] != password:
            self.connfd.send(b"false")
        else:
            self.connfd.send(b"ok")

    def run(self) -> None:
        while True:
            data = self.connfd.recv(1024).decode()
            temp = data.split()
            if data == "quit":
                MysqlTool.close()
                break
            elif temp[0] == "register":
                self.do_register(temp)
            elif temp[0] == "login":
                self.do_login(temp)
            elif temp[0] == "query_word":
                self.do_query_word(temp)
            elif temp[0] == "history":
                self.do_history(temp)

    def do_query_word(self, temp):
        word, uname = temp[1], temp[2]
        res = MysqlTool.query_by(table="words", where="word", value=word)
        if not res:
            self.connfd.send(b"false")
            return
        mean = res[0][2]
        self.connfd.send(mean.encode())
        if MysqlTool.insert(table="history", word=word, uname=uname):
            print("插入历史记录成功")
        else:
            print("历史记录插入失败")

    def do_history(self, temp):
        uname = temp[1]
        res = MysqlTool.query_by(table="history", where="uname", value=uname)
        if not res:
            self.connfd.send(b"false")
            return
        data = "\n".join(map(lambda x: (" "*5).join(map(str, list(x))), res[:10]))
        self.connfd.send(data.encode())


def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    while True:
        try:
            connfd, addr = sock.accept()
        except KeyboardInterrupt:
            sys.exit("服务端退出！")
        print(f"来自客户端{addr}的连接")
        p = DictServer(connfd)
        p.start()
        p.join()
        print(f"客户端{addr}退出。")


if __name__ == '__main__':
    main()
