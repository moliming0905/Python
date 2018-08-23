#devopps with python
###python库  psutil
<pre>
1.安装
<pre>
pip install psutil
</pre>
2.使用
<pre>
(1)获取cpu信息
<pre>
#encoding=utf-8

import psutil

	
#使用cpu_times方法获取cpu完整信息，需要显示所有逻辑CPU信息
#制定方法变量percpu=True即可，如pstuil.cpu_times(percpu=True)
cpu_times = psutil.cpu_times()	
print(cpu_times)

all_info_of_cpu_times = psutil.cpu_times(percpu=True)
print(all_info_of_cpu_times)

#获取单项数据信息，如用户user的cpu时间比
cpu_times_user = psutil.cpu_times().user
print(cpu_times)

#获取cpu的逻辑个数，默认logical=True 
logical_cpu_count = psutil.cpu_count()
print(logical_cpu_count)


#获取cpu的物理个数
physic_cpu_count = psutil.cpu_count(logical=False)
print(physic_cpu_count)
</pre>
(2)获取内存信息
<pre>
#encoding=utf-8

import psutil

#使用psutil.virtual_memory方法获取内存完整信息
mem = psutil.virtual_memory()
print(mem)

#获取内存总数
mem_size = mem.total
print(mem_size)

#获取空闲内存数
mem_free = mem.free
print(mem_free)

#获取swap分区信息
mem_swap = psutil.swap_memory()
print(mem_swap)
</pre>
(3)获取磁盘信息
<pre>
#encoding=utf-8

import psutil

#使用psutil.disk_partitions方法获取磁盘完整信息
disk_infos = psutil.disk_partitions()
for info in disk_infos:
	print(info)
	
#使用psutil.disk_usage方法获取分区(参数)的使用情况
disk_usages = psutil.disk_usage('/')
#for k,v in enumerate(disk_usages):
#	print(k,v)
print(disk_usages)
#for info in disk_usages:
#	print(info)

#使用psutil.disk_io_counters获取磁盘总的IO个数、读写信息
io_info = psutil.disk_io_counters()
print(io_info)

#"perdisk = True" 参数获取单个分区IO个数、读写信息
io_signal_info = psutil.disk_io_counters(perdisk=True)
print(io_signal_info)

</pre>
(4)获取网络信息
<pre>
#encoding=utf-8

import psutil

#使用psutil.net_io_counters获取网络总的IO信息，默认pernic = False
net_info = psutil.net_io_counters()
print(net_info)

#pernic=True输出每个网络接口的IO信息
net_info_detal = psutil.net_io_counters(pernic=True)
print(net_info)
</pre>
(5)其他系统信息
<pre>
#encoding=utf-8

import psutil
import datetime


#使用psutil.users方法返回当前登录系统的用户信息
login_user_info = psutil.users()
print(login_user_info)

#使用psutil.boot_time方法获取开机时间，以Linux时间戳格式返回
boot_time = psutil.boot_time()
time = datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
print("Boot time: ",time)
</pre>
进程管理
<pre>
#encoding=utf-8

import psutil

#列出所有进程PID

pids = psutil.pids()

print(pids)


#实例化一个Process对象，参数为一进程PID
p = psutil.Process(5926)
#进程名
print(p.name())
#进程bin路径
print(p.exe())
#进程工作目录绝对路径
print(p.cwd())
#进程状态
print(p.status())
#进程创建时间，时间戳格式
print(p.create_time())

#进程uid信息
print(p.uids())
#进程gid信息
print(p.gids())
#进程CPU时间信息，包括user、system两个cpu时间
print(p.cup_times())
#get进程cpu亲和度，如果设置进程cpu亲和度，讲cpu号作为参数即可
print(p.cpu_affinity())
#进程内存利用率
print(p.memory_percent())
#进程内存rss、vms信息
print(p.memory_info())
#进程IO信息，包括读写IO数以及字节数
print(p.io_counters())
#返回打开进程socket的namedutples列表，包括fs、family、laddr等信息
print(p.connections())
#进程开启的线程数
print(p.num_threads())
</pre>
<pre>
#encoding=utf-8

import psutil

from subprocess import PIPE

#通过psutil的Popen方法启动的应用程序，可以跟踪该程序运行的所有相关信息
#p = psutil.Popen([r"/user/bin/python","-c","print('hello')"],stdout=PIPE)
p = psutil.Popen([r"python","-c","print('hello')"],stdout=PIPE)

