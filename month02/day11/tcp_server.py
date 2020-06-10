from socket import *

language_library = {
    "你多大啦？": "我2岁啦",
    "你男生还是女生啊？": "人家女生呀",
    "呵呵": "聊天止于呵呵",
    "你爸上梁山": "你妈逼的"
}

# 创建套节字，不写参数默认也是tcp
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 绑定地址
tcp_socket.bind(('0.0.0.0', 8088))
# 设置监听
tcp_socket.listen(3)
# 等待客户端连接（阻塞函数）
print("等待连接。。。")
while True:
    connfd, addr = tcp_socket.accept()
    print(f"成功连接到:{addr}")
    # 收发消息
    data = connfd.recv(1024)
    if not data:
        break
    print(f"收到{data.decode()}")
    connfd.send(language_library.get(data.decode(), "这道题我不会").encode())
    connfd.close()
