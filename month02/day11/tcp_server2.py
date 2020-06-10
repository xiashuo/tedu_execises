from socket import *
import time

# 创建套节字，不写参数默认也是tcp
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 绑定地址
tcp_socket.bind(('0.0.0.0', 8888))
# 设置监听
tcp_socket.listen(3)


# 等待客户端连接（阻塞函数）
print("等待连接。。。")
connfd, addr = tcp_socket.accept()
print(f"成功连接到:{addr}")
file_name="%d-%d-%d.jpg"%time.localtime()[:3]
with open(file_name,"wb") as f:
    # 收发消息
    while True:
        data = connfd.recv(1024*1024)
        f.write(data)
        if data=='##':
            connfd.send("图片上传成功".encode())
            break
    connfd.close()
    tcp_socket.close()