print(p.name())
print(p.username())
print(p.communicate())
#得到进程运行的CPU时间
print(p.cpu_times())
</pre>
</pre>
</pre>


##IPy库
<pre>
#encoding=utf-8

from IPy import IP

ip = IP('192.168.0.0/16')

#输出192.168.0.0/16网段的IP个数
print ip.len()

#输出192.168.0.0/16网段的所有IP清单

for x in ip:
	print(x)

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

<pre>

综合例子


#encoding=utf-8

from IPy import IP

#接收用户输入，参数为IP地址或网段地址
ip_s = raw_input('Please input an IP or net-range: ')

ips = IP(ip_s)

#为一个网络地址

if len(ips) > 1:
	#输出网络地址
	print('net: %s'%ips.net())
	#输出网络掩码地址
	print('netmask: %s'%ips.netmask())
	#输出网络广播地址
	print('broadcast:%s'%ips.broadcast())
	#输出地址反向解析
	print('reverse address: %s'%ips.reverseNames()[0])
	#输出网络子网数
	print('subnet: %s'%len(ips))
#为单个IP地址	
else:
	#输出ip反向解析
	print('reverse address: %s'%ips.reverseNames()[0])

#输出十六进制地址
print('hexadecimal: %s'%ips.strHex())

#输出二进制地址
print('binary ip: %s'%ips.strBin())


#输出地址类型，如PRIVATE、PUBLIC、LOOPBACK等
print('iptype: %s'%ips.iptype())	
	
	
</pre>
</pre>
##dnspython库
<pre>
dnspython的DNS解析器类 resolver的query方法实现域名的查询功能。

query(self,qname,rdtype=1,rdclass=1,tcp=False,source=None,raise_on_no_answer=True,source_port=0)

qname参数为查询的域名。rdtype参数用来指定RR资源的类型
常用的有以下几种：

A记录，将主机名转换成IP地址

MX记录，邮件交换记录，定义邮件服务器的域名

CNAME记录，指别名记录，实现域名间的映射

NS记录，标记区域的域名服务器及授权子域

PTR记录，反向解析，与A记录相反，将IP转换成主机名

SOA记录，SOA标记，一个起始授权区的定义
<pre>
A记录
实现A记录查询方法源码


#encoding=utf-8

import dns.resolver

#输入域名地址
domain = raw_input('Please input an domain: ')

#指定查询类型为A记录
A = dns.resolver.query(domain,'A')

#通过response.answer方法获取查询回应信息
for i in A.response.answer:
	#遍历回应信息
	for j in i.items:
		print(j)
</pre>
<pre>
MX记录
实现MX记录查询方法源码

#encoding=utf-8

import dns.resolver

domain = raw_input('Please input an domain: ')

#指定查询类型为MX记录
MX = dns.resolver.query(domain,'MX')

#遍历回应结果，输出MX记录的preference及exchanger信息
for i in MX:
	print('MX preference = ',i.preference,'mail exchanger =',i.exchange)

</pre>
<pre>
NS记录
实现NS记录查询方法源码

#encoding=utf-8

import dns.resolver

domain = raw_input('Please input an domain: ')
#指定查询类型为NS记录
ns = dns.resolver.query(domain,'NS')

for i in ns.response.answer:
	for j in i.items:
		print(j.to_text())
</pre>


<pre>
CNAME记录
实现CNAME记录查询方法源码

#encoding=utf-8

import dns.resolver

domain = raw_input('Please input an domain: ')

#指定查询类型为CNAME记录
cname = dns.resolver.query(domain,'CNAME')

#结果将回应cname后的目标域名
for i in cname.response.answer:
	for j in i.items:
		print(j.to_text())
</pre>
<pre>
综合实例

#encoding=utf-8

import dns.resolver
import os
import httplib

#定义域名IP列表变量
iplist = []
#定义业务域名
appdomain="www.google.com.hk"

#域名解析函数，解析成功IP将被追加到iplist
def get_iplist(domain=""):
	try:
		#解析A记录类型
		A = dns.resolver.query(domain,'A')
	except Exception,e:
		print("dns resolver error: "+str(e))
		return
	for i in A.response.answer:
		for j in i.items:
			#追加到iplist
			iplist.append(j.address)
	return True
	
