#encoding=utf-8

import difflib

#定义字符串1
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

#以行进行分隔，以便进行对比
text1_lines = text1.splitlines()

#定义字符串2
text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()

#创建Differ()对象
#d = difflib.Differ()
d = difflib.HtmlDiff()
#采用compare方法对字符串进行比较
#diff = d.compare(text1_lines,text2_lines)
#print('\n'.join(list(diff)))

print(d.make_file(text1_lines,text2_lines))