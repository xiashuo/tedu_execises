from socket import *
from tools.mysql_tool import MysqlTool

socketfd = socket(AF_INET, SOCK_DGRAM)
socketfd.bind(("192.168.17.131", 8888))
MysqlTool.connect_database("dict")

while True:
    data, addr = socketfd.recvfrom(1000)
    print(f"接收到：{data.decode()}")
    res = MysqlTool.query_by("words", "word", data.decode())
    if not res:
        mean = "没有查到该单词！"
    else:
        mean = "单词含义为：" + res[0][2]
    socketfd.sendto(mean.encode(), addr)