def checkip(ip):
	checkurl = ip + ":80"
	getcontent = ""
	#定义http连接超时时间(5秒)
	httplib.socket.setdefaulttimeout(5)
	#创建http连接对象
	conn = httplib.HTTPConnection(checkurl)
	
	#发起URL请求，添加host主机头
	try:
		conn.request("GET","/",headers={"Host":appdomain})
		r = conn.getresponse()
		#获取URL页面前15个字符，以便做可用性校验
		getcontent = r.read(15)
	finally:
		#监控URL页的内容一般是事先定义好的，比如"HTTP200"等
		
		if getcontent == "<!doctype html>":
			print(ip + " [OK]")
		else:
			#此处可放告警程序，可以是邮件、短信通知
			print(ip + " [Error]")

if __name__ == "__main__":
	#条件： 域名解析正确且至少返回一个IP
	if get_iplist(appdomain) and len(iplist)>0:
		for ip in iplist:
			checkip(ip)
	else:
		print("DNS resolver error.")
	
</pre>

</pre>
##difflib模块
<pre>
<pre>
实例一


#encoding=utf-8

import difflib

#定义字符串1
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

#以行进行分隔，以便进行对比
text1_lines = text1.splitlines()

#定义字符串2
text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()

#创建Differ()对象
#d = difflib.Differ()
d = difflib.HtmlDiff()
#采用compare方法对字符串进行比较
#diff = d.compare(text1_lines,text2_lines)
#print('\n'.join(list(diff)))

print(d.make_file(text1_lines,text2_lines))
</pre>
<pre>
实例二 服务器配置文件差异比较

#encoding=utf-8

import difflib
import sys


try:
	#第一个配置文件路径参数
	#textfile1 = sys.argv[1]
	textfile1 = r"D:\python_code\devopps\config.ini.v1";
	
	
	#第二个配置文件路径参数
	#textfile2 = sys.argv[2]
	textfile2 = r"D:\python_code\devopps\config.ini.v2";
	
	
except Exception,e:
	print("Error: "+str(e))
	print("Usage: confFileDiff.py filename1 filename2")
	sys.exit()
	
#文件读取分隔函数
def readfile(filename):
	try:
		fileHandle = open(filename,'rb')
		#读取后以进行分隔
		text = fileHandle.read().splitlines()
		fileHandle.close()
		return text
	except IOError as error:
		print('Read file Error: '+str(error))
		sys.exit()

if textfile1=="" or textfile2=="":
	print("Usage: confFileDiff.py filename1 filename2")
	sys.exit()

#调用readfile函数，获取分隔后的字符串
text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

#创建HtmlDiff()类对象
d = difflib.HtmlDiff()

#通过make_file方法输出HTML格式的比对结果
print(d.make_file(text1_lines,text2_lines))
</pre>
</pre>
##filecmp模块
<pre>
filecmp提供了三个操作方法，分别是：
<pre>
cmp  单文件对比
  采用filecmp.cmp(f1,f2[,shallow])方法，比较文件名为f1和f2的文件，相同返回True,
不相同返回False，shallow默认为True,意思是只根据os.stat()方法返回的文件基本信息
进行对比，
比如最后访问时间、修改时间、状态改变时间等，会忽略文件内容的对比。当shallow为False时，
则os.stat()与文件内容同时进行校验。
</pre>
<pre>
cmpfiles 多文件对比
  采用filecmp.cmpfiles(dir1,dir2,common[,shallow])方法，对比dir1与dir2目录给定的
文件清单。
  该方法返回文件名的三个列表，分别为匹配、不匹配、错误。
  匹配为包含匹配的文件的列表，不匹配反之，错误列表包括了目录不存在文件、不具备读权限或
其他原因导致的不能比较的文件清单。
</pre>

<pre>
dircmp 目录对比
  通过dircmp(a,b[,ignore[,hide]])类创建一个目录的比较对象，其中a和b是参加比较的目录名。
ignore代表文件名忽略的列表，并默认为['RCS','CVS','tags']
hide代表隐藏的列表，默认为[os.curdir,os.pardir]
dircmp类可以获得目录比较的详细信息，如只有在a目录中包括的文件、a与b都在的子目录、
匹配的文件等，同时支持递归

<pre>
	dircmp提供了三个输出报告的方法：
	report() 比较当前指定目录中的内容
	report_partial_closure() 比较当前指定目录及第一级子目录中的内容
	report_full_closure() 递归比较所有指定目录的内容。
</pre>
<pre>
	为了输出更加详细的比较结果,dircmp类还提供了以下属性：
