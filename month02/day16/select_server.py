"""
重点代码！！

思路 ：
要关注的IO ：监听套接字　　各个客户端的连接套接字
"""

from socket import *
from select import select

# 　创建好监听套接字
sockfd = socket()
sockfd.bind(("0.0.0.0", 8081))
sockfd.listen(5)

# IO多路复用配合网络时一般为非阻塞网络模型
# sockfd.setblocking(False)

# 设置关注列表
rlist = [sockfd]  # 初始我们只关注监听套接字
wlist = []
xlist = []

# 循环监控我们放入列表中的IO
while True:
    # 对IO进行关注
    rs, ws, xs = select(rlist, wlist, xlist)
    # 对rs分情况讨论 --> sockfd一类：客户端连接  connfd一类：对应的客户端发消息
    print("1", rs)
    for r in rs:
        if r is sockfd:
            print("2", rs)
            connfd, addr = r.accept()
            print("Connect from ", addr)
            # 每连接一个客户端，就将这个客户端连接套接字加入关注
            # connfd.setblocking(False)
            rlist.append(connfd)
            print("3", rs)
        else:
            print("4", rs)
            data = r.recv(1024).decode()
            print("5", rs)
            if not data:
                # 客户端退出处理
                rlist.remove(r)  # 不需要监控这个IO
                r.close()
                continue
            print(data)

    for w in ws:
        pass

    for x in xs:
        pass
