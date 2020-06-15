import socket
from multiprocessing import Process
import sys

ADDR = ('127.0.0.1', 8088)


def login(sock):
    while True:
        name = input("输入聊天昵称：")
        msg = f"login,{name}"
        sock.sendto(msg.encode(), ADDR)
        recv, addr = sock.recvfrom(200)
        if recv.decode() == "ok":
            print(f"{name},您已进入群聊！")
            return name
        else:
            print("该昵称已存在！请重新输入昵称！")


def recv_msg(sock):
    while True:
        recv, addr = sock.recvfrom(2048)
        print()
        print(recv.decode())
        print("发言：",end="")


def send_msg(sock, name):
    while True:
        print()
        try:
            content = input("发言：")
        except:
            content="quit"

        if content == "quit":
            sock.sendto(f"quit,{name}".encode(),ADDR)
            sys.exit("您已退出群聊")
        msg = f"chat,{name},{content}"
        sock.sendto(msg.encode(), ADDR)
        print()
        print(f"我：{content}")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    name = login(sock)
    p = Process(target=recv_msg, args=(sock,))
    p.daemon = True
    p.start()
    send_msg(sock, name)


if __name__ == '__main__':
    main()
