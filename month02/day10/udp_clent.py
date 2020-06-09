from socket import *

socketfd = socket(AF_INET, SOCK_DGRAM)

while True:
    word=input(">>")
    socketfd.sendto(word.encode(), ('192.168.17.131', 8888))
    if word== "end":
        break
    res,addr=socketfd.recvfrom(1000)
    print(res.decode())

socketfd.close()


