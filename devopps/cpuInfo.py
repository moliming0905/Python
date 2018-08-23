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
