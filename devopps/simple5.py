#encoding=utf-8

import dns.resolver
import os
import httplib

#定义域名IP列表变量
iplist = []
#定义业务域名
appdomain="www.google.com.hk"

#域名解析函数，解析成功IP将被追加到iplist
def get_iplist(domain=""):
	try:
		#解析A记录类型
		A = dns.resolver.query(domain,'A')
	except Exception,e:
		print("dns resolver error: "+str(e))
		return
	for i in A.response.answer:
		for j in i.items:
			#追加到iplist
			iplist.append(j.address)
	return True
	
def checkip(ip):
	checkurl = ip + ":80"
	getcontent = ""
	#定义http连接超时时间(5秒)
	httplib.socket.setdefaulttimeout(5)
	#创建http连接对象
	conn = httplib.HTTPConnection(checkurl)
	
	#发起URL请求，添加host主机头
	try:
		conn.request("GET","/",headers={"Host":appdomain})
		r = conn.getresponse()
		#获取URL页面前15个字符，以便做可用性校验
		getcontent = r.read(15)
	finally:
		#监控URL页的内容一般是事先定义好的，比如"HTTP200"等
		
		if getcontent == "<!doctype html>":
			print(ip + " [OK]")
		else:
			#此处可放告警程序，可以是邮件、短信通知
			print(ip + " [Error]")

if __name__ == "__main__":
	#条件： 域名解析正确且至少返回一个IP
	if get_iplist(appdomain) and len(iplist)>0:
		for ip in iplist:
			checkip(ip)
	else:
		print("DNS resolver error.")
	
	
	
	