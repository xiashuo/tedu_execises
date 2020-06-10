from socket import *
sockfd = socket()
sockfd.connect(('127.0.0.1', 8888))
filename=input(">>")
with open(filename,"rb") as f:
    while True:
        data = f.read(1024*1024)
        if not data:
            sockfd.send("##".encode())
            break
        sockfd.send(data)

sockfd.close()

