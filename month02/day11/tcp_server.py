"""
tcp 服务端 基础演示
"""

from socket import *

# 创建TCP套接字 （不写参数默认也是tcp）
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听
tcp_socket.listen(3)

# 等待客户端连接 (阻塞函数)
print("Waiting for connect ....")
connfd,addr = tcp_socket.accept()
print("Connect from",addr)

# 收发消息
data = connfd.recv(1024)
print("收到:",data.decode())

connfd.send(b"Thanks")

# 关闭
connfd.close()
tcp_socket.close()


