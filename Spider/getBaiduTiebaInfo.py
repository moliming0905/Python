#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import urllib2

def loadPage(url,filename):
    """
        作用：根据URL发送请求，获取服务器响应文件
        url:需要爬取的url地址
        filename:处理的文件名
    """
    print "Download "+filename
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"
    }
    request = urllib2.Request(url, headers = headers)
    return urllib2.urlopen(request).read()

def writePage(html,filename):
    """
        作用：将html内容写入到本地
        html:服务器相应文件内容
    """
    print "Saveing "+filename
    with open(filename+".html",'w') as f:
        f.write(html)
    print "_"*30
def tiebaSpider(url,beginPage,endPage):
    """
    作用： 贴吧爬虫调度器，负责组合处理每个页面的url
    url：贴吧url的前部分
    beginPage：起始页
    endPage：结束页
    """
    for page in range(beginPage,endPage+1):
        pn = (page - 1 )*50
        filename = str(pn)+"page"
        fullurl = url + "&pn="+str(pn)

        html = loadPage(fullurl,filename)
        #print html
        writePage(html,filename)

if __name__ == "__main__":
    kw = raw_input("Enter the name of tieba :")
    beginPage = int(raw_input("Enter start page number:"))
    endPage = int(raw_input("Enter end page number:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)
