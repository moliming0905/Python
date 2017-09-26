#！/usr/bin/env python
import urllib2  #引入URL操作库

#设置用户代理信息(注意是字典类型的)，反反爬虫
ua_headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"
    }

#编辑HTTP报头请求信息
request = urllib2.Request("http://www.baidu.com/",headers=ua_headers)

#用上面的数据报向服务器发出请求信息，保存回应信息
response = urllib2.urlopen(request)

#读取响应信息
html = response.read()

#打印状态码
print response.getcode()

#打印请求的url地址
print response.geturl()

#打印响应状态信息
print response.info()