left 左目录，如类定义中的a
right 右目录，如类定义中的b
left_list  左目录中的文件及目录列表
right_list 右目录中的文件及目录列表
common	两边目录共同存在的文件或目录
left_only 只在左目录中的文件或目录
right_only 只在右目录中的文件或目录
common_dirs 两边目录都存在的子目录
common_files 两边目录都存在的子文件
common_funny 两边目录都存在的子目录(不同目录类型或os.stat()记录的错误)
same_files 匹配相同的文件
diff_files 不匹配的文件
funny_files 两边目录中都存在，但无法比较的文件
subdirs 将common_dirs目录名映射到新的dircmp对象，格式为字典类型
</pre>
<pre>
实例一

#encoding=utf-8

import filecmp

#定义左目录
a = r"D:\python_code"

#定义右目录
b = r"D:\SpiderData"

#目录比较，忽略test.py文件
dirobj = filecmp.dircmp(a,b,['test.py'])

#输出对比结果数据报表，详细说明请参考filecmp类方法及属性信息

dirobj.report()
dirobj.report_partial_closure()
dirobj.report_full_closure()
print("left_list: "+str(dirobj.left_list))
print("right_list: "+str(dirobj.right_list))
print("common: "+str(dirobj.common))
print("left_only: "+str(dirobj.left_only))
print("right_only: "+str(dirobj.right_only))
print("common_dirs: "+str(dirobj.common_dirs))
print("common_files: "+str(dirobj.common_files))
print("common_funny: "+str(dirobj.common_funny))
print("same_file: "+str(dirobj.same_files))
print("diff_files: "+str(dirobj.diff_files))
print("funny_files: "+str(dirobj.funny_files))
</pre>
</pre>
</pre>
##pycurl
<pre>
<pre>
pycurl.Curl()类实现了创建一个libcurl包的Curl句柄对象，无参数
Curl对象的几个方法：

close()方法，对应libcurl包中的curl_easy_cleanup方法，无参数，实现关闭、回收Curl对象。

perform()方法，对应libcurl包中的curl_easy_perform方法，无参数，实现Curl对象请求的提交。

setopt(option,value)方法，对应libcurl包中的curl_easy_setopt方法，
参数option是通过libcurl的常量来指定的，参数value的值会依赖option，
可以是一个字符串、整形、长整型、文件对象、列表或函数等。

getinfo(option)方法，对应libcurl包中的curl_easy_getinfo方法，
参数option是通过libcurl的常量来指定的。
</pre>
<pre>
# -*- coding: utf-8 -*-

import os
import time
import sys
import pycurl


#探测的目标URL
URL="http://www.baidu.com"
#创建一个curl对象
c = pycurl.Curl()
#定义请求的URL常量
c.setopt(pycurl.URL,URL)
#定义请求连续的等待时间
c.setopt(pycurl.CONNECTTIMEOUT,5)
#定义请求超时时间
c.setopt(pycurl.TIMEOUT,5)
#屏蔽下载进度条
c.setopt(pycurl.NOPROGRESS,1)
#完成交互后强制断开连接，不重用
c.setopt(pycurl.FORBID_REUSE,1)
#指定HTTP重定向的最大数为1
c.setopt(pycurl.MAXREDIRS,1)
#设置保存DNS信息的时间为30秒
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)

#创建一个文件对象，以"wb"方式打开，用来存储返回的http头部及页面内容
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
#将返回的HTTP HEADER定向到indexfile文件
c.setopt(pycurl.WRITEHEADER,indexfile)
#将返回的HTML内容定向到indexfile文件对象
c.setopt(pycurl.WRITEDATA,indexfile)
try:
	#提交请求
	c.perform()
except Exception,e:
	print("connection error: "+str(e))
	indexfile.close()
	c.close()
	sys.exit()

#获取DNS解析时间
NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
#获取建立连接时间
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
#获取从建立连接到准备传输所耗的时间
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
#获取从建立连接到传输开始消耗的时间
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
#获取传输的总时间
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
#获取HTTP状态码
HTTP_CODE = c.getinfo(c.HTTP_CODE)
#获取下载数据包大小
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
#获取HTTP头部大小
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
#获取平均下载速度
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

#打印输出相关数据

