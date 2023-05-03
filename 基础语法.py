"""
python关键字:35个
import keyword
print(keyword.kwlist)

['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
"""
缩进：4个空格或tab
if 2>1:
    print("a")
"""
"""
转义符：\
\n 换行:   
print("我是\n你是？")
\t 制表符(补齐4个占位):    
print("hello\toooo")
\r 覆盖:   
print("hello\roooo")    oooo覆盖hello
\b 删除:  
print("hella\bo")   删除\b前一个字符
\\ 表示一个\:    
print("hella\\o")
使转义符不起作用:  
print(r"hello\no")    print(R"hello\no")
"""
"""
注释：# “”“ ''' ctrl+/(可以一次注释选中的目标)
#这是一个注释

\"""
这是一个注释
这是一个注释
\"""

\'''
这是一个注释
这是一个注释
\'''
"""
"""
输出：print
print("hello world")
var = input("输入一个数：")
print(var, "<class 'int'>", sep="\n")   换行输出

输入：input
name = input("请输入你的名字:")
print("你好:" + name)
"""
"""
变量：
命名规则：name _name name_1 name_a
1.变量名只能是字母、数字和下划线组合
2.变量名第一个字符不能是数字
3.变量名区分大小写
4.关键字不能作为变量名
变量赋值：_name = 1
多个变量赋值：a, b, c = 1, 2, 3
"""
"""
常量：以大写字母命名  BI = 3.1415926
"""






