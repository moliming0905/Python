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


