#!/usr/bin/env python
import urllib
import urllib2

#这是百度搜索链接，一般是这样的"http://www.baidu.com/s?wd=python"等，这句意思是查有关python的词条
url = "http://www.baidu.com/s"

#设置用户代理，反反爬虫
headers = {"User-Agent": "Mozilla"}

#输入查询的关键字
keyword = raw_input("Enter the query string:")

wd = {"wd": keyword}

#通过urllib.urlencode()进行解码，参数是一个字典类型
wd = urllib.urlencode(wd)

#拼接完整的URL
fullurl = url + "?" + wd

#组织报头信息
request = urllib2.Request(fullurl, headers=headers)

#发出请求
response = urllib2.urlopen(request)

#打印获得的词条HTML页面信息
print response.read()
