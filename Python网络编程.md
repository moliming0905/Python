#Python 网络编程
###socket模块的四种可能异常
<pre>
1.与一般I/O和通信问题有关的socket.error
2.与查询地址信息有关的 socket.gaierror
3.与其他地址错误有关的socket.herror(和C语言中的h_errno相关)
4.与在一个socket上调用settimeout()后，处理超时有关的socket.timeouit
</pre>
###setsockopt()和getsockopt()的选项
<pre>
1. SO_BINDTODEVICE
意义：可以使socket只在某个特殊的网络接口(网卡)有效，也许不能是移动便携设备
期望值： 一个字符串给出设备的名称，或者一个空字符串返回默认值

2.SO_BROADCAST
意义：允许广播地址发送和接收信息包，只对UDP有效。
期望值： 布尔型整数

3.SO_DONTROUTE
意义：禁止通过路由器和网关往外发送信息包。这主要是为了安全而用在以太网上udp通信的一种方法。
不管目的地址使用什么IP地址，它都可以防止数据离开本地网络。
期望值：布尔型整数

4.SO_KEEPALIVE
意义：可以使TCP通信的信息包保持连续性，这些信息包可以在没有信息传输的时候，
使通信的双方确定连接是保持的。
期望值：布尔型整数

5.SO_OOBINLINE
意义：可以把收到的不正常数据看成是正常的数据；也就是说，
会通过一个标准的对recv()的调用来接收这些数据。
期望值：布尔型数据

6.SO_REUSEADDR
意义：当socket关闭后，本地端用于该socket的端口号立刻就可以被重用。
通常来说，只有经过系统定义的一段时间后，才能被重用。
期望值：布尔型整数

7.SO_TYPE
意义：重新得到socket类型（例如SOCK_STREAM或SOCK_DGRAM）。只用于getsockopt()
期望值:整数
</pre>
获取当前机器安装的Python支持的socket选项
<pre>
#encoding=utf-8

import socket
solist = [x for x in dir(socket) if x.startswith('SO_')]
solist.sort()

for x in solist:
	print(x)
</pre>
<pre>
#结果
SO_ACCEPTCONN
SO_BROADCAST
SO_DEBUG
SO_DONTROUTE
SO_ERROR
SO_EXCLUSIVEADDRUSE
SO_KEEPALIVE
SO_LINGER
SO_OOBINLINE
SO_RCVBUF
SO_RCVLOWAT
SO_RCVTIMEO
SO_REUSEADDR
SO_SNDBUF
SO_SNDLOWAT
SO_SNDTIMEO
SO_TYPE
SO_USELOOPBACK

请按任意键继续. . .

</pre>