print("HTTP状态码： %s"%HTTP_CODE)
print("DNS解析时间： %.2f ms"%(NAMELOOKUP_TIME*1000))
print("建立连接时间：%.2f ms"%(CONNECT_TIME*1000))
print("准备传输时间：%.2f ms"%(PRETRANSFER_TIME*1000))
print("传输开始时间：%.2f ms"%(STARTTRANSFER_TIME*1000))
print("传输结束总时间：%.2f ms"%(TOTAL_TIME*1000))
print("下载数据包大小: %d byte"%(SIZE_DOWNLOAD))
print("HTTP头部大小: %d byte"%(HEADER_SIZE))
print("平均下载速度: %d bytes/s"%(SPEED_DOWNLOAD))

#关闭文件及curl对象
indexfile.close()
c.close()
<pre>
结果如下：


HTTP状态码： 200
DNS解析时间： 0.00 ms
建立连接时间：32.00 ms
准备传输时间：32.00 ms
传输开始时间：47.00 ms
传输结束总时间：110.00 ms
下载数据包大小: 117121 byte
HTTP头部大小: 929 byte
平均下载速度: 1064736 bytes/s

请按任意键继续. . .
</pre>
</pre>
</pre>
##xlsxwriter库
<pre>
<pre>
Workbook类

Workbook(filename[,options])
Workbook代表整个电子表格文件，并且存储在磁盘上

参数：
filename(String类型) 为创建的Excel文件存储路径
options(Dict类型)为可选的Workbook参数，一般作为初始化工作表内容格式，
例如值为{'strings_to_numbers':True}表示使用worksheet.write()方法时激活字符串转换数字
<pre>
方法：
1.add_worksheet([sheetname])方法，作用是添加一个新的工作表，参数
参数sheetname(String类型)为可选的工作表名称，默认为Sheet1。
worksheet1 = workbook.add_worksheet()	#Sheet1
worksheet2 = workbook.add_worksheet('Foglio2') #Foglio2
worksheet3 = workbook.add_worksheet('Data')	#Data
worksheet4 = workbook.add_worksheet()	#Sheet4


2.add_format([properties])方法，作用是在工作表中创建一个新的格式对象来格式化单元格。
参数properties(dict类型)为指定一个格式属性字典，例如设置一个
加粗的格式对象，workbook.add_format({'bold':True})
通过Format methods(格式化方法)也可以实现格式的设置，等价的设置加粗格式代码如下
bold = workbook.add_format()
bold.set_bold()

3.add_chart(options)方法，作用是在工作表中创建一个图表对象，内部是通过insert_chart()方法来实现，
参数options(dict类型)为图表指定一个字典属性，例如
设置一个线条类型的图表对象，代码为
chart = workbook.add_chart({'type':'line'})

4.close()方法，作用是关闭工作表文件，如workbook.close()
</pre>
Worksheet类--将数据写入单元格或工作表格式布局等
Worksheet对象不能直接实例化，取而代之的是通过Workbook对象
调用add_worksheet()方法来创建。
<pre>
方法：
1.write(row,col,*args)方法，作用是写普通数据到工作表的单元格，
参数row为行坐标，col为列坐标，坐标索引起始值为0;
*args无名字参数为数据内容，可以为数字、公式、字符串或格式对象。
为了简化不同数据类型的写入过程，write方法已经作为其他更加具体
数据类型方法的别名，包括：
（1）write_string() 写入字符串类型数据，如：
worksheet.write_string(0,0,'Your text here')
 (2)write_number() 写入数字类型数据，如：
worksheet.write_number('A2',2.3451)
 (3)write_blank() 写入空类型数据，如：
worksheet.write('A2',None)
 (4)write_formula() 写入公式类型数据，如：
worksheet.write_formula(2,0,'=SUM(B1:B5)')
 (5)write_datetime() 写入日期类型，如：
worksheet.write_datetime(7,0,datetime.datetime.strptime('2013-01-23','%Y-%m-%d'),workbook.add_format({'num_format':'yyyy-mm-dd'}))
 (6)write_boolean() 写入逻辑类型数据，如：
worksheet.write_boolean(0,0,True)
 (7)write_url() 写入超链接类型数据，如：
worksheet.write_url('A1','ftp://www.python.org/')

2.set_row(row,height,cell_format,options)方法，作用是设置行单元格的属性。
参数：
 row(int类型)指定行位置，起始下标为0
 height(float类型)设置行高，单位像素
 cell_format(format类型)指定格式对象
 options(dict类型)设置行hidden(隐藏)、level(组合分级)、collapsed(折叠)
