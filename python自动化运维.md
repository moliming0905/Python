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
</pre>
</pre>