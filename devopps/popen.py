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