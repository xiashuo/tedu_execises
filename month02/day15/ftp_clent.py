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
import os, sys, time

ADDR = ("127.0.0.1", 8088)


def init_view():
    print()
    print("*" * 10 + " ftp文件系统命令表 " + "*" * 10)
    dict_command = {"list": "显示所有file", "get file": "下载file文件", "put file": "上传file文件", "quit": "退出系统"}
    for k, v in dict_command.items():
        print("*" + " " * 10 + f"{k}：{v}" + " " * (22 - len(f"{k}：{v}")) + "*")
    print("*" * 38)


def get_file(sock, file_name):
    msg = sock.recv(128).decode()
    if msg == "false":
        print(f"{file_name}文件不存在！")
        return
    with open(file_name, "wb") as f:
        while True:
            data = sock.recv(2048)
            if data == b"##":
                print(f"{file_name}已下载完成。")
                break
            f.write(data)


def put_file(sock, file_name):
    if not os.path.exists(file_name):
        print(f"{file_name}文件不存在！")
        return
    sock.send(f"put {file_name}".encode())
    msg = sock.recv(128).decode()
    if msg == "false":
        print(f"{file_name}文件已存在！")
        return
    with open(file_name, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                sock.send(b"##")
                break
            sock.send(data)
        msg = sock.recv(128).decode()
        if msg == "ok":
            print(f"{file_name}已上传完成。")
        else:
            print(f"{file_name}上传失败。")


def main():
    sock = socket()
    sock.connect(ADDR)
    while True:
        init_view()
        try:
            command = input("输入命令：")
        except KeyboardInterrupt:
            command = "quit"
        if command == "quit":
            sock.send(command.encode())
            sys.exit("已退出系统")
        elif command == "list":
            sock.send(command.encode())
            data = sock.recv(1024).decode()
            print(data)
        elif command[:3] == "get":
            sock.send(command.encode())
            file_name = command.split()[-1]
            get_file(sock, file_name)
        elif command[:3] == "put":
            file_name = command.split()[-1]
            put_file(sock, file_name)
        else:
            print("请输入正确命令！")
            continue


if __name__ == '__main__':
    main()
