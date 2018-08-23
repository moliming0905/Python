#encoding=utf-8

from IPy import IP

ip = IP('192.168.0.0/16')

#输出192.168.0.0/16网段的IP个数
print ip.len()

#输出192.168.0.0/16网段的所有IP清单

for x in ip:
	print(x)