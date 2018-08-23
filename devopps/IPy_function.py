#encoding=utf-8

from IPy import IP
ip = IP('192.168.1.20')
#反向解析地址格式
print(ip.reverseNames())

#192.168.1.20为私网类型 'PRIVATE'
print(ip.iptype())

#8.8.8.8为公网类型
print(IP('8.8.8.8').iptype())

#转换为整型格式
print(IP('8.8.8.8').int())

#转换为十六进制格式
print(IP('8.8.8.8').strHex())

#转换为二进制格式
print(IP('8.8.8.8').strBin())

#十六进制转换为IP格式
print(IP(0x80808080))

print(IP('192.168.1.0').make_net('255.255.255.0'))
print(IP('192.168.1.0/255.255.255.0',make_net=True))
print(IP('192.168.1.0-192.168.1.255',make_net=True))

#wantprefixlen=0 无返回
print(IP('192.168.1.0/24').strNormal(0))

#prefix格式，如192.168.1.0/24
print(IP('192.168.1.0/24').strNormal(1))

#decimalnetmask格式，如192.168.1.0/255.255.255.0
print(IP('192.168.1.0/24').strNormal(2))

#lastIP格式，如192.168.1.0-192.168.1.255
print(IP('192.168.1.0/24').strNormal(3))

print(IP('10.0.0.0/24')<IP('12.0.0.0/24'))

print('192.168.1.100' in IP('192.168.1.0/24'))

print(IP('192.168.1.0/24') in IP('192.168.0.0/16'))

#判断两个网段是否存在重叠
print(IP('192.168.0.0/23').overlaps('192.168.1.0/24'))
#返回1代表存在重叠

print(IP('192.168.1.0/24').overlaps('192.168.2.0'))
#返回0代表不存在重叠




