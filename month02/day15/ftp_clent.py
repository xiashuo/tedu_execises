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

ADDR = ("127.0.0.1", 8088)

def init_view():
    print("*"*10+" ftp文件系统命令表 "+"*"*10)
    dict_command={"list":"显示所有文件","get file":"下载file文件","put file":"上传file文件","quit":"退出系统"}
    for k,v in dict_command.items():
        print("*"+" "*10+f"{k}:{v}"+" "*(21-len(f"{k}:{v}"))+"*")
    print("*"*37)
def main():
    # init_view()
    sock = socket()
    sock.connect(ADDR)
    while True:
        sock.send(b"hello")
        data = sock.recv(1024).decode()
        print(data)


if __name__ == '__main__':
    # main()
    init_view()
    print(len("ftp文件系统命令表 **********"))
