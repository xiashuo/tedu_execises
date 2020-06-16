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

ADDR = ("0.0.0.0", 8088)


class Ftp_Server(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    def run(self) -> None:
        while True:
            data = self.connfd.recv(1024).decode()
            print(data)
            self.connfd.send(b"ok")


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(5)
    while True:
        connfd, addr = sock.accept()
        print("Connect from", addr)
        ftp_server = Ftp_Server(connfd)
        ftp_server.start()

if __name__ == '__main__':
    main()