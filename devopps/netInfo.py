#encoding=utf-8

import psutil

#使用psutil.net_io_counters获取网络总的IO信息，默认pernic = False
net_info = psutil.net_io_counters()
print(net_info)

#pernic=True输出每个网络接口的IO信息
net_info_detal = psutil.net_io_counters(pernic=True)
print(net_info)