#encoding=utf-8

import socket

print("Createing socket...")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("done.")

print("Connecting to remote host....")
s.connect(("www.baidu.com",80))
print("done.")



