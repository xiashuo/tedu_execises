from socket import *

ADDR = ('0.0.0.0', 8088)
dict_users = {}


def sendto_all_users(sock, msg):
    for user in dict_users:
        sock.sendto(msg.encode(), dict_users[user])


def do_login(sock, name, addr):
    if name in dict_users:
        sock.sendto(b"false", addr)
        return False
    sock.sendto(b"ok", addr)
    msg = f"欢迎{name}进入群聊！"
    sendto_all_users(sock, msg)
    dict_users[name] = addr
    return True


def do_chat(sock, name, content):
    for i in dict_users:
        if i != name:
            sock.sendto(f"{name}：{content}".encode(), dict_users[i])


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)
    while True:
        recv, addr = sock.recvfrom(2048)
        list_recv = recv.decode().split(",", 2)
        request_type, name = list_recv[0], list_recv[1]
        if request_type == "login":
            do_login(sock, name, addr)
        elif request_type == "quit":
            del dict_users[name]
            msg = f"{name}已退出群聊。"
            sendto_all_users(sock, msg)
        elif request_type == "chat":
            content = list_recv[2]
            do_chat(sock, name, content)


if __name__ == '__main__':
    main()
