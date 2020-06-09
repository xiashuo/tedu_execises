'''
套接字基础函数示例
'''
import socket

udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind(('localhost',8088))
udp_socket.bind(('127.168.0.1',8088))
udp_socket.bind(('192.168.17.131',8088))
udp_socket.bind(('0.0.0.0',8088))

