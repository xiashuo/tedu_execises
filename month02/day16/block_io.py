"""
非阻塞IO演示
套接字对象--> 非阻塞
"""

from socket import *
import time


# 创建tcp套接字
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

# 设置非阻塞
# sockfd.setblocking(False)

# 设置超时时间
sockfd.settimeout(3)

while True:
    try:
        print("Waiting for connect")
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
    except BlockingIOError as e:
        # 现在没有客户端连接 做与连接无关事情
        time.sleep(2)
        with open("test.log",'a') as f:
            msg = "%s : %s\n"%(time.ctime(),e)
            f.write(msg)
    except timeout as e:
        with open("test.log",'a') as f:
            msg = "%s : %s\n"%(time.ctime(),e)
            f.write(msg)
    else:
        # 客户端连接上
        data = connfd.recv(1024)








