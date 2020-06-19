from socket import *

sockfd = socket()
sockfd.bind(("0.0.0.0", 8889))
sockfd.listen(3)

connfd, addr = sockfd.accept()
data = connfd.recv(1024)
print(data.decode())
response = "HTTP/1.1 200 ok\n"
response += "Content-Type:text/html;charset=utf-8\n"
response += "\n"
with open("python.html") as f:
    data=f.read()
response += data
print(response)
connfd.send(response.encode())
sockfd.close()
