"""
一、数据类型：
1.数字：
int、float、bool
int：整数，正数或负数，不带小数点
a = -5
b = 6
print(a + b)

float：浮点数
a = -5
b = 6.1
print(a + b)

bool：Troe(1)、Fales(0)

运算符示例：
print(5 + 4) 加
print(5 - 4)    减
print(5 * 4)    乘
print(5 / 4)    除
print(5 // 4)   相除，向下取整
print(5 % 4)    取模，返回两数相除的余数
print(5 ** 4)   乘方

比较运算符：
>   大于
>=  大于等于
<   小于
<=  小于等于
!=  不等于
==  等于
var1 = 8
var2 = 3
print(var1 > var2)
返回True或False

布尔值也可以用and、or、not运算：
and 与
所有值都为True，结果才为True
print(True and True)

or 或
只要一个值为True，结果才就True
print(True or False)

not 非
对布尔表达式的结果取反值
print(not True and True)

空值：None
内置函数的返回值：
"""
"""
2.字符串：通过引号表示
a = "hello word" 
b = 'hello word'

字符串索引：从0开始到-1结束
c = "北京欢迎您！"
print(c[0])  取第一个值
print(c[-1])  取最后一个值
print(c[0:3])  或  print(c[:3])  取0-3，取左不取右
print(c[-3:-1])  取倒数第一个到倒数第三个字符，取左不取右
print(c[-3:])    取倒数第一个到倒数第三个字符
print(c[::-1])   反转字符串

切片 [开始:结尾:步长]，
c = "北京欢迎您！"
print(c[0:4])
print(c[0:4:2])
北京欢迎
北欢

print(c[-6:-2])
print(c[-6:-2:3])
北京欢迎
北迎

字符串拼接：
a = "hello" + "python"    b = "太好玩了"   c = ','.join((a,b))
print(a)
print(a + b)
print(c)

字符串格式化：
format:
a = "大家好，我的名字叫{}!,我的年龄是{},".format("Tom","19")

b = "大家好，我的名字叫{}!,我的年龄是{},"
print(b.format("Tom","19"))

b = "大家好，我的名字叫{1}!,我的年龄是{0},"
print(b.format("Tom","19"))

input_name = input("请输入你的名字：")
name = "我的名字叫{}!".format(input_name)
print(name)

s = 3.14559
x = 5.66
print("今天的橘子{1:.2f}一斤!".format(s, x))  取两位小数，四舍五入 :.2f
print("今天的橘子{:.2%}一斤!".format(0.45625))  以百分比显示   :.2%

find:
var = "hellopython"
print(var.find("o"))  返回o第一次出现的位置索引,未找到返回-1
print(var.find("o", 5, -1))   返回5到最后一个字符中o第一次出现的位置索引

count:
var = "hellopython"
print(var.count("o"))   统计o出现的次数

replace:替换指定的片段
参数1：要替换的字符串
参数2：替换后的字符串
参数3：替换次数
var = "HelloPythona"
s1 = var.replace("o", "T",2)

upper:将小写换成大写
s2 = var.upper()
print(s2)

lower：将大写换成小写
s2 = var.lower()
print(s2)

.lower() --- 全部小写
.upper() --- 全部大写
.title() --- 各个字符的首字母大写
.capitalize() --- 首字母大写


split:
指定分割点对字符串进行分割
参数1：分割点
参数2：分割次数
var = "HelloPythona"
print(var.split("o"))
print(var.split("o", 1))

strip:
去除字符串首尾空格
var = "   HelloPythona   "
print(var.strip())
var1 = "333HelloPythona333"
print(var.strip("3"))   去除字符3
var2 = "333 Hello Pythona 333"
print(var2.replace(" ", ""))  去除中间空格

格式化输出方法：
%s :为字符占位，任意类型都可以
s1 = input("请输入你的成绩：")
s2 = "我的成绩是%s"%(s1)
print(s2)

%d ：为数值类型占位
s2 = "我的成绩是%s"%(99)
print(s2)

%f ：为浮点数占位
s2 = "我的成绩是%f"%(99.69)
print(s2)

F表达式：(F、f都可以，python3.6以上支持)
name = "tom"
age = "19"
s1 = "我的名字叫{},我的年龄是{}".format(name, age)
s2 = F"我的名字叫{name},我的年龄是{age}"
print(s2)

len:字符串长度
s1 = "hellopython"
print(len(s1))    统计字符串长度
"""
"""
列表：list
定义列表： list_1 = [1, 2, 3, 6, 5, "成都", 10, [9, 5, 6]]
列表索引：0到-1
列表取值：
print(list_1[2])
print(list_1[-1][1])
查看列表长度：print(len(list_1))

列表的加法：
list_2 = [10, 20, 30]
print(list_1 + list_2)
[1, 2, 3, 6, 5, '成都', 10, [9, 5, 6], 10, 20, 30]
列表的乘法：
print(list_2 * 3)
[10, 20, 30, 10, 20, 30, 10, 20, 30]

列表切片取值
list_1 = [1, 2, 3, 6, 5, 10, 9, 5, 6]
print(list_1[0:3])    取0-3，取左不取右

print(list_1[-4:-1])  取倒数第1位到倒数第4位，取左不取右
print(list_1[-4:])    取倒数第1位到倒数第4位
print(list_1[2:-1:2])  跨2位取值
print(list_1[::-1])    反转列表
"""


# offer_list = ["Allen", "Tom"]
# offer1 = ", you have passed our interview and will soon become a member of our company."
# offer2 = ", welcome to join us!"
#
# print(offer_list[0] + offer1)
# print(offer_list[1] + offer1)
# print(offer_list[0] + offer2)
# offer_list[1] = "Andy"
# print(offer_list[1] + offer2)

#将输入字符串生成列表
# var1 = input()
# print(var1.split())

# 生成数字列表
# str1 = input()
# list_1 = str1.split()
# list_2 = []
# for i in list_1:
#     i = int(i)
#     list_2.append(i)
# print(list_2)























