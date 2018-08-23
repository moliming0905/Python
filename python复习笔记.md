#python复习笔记
<font color=blue>##基础</font>
<pre>
1.下划线(_)在解释器中有特别的含义，表示最后一个表达式的值。

<pre>
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>python
Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on
n32
Type "help", "copyright", "credits" or "license" for more information.
>>> print "hello world"
hello world
>>> _
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_' is not defined
>>> mystring = "hello world"
>>> print mystring
hello world
>>> mystring
'hello world'<font color=red>
>>> _
'hello world'</font>
>>>
</pre>

2.print语句也支持将输出重定向到文件。符号>>用来定向输出
<pre>
>>> import sys
>>> print >> sys.stderr, 'Fatal error: invalid input!'
Fatal error: invalid input!
>>> print >> sys.stderr,'Fatal error: invalid input!'
Fatal error: invalid input!<font color=red>
>>> logfile = open('D:/python_code/mylog.txt','a')
>>> print >> logfile,'Fatal error: invalid input!'
>>> logfile.close()</font>
</pre>
3.enumerate()函数
<pre>
In [4]: foo = 'abc'

In [5]: for i in range(len(foo)):
   ...:     print foo[i],'(%d)'%i
   ...:
a (0)
b (1)
c (2)

In [6]: for i,ch in enumerate(foo):
   ...:     print ch,'(%d)'%i
   ...:
a (0)
b (1)
c (2)

In [7]:
</pre>
4.列表解析
[运算式 参数列表 判断条件]
<pre>
In [7]: squared = [x**2 for x in range(4)]

In [8]: squared
Out[8]: [0, 1, 4, 9]

In [9]: sqdEvens = [x**2 for x in range(8) if not x%2]

In [10]: sqdEvens
Out[10]: [0, 4, 16, 36]

In [11]: sum = [x+y for x in range(3) for y in range(3) if x!=y]

In [12]: sum
Out[12]: [1, 2, 1, 3, 2, 3]

In [13]: sum2 = [x*y for x in range(3) for y in range(3) if x!=y]

In [14]: sum2
Out[14]: [0, 0, 0, 2, 0, 2]

