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