操作示例如下：
#在A1单元格写入'Hello'字符串
worksheet.write('A1','Hello')
#定义一个加粗的格式对象
cell_format = workbook.add_format({'bold':True})
#设置第1行单元格高度为40像素，且引用加粗格式对象
worksheet.set_row(0,40,cell_format)
#隐藏第2行单元格
worksheet.set_row(1,None,None,{'hidden':True})

3.set_column(first_col,last_col,width,cell_format,options)方法，作用是设置一列或多列单元格属性。
参数：
 first_col(int类型)指定开始列位置，起始下标为0
 last_col(int类型)指定结束列位置，起始下标为0，可以设置成与first_col一样。
 width(float类型)设置列宽
 cell_format(Format类型)指定格式对象
 options(dict类型)设置行hidden(隐藏)、level(组合分级)、collapsed(折叠)。
操作示例如下：
#在A1单元格写入'Hello'字符串
worksheet.write('A1','Hello')

#在B1单元格写入'World'字符串
worksheet.write('B1','World')

#定义一个加粗的格式对象
cell_format = workbook.add_format({'bold':True})

#设置0到1即(A到B)列单元格宽度为10像素，且引用加粗格式对象
worksheet.set_column(0,1,10,cell_format)

#设置C到D列单元格宽度为20像素
worksheet.set_column('C:D',20)

#隐藏E到G列单元格
worksheet.set_column('E:G',None,{'hidden':1})

4.insert_image(row,col,image[,options])方法，作用是插入图片到指定单元格，
支持PNG、JPEG、BMP等图片格式。
参数：
 row 为行坐标
 col 为列坐标，坐标索引起始值为0,
 image(string类型)为图片路径
 options(dict类型)为可选参数，作用是指定图片的位置、比例、链接URL信息。
操作示例如下：
#在B5单元格插入python-logo.png图片，图片超级链接为http://python.org
worksheet.insert_image('B5','img/python-logo.png',{'url':'http://python.org'})
</pre>
Chart类
支持的图表类型包括面积、条形图、柱形图、折线图、饼图、散点图、股票和雷达等
图表对象是通过Workbook(工作簿)的add_chart方法创建，通过{type,'图表类型'}字典参数指定图表的类型
语句如下：
#创建一个column(柱形)图表
chart = workbook.add_chart({type,'column'})
<pre>
更多图表类型说明：
 area:创建一个面积样式的图表	
 bar:创建一个条形样式的图表
 column:创建一个柱形样式的图表
 line:创建一个线条样式的图表
 pie:创建一个饼图样式的图表
 scatter:创建一个散点样式的图表
 stock:创建一个股票样式的图表
 radar：创建一个雷达样式的图表
</pre>
然后再通过Worksheet(工作表)的insert_chart()方法插入到指定位置，语句如下：
#在A7单元格插入图表
worksheet.insert_chart('A7',chart)
<pre>
chart类常用方法：
1.chart.add_series(options)方法，作用为添加一个数据系列到图表，
参数
 options(dict类型)设置图表系列选项的字典，操作示例如下：
chart.add_series({
	'categories':'=Sheet1!$A$1:$A$5',
	'values': '=Sheet1!$B$1:$B$5',
	'line':{'color':'red'},
})

add_series方法最常用的三个选项为categories、value、line
 categories 设置图表类别标签范围
 values 设置图表数据范围
 line 设置图表线条属性，包括颜色、宽度等

其他常用方法及示例
 set_x_axis(options)方法，设置图表X轴选项，示例代码如下：

chart.set_x_axis({
 #设置x轴标题名称
 'name':'Earnings per Quarter',
 #设置x轴标题字体属性
 'name_font':{'size':14,'bold':True},
 #设置x轴数字字体属性
 'num_font':{'italic':True},

})

 set_size(options)方法，设置图表大小，如chart.set_size({
 'width':720,'height':576})
 其中width为宽度，height为高度

 set_title(options)方法，设置图表标题，如chart.set_title({
'name':'Year End Results'})

 set_style(style_id)方法，设置图表样式，style_id为不同数字则代表不同样式，
如chart.set_style(37)

 set_table(options)方法,设置X轴为数据表格形式，如chart.set_table(),
  
</pre>

</pre>

<pre>
简单实例

# -*- coding:utf-8 -*-

import xlsxwriter

#创建一个Excel文件
workbook = xlsxwriter.Workbook('demo1.xlsx')
#创建一个工作表对象
worksheet = workbook.add_worksheet()

