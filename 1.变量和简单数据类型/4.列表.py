#列表
#列表非常适合用于存储在程序运行期间可能变化的数据集。
# 列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。
#列表由一系列按特定顺序排列的元素组成。
#可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；
#也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。
#鉴于列表通常包含多个元素，给列表指定一个表示复数的名称，如：letters、digits或names  
#在Python中，用方括号[]来表示列表，并用逗号来分隔其中的元素。
# names = ["zhangsan", "lisi", "wangwu", "zhaoliu"]
# print(names)

#1.访问列表元素
#列表的元素从0开始，要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内
# print(names[0])

#1.1访问列表最后一个元素可直接使用-1
# print(names[-1])

#1.2取出列表中的值存入变量
# message = "hello" + " " + names[1]
# print(message)

#2.修改、添加和删除元素
#2.1修改列表元素
# names[0] = "xusong"
# names[2] = "zhoujielun"
# print(names)

#2.1在列表末尾添加元素
#使用方法append()，可以将元素添加到列表末尾
# names.append("lironghao")
# print(names)

#2.2在列表中插入元素 
#使用方法insert()，可在列表的任何位置添加新元素。需要指定新元素的索引和值。
# names.insert(0,"python")
# print(names)

#2.3从列表中删除元素
#2.3.1使用使del语句删除元素
# del names[0]
# print(names)

#2.3.2使用方法pop()删除元素
#删除列表末尾的元素
# names_1 = names.pop()   #print(names.pop())
# print(names_1)

#删除任何位置处的元素
# print(names.pop(0))

#2.3.3根据值删除元素
#使用方法remove(),方法remove()只删除第一个匹配的值,
# 如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
# names.remove("lisi")
# print(names)

#3.组织列表
#3.1使用方法 使 sort() 对列表进行永久性排序(默认按字母排序)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

#按字母顺序相反的顺序排列,传递参数sort(reverse=True)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

#sort()的修改是永久性的

#3.2使用函数 使 sorted() 对列表进行临时排序(默认按字母排序)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(sorted(cars))

#3.3反转列表元素
#使用方法reverse()
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.reverse()
# print(cars)

#3.3确定列表的长度 
#使用函数len()
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))

#4.操作列表
#4.1使用for循环来打印名单中的所有名字
# names = ["zhoujielun", "linjunjie", "lironghao", "xusong"]
# for names_1 in names:
#     print(names_1)

#循环是让计算机自动完成重复工作的常见方式之一。

#4.2在for循环中执行更多的操作
# names = ["zhoujielun", "linjunjie", "lironghao", "xusong"]
# for names_1 in names:
#     print(names_1)
#     print("hello" + " " + names_1.title())

#4.3在for 循环结束后执行一些操作
# names = ["zhoujielun", "linjunjie", "lironghao", "xusong"]
# for names_1 in names:
#     print(names_1)
#     print("hello" + " " + names_1.title())
# print("over")

#5.创建数值列表
#5.1使用函数range()
#函数range()能够生成一系列的数字
# for value in range(1,6):
#     print(value)

#函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，输出不包含第二个值。

#5.2创建数字列表
#可使用函数list()将range()的结果直接转换为列表
# nums = list(range(1,6))
# print(nums)

#使用函数range() 时，还可指定步长
#函数range()从1开始数，然后不断地加2，直到达到或超过终值
# nums = list(range(1,9,2))
# print(nums)

#创建一个列表，其中包含前10个整数（即1~10）的平方
# lists = []
# for nums in range(1,11):
#     lists.append(nums ** 2)
# print(lists)

#5.3对数字列表执行简单的统计计算
#5.3.1列表的最大值：
# lists = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(max(lists))

#5.3.2列表的最小值：
# lists = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(min(lists))

#5.3.3列表的总和：
# lists = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(sum(lists))

#6.列表解析
#要使用这种语法，首先指定一个描述性的列表名，如squares；然后指定一个左方括号，
#并定义一个表达式，用于生成要存储到列表中的值。表达式 为value**2 ，它计算平方值。
#接下来，编写一个for 循环，用于给表达式提供值，再加上右方括号。
#for 循环为for value in range(1,11) ，它将值 1~10提供给表达式value**2 。
#注意，这里的for语句末尾没有冒号。

# squares = [value ** 2 for value in range(1,11)]
# print(squares)

#7.使用列表的一部分
#7.1切片
#要创建切片，可指定要使用的第一个元素和最后一个元素的索引
lists = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(lists[0:3])print(lists[0:3])
#
# #提取列表的第2~4个元素
# print(lists[1:4])
#
# #如果没有指定第一个索引，将自动从列表开头开始：
# print(lists[:4])
# #没有指定第二个索引，将自动从列表结尾结束：
# print(lists[3:])

#输出最后三个元素：
# print(lists[-3:])

#7.2遍历切片
#遍历列表的部分元素，可在for循环中使用切片
for list_1 in lists[:3]:
    print(list_1)


#练习
#使用一个for 循环打印数字1~20（含）
# for num in range(1,21):
#     print(num)

#创建一个列表，其中包含数字1~1000
# lists = [num for num in range(1,1001)]
# print(lists)

#计算1~1000000的总和：创建一个列表，其中包含数字1~1000000，
#使用min() 和max() 核实该列表确实是从1开始，到1000000结束的。
#另外，对这个列表调用函数sum()，计算1~1000000的总和。
# nums = [num for num in range(1,1000001)]
# print(min(nums))
# print(max(nums))
# print(sum(nums))

#通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；
#再使用一个for 循环将这些数字都打印出来
# nums = [num for num in range(1,21,2)]
# for nums_1 in nums:
#     print(nums_1)

#创建一个列表，其中包含3~30内能被3整除的数字；
#再使用一个for 循环将这个列表中的数字都打印出来
# nums = [num  for num in range(3,31,3)]
# for nums_1 in nums:
#     print(nums_1)

#创建一个列表，其中包含前10个整数（即1~10）的立方，
# 再使用一个for 循 环将这些立方数都打印出来。
# nums = [num ** 3  for num in range(1,10)]
# for nums_1 in nums:
#     print(nums_1)