</pre>
5.实用的内建函数
<pre>
dir([obj])  显示对象的属性，如果没有提供参数，则显示全局变量的名字。
help([obj]) 以一种整齐美观的形式，显示对象的文档字符串，如果没有
提供任何参数，则会进入交互式帮助。
int(obj) 将一个对象转换为整型
len(obj) 返回对象的长度
open(fn,mode) 以mode('r'=读,'w'=写,'a'=追加)的方式打开一个文件名
为fn的文件。
range([[start,] stop[,step]])返回一个整型列表。起始值为start,
结束值为stop-1,start默认值为0,step默认值为1
raw_input(str)等待用户输入一个字符串，可以提供一个可选的参数
str用作提示信息。
str(obj) 将一个对象转换为字符串
type(obj) 返回对象的类型(返回值本身是一个type对象)
</pre>
</pre>
##语句和语法
<pre>
1.井号(#)表示之后的字符为python注释
2.换行(\n)是标准的行分隔符(通常一个语句一行)
3.反斜线(\)继续上一行
<pre>
有两种例外情况一个语句不使用反斜线也可以跨行。在使用闭合操作符时，
单一语句可以跨多行。
例如：在含有小括号、中括号、花括号时可以多行书写。
另外就是三引号包括下的字符串也可以跨行书写。
</pre>
4.分号(;)将两个语句连接在一行中
5.冒号(:)将代码块的头和体分开
6.语句(代码块)用缩进块的方式体现
7.不同的缩进深度分隔不同的代码块
8.python文件以模块的形式组织。
</pre>
##变量和内存管理
<pre>
<pre>
1.变量无需事先声明
2.变量无需指定类型
3.程序员不用关心内存管理
4.变量名会被"回收"
5.del语句能够直接释放资源
</pre>
<pre>
变量定义，变量生命可以在代码块的中间，不过仍然必须在变量
被使用前声明变量的名字和类型。
在Python中，无需此类显式变量声明语句，变量在第一次被赋值时自动声明。
和其他大多数语言一样，变量只有被创建和赋值后才能被使用。
</pre>
del语句
<pre>
del语句会删除对象的一个引用，它的语法如下：
del obj1[,obj2[,...objN]]
del会删除当前对象的引用，将引用计数器减1，如果引用计数器为0
则会导致该对象从此无法访问或无法抵达，从此刻起，该对象就成为垃圾回收机制的回收对象。
注意任何追踪或调试程序会给一个对象增加一个额外的引用，这会推迟
该对象被回收的时间。
</pre>
垃圾收集
<pre>
  不再使用的内存会被一种称为垃圾收集的机制释放。虽然解释器跟踪对象
的引用计数，但垃圾收集器负责释放内存。垃圾收集器是一块独立代码，
它用来寻找引用计数为0的对象。它也负责检查那些虽然引用计数大于0
但也应该被销毁的对象。特定情形会导致循环引用。
  一个循环引用发生在当你有至少两个对象互相引用时，也就是说所有
的引用都消失时，这些引用仍然存在，这说明只靠引用计数是不够的。
python的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。
当一个对象的引用计数变为0，解释器会暂停，释放掉这个对象和仅有这个对象可访问(可到达)的其他对象。作为引用计数的补充，垃圾收集器也会
留心被分配的总量很大的(及未通过引用计数销毁的那些)对象。
在这种情况下，解释器会暂停下来，试图清理所有未引用的循环。
</pre>
</pre>
##序列
<pre>
切片
<pre>
In [52]: s = 'abcde'

In [53]: i = -1

In [54]: for i in range(-1,-len(s),-1):
    ...:     print s[:i]
    ...:
abcd
abc
ab
a

In [55]: s = 'abcde'

In [56]: for i in [None] + range(-1,-len(s),-1):
    ...:     print s[:i]
    ...:
abcde
abcd
abc
ab
a

使用None作为索引值，这样一来就可以满足你的需要，比如说，在你
想用一个变量作为索引来从第一个到遍历最后一个元素的时候。

In [57]: for i in [None].extend(range(-1,-len(s),-1)):
    ...:     print s[:i]
    ...:
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-57-e791611ff738> in <module>()
----> 1 for i in [None].extend(range(-1,-len(s),-1)):
      2     print s[:i]
      3

TypeError: 'NoneType' object is not iterable
可变对象的内建函数extend()根本没有返回值，所以这个方法是行不通的。
这个错误发生的原因是[None].extend(...)函数返回None,None既不是
序列类型也不是可迭代对象。
在这种情况下使用上面提到的列表连接操作来实现是唯一不需要添加额外
代码的方法。
</pre>
</pre>
##字符串内建函数
<pre>
1. string.capitalize()  把字符串的第一个字符大写
2. string.center(width)  返回一个原字符串居中，并使用空格填充
至长度width的新字符串
3. string.count(str,beg=0,end=len(string))  返回str在string
里面出现的次数，如果beg或者end指定则返回指定范围内str出现的次数
4. string.decode(encoding='UTF-8' errors='strict')   
以decoding指定的编码格式解码string，如果出错默认报一个ValueError的异常，
除非errors指定的是'ignore'或者'replace'
5. string.encode(encoding='UTF-8',errors='strict') 
以encoding指定的编码格式编码string,如果出错默认报一个ValueError的异常，
除非errors指定的是'ignore'或者'replace'
6. string.endswith(obj,beg=0,end=len(string)) 
检查字符串是否是以obj结束，如果beg或者end指定则检查指定的范围
内是否以obj结束，如果是，返回True,否则返回False.
7. string.expandtabs(tabsize=8) 把字符串string中的tab符号
转换为空格，默认的空格数tabsize是8
8. string.find(str,beg=0,end=len(string)) 检测str是否包含
在string中，如果beg和end指定范围，则检查是否包含在指定范围内，
如果是返回开始的索引值，否则返回-1
9. string.index(str,beg=0,end=len(string)) 跟find()方法一样，
只不过如果str不在string中会报一个异常。
10. string.isalnum()  如果string至少有一个字符并且所有字符
都是字母或数字则返回True,否则返回False
11. string.isalpha()  如果string至少有一个字符并且所有字符
都是字母则返回True,否则返回False
12. string.isdecimal()  如果string只包含十进制数字则返回True
否则返回False
13. string.isdigit() 如果string只包含数字则返回True,否则返回False
14. string.islower() 如果string中包含至少一个区分大小写的字
符，并且所有这些(区分大小写的)字符都是小写，则返回True,否则返回False。
15. string.isnumeric() 如果string中只包含数字字符，则返回True
否则返回False
16. string.isspace()  如果string中只包含空格，则返回True,
否则返回False
17. string.istitle()  如果string是标题化的(见title())则
返回True,否则返回False
18. string.isupper()  如果string中包含至少一个区分大小写的
字符，并且所有这些(区分大小写的)字符都是大写，则返回True,否则返回False
19. string.join(seq) 以string作为分隔符，将seq中所有的元素
(字符串表示)合并为一个新的字符串
20. stirng.ljust(width) 返回一个原字符串左对齐，并使用空格
填充至长度width的新字符串
21. string.lower() 转换string中所有大写字符为小写
22. string.lstrip()  截掉string左边的空格
23. string.partition(str) 有点像find()和split()的结合体
，从str出现的第一个位置起，把字符串string分成一个3元组(string_pre_str,str,string_post_str),
如果string中不包含str则string_pre_str = string
24. string.replace(str1,str2,num=string.count(str1))
把string中的str1替换成str2,如果num指定，则替换不超过num次
25. string.rfind(str,beg=0,end=len(string)) 类似于
find()函数，不过是从右边开始查找。
26. string.rindex(str,beg=0,end=len(string)) 类似于index()
不过是从右边开始。
27. string.rjust(width)  返回一个原字符串右对齐，并使用
空格填充至长度width的新字符串
28. string.rpartition(str) 类似于partition()函数，不过
是从右边开始查找。
29. string.rstrip() 删除string字符串末尾的空格。
30. string.split(str="",num=string.count(str))
以str为分隔符切片string，如果num有指定值，则仅分隔num个子字符串
31. string.splitlines(num=string.count('\n')) 按照行分隔，
返回一个包含各行作为元素的列表，如果num指定则仅切片num行。
32. string.startswith(obj,beg=0,end=len(string))
检查字符串是否是以obj开头，是则返回True,否则返回False
如果beg和end指定值，则在指定范围内检查
33. string.strip([obj]) 在string上执行lstrip()和rstrip()
34. string.swapcase() 翻转string中的大小写
35. string.title() 返回“标题化”的string，就是说所有单词都是
以大写开始，其余字母均为小写(见istitle())
36. string.translate(str,del="") 根据str给出的表(包含256个字符)
转换string的字符，要过滤掉的字符放到del参数中
37. string.upper() 转换string中的小写字母为大写
38. string.zfill(width) 返回长度为width的字符串，原字符串string
右对齐，前面填充0
<pre>

In [79]: string1 = "akdsg;lkajsd"

In [80]: import string

In [81]: string.capitalize(string1)
Out[81]: 'Akdsg;lkajsd'

In [82]: string.capitalize(string1)
Out[82]: 'Akdsg;lkajsd'

In [83]:

In [83]: quest = 'what is your favorite color?'

In [84]: quest.capitalize()
Out[84]: 'What is your favorite color?'

In [85]: quest.center(40)
Out[85]: '      what is your favorite color?      '

In [86]: quest.count('or')
Out[86]: 2

In [87]: quest.endswith('blue')
Out[87]: False

In [88]: quest.endswith('color?')
Out[88]: True

In [89]: quest.find('or',30)
Out[89]: -1

In [90]: quest.find('or',22)
Out[90]: 25

In [91]: quest.index('or',10)
Out[91]: 16

In [92]: ':'.join(quest.split())
Out[92]: 'what:is:your:favorite:color?'

In [93]: quest.replace('favorite color','quest')
Out[93]: 'what is your quest?'

In [94]: quest.upper()
Out[94]: 'WHAT IS YOUR FAVORITE COLOR?'

In [95]:
</pre>
</pre>
##集合的所有方法
<pre>
方法，所有的集合方法
<pre>
1. s.issubset(t) 如果s是t的子集，则返回True，否则返回False
2. s.issuperset(t) 如果t是s的超集，则返回True,否则返回False
3. s.union(t) 返回一个新集合，该集合是s和t的并集
4. s.intersection(t) 返回一个新集合，该集合是s和t的交集
5. s.difference(t) 返回一个新集合，该集合是s的成员，但不是t的成员
6. s.symmetric_difference(t) 返回一个新集合，该集合是s或t的成员，但不是s和t共有的成员
7. s.copy() 返回一个新集合，它是集合s的浅复制
</pre>
方法，仅适用于可变集合
<pre>
1. s.update(t) 用t中的元素修改s,即，s现在包含s或t的成员
2. s.intersection_update(t) s中的成员是共同属于s和t的元素
3. s.difference_update(t) s中的成员是属于s但不包含在t中的元素
4. s.symmetric_differece_update(t) s中的成员更新为那些包含在s或t中，但不是s和t共有的元素
5. s.add(obj) 在集合s中添加对象obj
6. s.remove(obj) 从集合s中删除对象obj;如果obj不是集合s中的元素(obj not in s) 将引发KeyError错误
7. s.discard(obj) 如果obj是集合s中的元素，从集合s中删除对象obj
8. s.pop() 删除集合s中的任意一个对象，并返回它
9. s.clear()  删除集合s中的所有元素
</pre>
</pre>