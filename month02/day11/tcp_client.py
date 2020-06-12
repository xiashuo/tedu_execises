"""
tcp套接字基础流程 客户端
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket()

# 发起连接
tcp_socket.connect(("127.0.0.1",8888))

# 发送接收消息
msg = input(">>")
tcp_socket.send(msg.encode())
data = tcp_socket.recv(1024)
print("从服务器收到:",data.decode())

# 关闭套接字
tcp_socket.close()
