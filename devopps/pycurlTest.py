# -*- coding: utf-8 -*-

import os
import time
import sys
import pycurl


#̽���Ŀ��URL
URL="http://www.baidu.com"
#����һ��curl����
c = pycurl.Curl()
#���������URL����
c.setopt(pycurl.URL,URL)
#�������������ĵȴ�ʱ��
c.setopt(pycurl.CONNECTTIMEOUT,5)
#��������ʱʱ��
c.setopt(pycurl.TIMEOUT,5)
#�������ؽ�����
c.setopt(pycurl.NOPROGRESS,1)
#��ɽ�����ǿ�ƶϿ����ӣ�������
c.setopt(pycurl.FORBID_REUSE,1)
#ָ��HTTP�ض���������Ϊ1
c.setopt(pycurl.MAXREDIRS,1)
#���ñ���DNS��Ϣ��ʱ��Ϊ30��
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)

#����һ���ļ�������"wb"��ʽ�򿪣������洢���ص�httpͷ����ҳ������
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
#�����ص�HTTP HEADER����indexfile�ļ�
c.setopt(pycurl.WRITEHEADER,indexfile)
#�����ص�HTML���ݶ���indexfile�ļ�����
c.setopt(pycurl.WRITEDATA,indexfile)
try:
	#�ύ����
	c.perform()
except Exception,e:
	print("connection error: "+str(e))
	indexfile.close()
	c.close()
	sys.exit()

#��ȡDNS����ʱ��
NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
#��ȡ��������ʱ��
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
#��ȡ�ӽ������ӵ�׼���������ĵ�ʱ��
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
#��ȡ�ӽ������ӵ����俪ʼ���ĵ�ʱ��
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
#��ȡ�������ʱ��
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
#��ȡHTTP״̬��
HTTP_CODE = c.getinfo(c.HTTP_CODE)
#��ȡ�������ݰ���С
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
#��ȡHTTPͷ����С
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
#��ȡƽ�������ٶ�
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

#��ӡ����������

print("HTTP״̬�룺 %s"%HTTP_CODE)
print("DNS����ʱ�䣺 %.2f ms"%(NAMELOOKUP_TIME*1000))
print("��������ʱ�䣺%.2f ms"%(CONNECT_TIME*1000))
print("׼������ʱ�䣺%.2f ms"%(PRETRANSFER_TIME*1000))
print("���俪ʼʱ�䣺%.2f ms"%(STARTTRANSFER_TIME*1000))
print("���������ʱ�䣺%.2f ms"%(TOTAL_TIME*1000))
print("�������ݰ���С: %d byte"%(SIZE_DOWNLOAD))
print("HTTPͷ����С: %d byte"%(HEADER_SIZE))
print("ƽ�������ٶ�: %d bytes/s"%(SPEED_DOWNLOAD))

#�ر��ļ���curl����
indexfile.close()
c.close()



