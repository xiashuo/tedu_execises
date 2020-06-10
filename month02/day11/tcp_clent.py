from socket import *


while True:
    data = input("我：")
    if not data:
        break
    sockfd = socket()
    sockfd.connect(('127.0.0.1', 8088))
    sockfd.send(data.encode())
    res = sockfd.recv(1024)
    print("小美：" + res.decode())
    sockfd.close()
