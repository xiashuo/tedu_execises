'''
文件服务器

需求：

【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
【2】 客户端可以查看服务器文件库中有什么文件。
【3】 客户端可以从文件库中下载文件到本地。
【4】 客户端可以上传一个本地文件到文件库。
【5】 使用print在客户端打印命令输入提示，引导操作
'''
from socket import *
from threading import Thread
import os, time

ADDR = ("0.0.0.0", 8088)
FILE_PATH = "D:/programing/PythonProjects/tedu_execises/mysql_data/"


class Ftp_Server(Thread):
    def __init__(self, connfd, addr):
        self.connfd = connfd
        self.addr = addr
        super().__init__()

    def list_files(self):
        list_files = os.listdir(FILE_PATH)
        data = "\n".join(list_files)
        self.connfd.send(data.encode())

    def get_file(self, file_name):
        if not os.path.exists(FILE_PATH + file_name):
            self.connfd.send(b"false")
        else:
            self.connfd.send(b"ok")
            with open(FILE_PATH + file_name, "rb") as f:
                while True:
                    data = f.read(1024 * 1024)
                    if not data:
                        self.connfd.send(b"##")
                        break
                    self.connfd.send(data)
                    time.sleep(0.1)

    def put_file(self, file_name):
        with open(FILE_PATH+file_name, "wb") as f:
            while True:
                data = self.connfd.recv(2048)
                if data == b"##":
                    self.connfd.send(b"ok")
                    break
                f.write(data)

    def run(self) -> None:
        while True:
            try:
                data = self.connfd.recv(1024).decode()
            except ConnectionResetError:
                data = "quit"
            if data == "quit":
                self.connfd.close()
                print(f"客户端{self.addr}已退出。")
                return
            elif data == "list":
                self.list_files()
            elif data[:3] == "get":
                file_name = data.split()[-1]
                self.get_file(file_name)
            elif data[:3] == "put":
                file_name = data.split()[-1]
                self.put_file(file_name)


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(5)
    while True:
        connfd, addr = sock.accept()
        print("Connect from", addr)
        ftp_server = Ftp_Server(connfd, addr)
        ftp_server.start()


if __name__ == '__main__':
    main()
