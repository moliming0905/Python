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



