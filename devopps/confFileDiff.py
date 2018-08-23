#encoding=utf-8

import difflib
import sys


try:
	#第一个配置文件路径参数
	#textfile1 = sys.argv[1]
	textfile1 = r"D:\python_code\devopps\config.ini.v1";
	
	
	#第二个配置文件路径参数
	#textfile2 = sys.argv[2]
	textfile2 = r"D:\python_code\devopps\config.ini.v2";
	
	
except Exception,e:
	print("Error: "+str(e))
	print("Usage: confFileDiff.py filename1 filename2")
	sys.exit()
	
#文件读取分隔函数
def readfile(filename):
	try:
		fileHandle = open(filename,'rb')
		#读取后以进行分隔
		text = fileHandle.read().splitlines()
		fileHandle.close()
		return text
	except IOError as error:
		print('Read file Error: '+str(error))
		sys.exit()

if textfile1=="" or textfile2=="":
	print("Usage: confFileDiff.py filename1 filename2")
	sys.exit()

#调用readfile函数，获取分隔后的字符串
text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

#创建HtmlDiff()类对象
d = difflib.HtmlDiff()

#通过make_file方法输出HTML格式的比对结果
print(d.make_file(text1_lines,text2_lines))

	