#设定第一列(A)宽度为20像素
worksheet.set_column('A:A',20)
#定义一个加粗的格式对象
bold = workbook.add_format({'bold':True})
#A1单元格写入'Hello'
worksheet.write('A1','Hello')
#A2单元格写入'World'并引用加粗格式对象bold
worksheet.write('A2','World',bold)
#B2单元格写入中文并引用加粗格式对象bold
worksheet.write('B2',u'中文测试',bold)
#用行列表示法写入数字'32'与'35.5'
worksheet.write(2,0,32)
#行列表示法的单元格下标以0作为起始值，'3,0'等价于'A3'
worksheet.write(3,0,35.5)
#求A3:A4的和，并将结果写入'4,0',即'A5'
worksheet.write(4,0,'=SUM(A3:A4)')
#在B5单元格插入图片
#worksheet.insert_image('B5','img/python-logo.png')
#关闭Excel文件
workbook.close()
</pre>
<pre>
#coding:utf-8

import xlsxwriter

#创建一个Excel文件
workbook = xlsxwriter.Workbook('chart.xlsx')
#创建一个工作表对象
worksheet = workbook.add_worksheet()
#创建一个图表对象
chart = workbook.add_chart({'type':'column'})
#定义数据表头列表
title = [u'业务名称',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日',u'平均流量']
#定义频道名称
buname = [u'业务官网',u'新闻中心',u'购物频道',u'体育频道',u'亲子频道']
#定义5频道一周7天流量数据列表

data = [
	[150,152,158,149,155,145,148],
	[89,88,95,93,98,100,99],
	[201,200,198,175,170,198,195],
	[75,77,78,78,74,70,79],
	[88,85,87,90,93,88,84],
]

#定义format格式对象
format = workbook.add_format()
#定义format对象单元格边框加粗(1像素)的格式
format.set_border(1)

#定义format_title格式对象
format_title = workbook.add_format()
#定义format_title对象单元格边框加粗(1像素)的格式
format_title.set_border(1)
#定义format_title对象单元格背景颜色为#cccccc格式
format_title.set_bg_color('#cccccc')
#定义format_title对象单元格居中对齐的格式
format_title.set_align('center')
#定义format_title对象单元格内容加粗的格式
format_title.set_bold()
#定义format_ave格式对象
format_ave = workbook.add_format()
#定义format_ave对象单元格边框加粗(1像素)的格式
format_ave.set_border(1)
#定义format_ave对象单元格数字类别显示格式
format_ave.set_num_format('0.00')

#下面分别以行或列写入方式将标题、业务名称、流量数据写入起始单元格，同时引用不同格式对象
worksheet.write_row('A1',title,format_title)
worksheet.write_column('A2',buname,format)
worksheet.write_row('B2',data[0],format)
worksheet.write_row('B3',data[1],format)
worksheet.write_row('B4',data[2],format)
worksheet.write_row('B5',data[3],format)
worksheet.write_row('B6',data[4],format)

#定义图表数据系列函数
def chart_series(cur_row):
	#计算(AVERAGE函数)频道周平均流量
	worksheet.write_formula('I'+cur_row,'=AVERAGE(B'+cur_row+':H'+cur_row+')',format_ave)
	chart.add_series({
		#将"星期一至星期日"作为图表数据标签(x轴)
		'categories':'=Sheet1!$B$1:$H$1',
		#频道一周所有数据作为数据区域
		'values':'=Sheet1!$B$'+cur_row+':$H$'+cur_row,
		#线条颜色定义为black(黑色)
		'line': {'color':'black'},
		#引用业务名称为图例项
		'name':'=Sheet1!$A$'+cur_row,
	
	})

#数据域以第2~6行进行图表数据系列函数调用	
for row in range(2,7):
	chart_series(str(row))

#设置X轴表格格式，本示例不启用
#chart.set_table()
#设置图表样式，本示例不启用
#chart.set_style(30)

#设置图表大小
chart.set_size({'width':577,'height':287})
#设置图表(上方)大标题
chart.set_title({'name':u'业务流量周报图表'})
#设置y轴(左侧)小标题
chart.set_y_axis({'name':'Mb/s'})

#在A8单元格插入图表
worksheet.insert_chart('A8',chart)
#关闭Excel文档
workbook.close()
</pre>
</pre>

##scapy库
<pre>

</pre>