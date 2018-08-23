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