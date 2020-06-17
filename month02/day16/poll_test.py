
from select import *
from socket import *
from time import sleep


tcp_sock = socket()
tcp_sock.bind(('0.0.0.0',8888))
tcp_sock.listen()

udp_sock = socket(AF_INET,SOCK_DGRAM)
udp_sock.bind(("0.0.0.0",9999))

f = open("test.log")

p = poll() # poll对象
p.register(tcp_sock,POLLIN) # 关注ＩＯ
p.register(f,POLLIN)

print(tcp_sock.fileno(),POLLIN)

sleep(5)

events = p.poll() #　监控ＩＯ
print(events) # [(3,1),...]

