# 1.用户输入：
# 1.1函数input()的工作原理：
# 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中。
# name = input("请输入你的名字：")
# print("你好！" + " " + name)

# 1.2获取数值输入：
# age = int(input("输入年龄："))
# if age < 18:
#     print("小于" + str(age))

# 1.3 求模运算符 
# 处理数值信息时，求模运算符（%）它可以将两个数相除并返回余数
# print( 4 % 3)
# print( 5 % 2)

# 2. while循环简介:
# for循环用于针对集合中的每个元素都一个代码块，而while循环不断地运行，直到指定的条件不满足为止

# 2.1 使用while循环：
# num = 1
# while num <= 5:
#     print(num)
#     num += 1        # num += 1 等于：num = num + 1

# 2.2 选择何时退出循环：
# message = ""
# while message != "quit":
#     message = input("输入任意内容开始运行，输入quit退出：")
#     if message != "quit":
#         print(message)

# 2.3 使用标志：
# 定义一个变量，用于判断整个程序是否处于活动状态，这个变量被称为标志。
# a = True
# while a:
#     message = input("输入任意内容开始运行，输入quit退出：")
#     if message == "quit":
#         a = False
#     else:
#         print(message)

# 2.4 使用break退出循环：
# while True:
#     message = input("输入任意内容开始运行，输入quit退出：")
#     if message == "quit":
#         break
#     else:
#         print(message)

# 2.5 在循环中使用continue:
# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         continue    # 如果num除2返回的余数等于0的话就返回到程序开头，否则就打印num
#     print(num)

# 2.6 避免无限循环：
# x = 1 
# while x <= 5: 
#     print(x) 
# 这里x的值没有发生变化，条件测试 x <= 5的结果始终为True，所以会一直运行下去
# 编写时至少有一个能让循环条件为False或让break语句得以执行

# 3. 用while循环处理列表和字典：
# 3.1 在列表之间移动元素：
# 将users列表中的元素移动到new_users列表中
# users = ['alice', 'brian', 'candace']
# new_users = []
# while users:
#     c_users = users.pop()
#     new_users.append(c_users)
# for b in new_users:
#     print(b)
# print(users)

# 3.2 删除包含特定值的所有列表元素:
# 删除cat元素
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while "cat" in pets:
#     pets.remove("cat")
# print(pets)

# 3.3 用户输入填入字典：
# ressages = {}
# while True:
#     name = input("请输入你的名字:")
#     ressage = input("请输入你的答案:")
#     ressages[name] = ressage
#     a = input("输入任意键继续，输入no退出：")
#     if  a == "no":
#         break
#     continue
# print(ressages)



