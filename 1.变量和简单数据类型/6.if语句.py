#5.if语句
#if语句能够检查程序的当前状态，并据此采取相应的措施.

#5.1简单示例
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.lower())

#5.2条件测试
#每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试。
#Python根据条件测试的值为True还是False来决定是否执行if语句中的代码。
#如果条件测试的值为True，Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码。

#5.2.1检查是否相等
# car = "bmw"
# print(car == "bmw")
# print(car == "Bmw")

#5.2.2检查是否相等时忽略大小写
# car = "BMw"
# print(car.lower() == "bmw")

#5.2.3检查是否不相等
# car = "BMw"
# print(car != "bmw")

#5.2.4比较数字
# age = 20
# print(age == 20)
# print(age <= 20)
# print(age >= 20)
# print(age != 20)
# print(age > 20)
# print(age < 20)

#5.2.5检查多个条件
#使用and
# age = 20
# age_1 = 40
# print(age > 22 and age_1 > 22)    #False    print((age > 22) and (age_1 > 22))
# print(age > 18 and age_1 > 22)    #True

#使用or
# age = 20
# age_1 = 40
# print(age > 22 or age_1 > 22)     #满足其中一个条件就会返回True,两个条件都不满足才会返回False

#5.2.6检查特定值是否包含在列表中
#使用in
# lists =  ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in lists)

#5.2.7检查特定值是否不包含在列表中
#使用not in
# lists =  ['mushrooms', 'onions', 'pineapple']
# print('mushr' not in lists)

#5.2.8布尔表达式
#与条件表达式一样，布尔表达式的结果要么为True，要么为False.

#5.3if语句
#5.3.1简单的if语句
# age = 20
# if age >= 19:
#     print("you are old enough to vote!")

#5.3.2if-else语句
# age = 20
# if age >= 22:
#     print("you are old enough to vote!")
# else:
#     print("Sorry, you are too young to vote.")

#5.3.3 if-elif-else
#4岁以下免费；4~18岁收费5美元；18岁（含）以上收费10美元。
# age = input("请输入你的年龄：")
# if int(age) < 4:
#     print("你可以免费！")
# elif int(age) < 18:
#     print("收费5美元！")
# else:
#     print("收费10美元！")

#优化
# age = input("请输入你的年龄：")
# if int(age) < 4:
#     price = 0
# elif int(age) < 18:
#     price = 5
# else:
#     price = 10
# print("你的费用是：" + str(price) + "美元！")

#5.3.4使用多个elif代码块
# age = input("请输入你的年龄：")
# if int(age) < 4:
#     price = 0
# elif int(age) < 18:
#     price = 5
# elif int(age) < 65:
#     price = 10
# else:
#     price = 5
# print("你的费用是：" + str(price) + "美元！")

#5.3.6测试多个条件
# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("有mushrooms")
# if 'extra cheese' in requested_toppings:
#     print("有extra cheese")

#练习
#5-3假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green' 、'yellow' 或'red' 。
# 编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
# 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
# alien_color = 'green'
# if alien_color == "green":
#     print("恭喜你获得5个点！")


# alien_color_2 = 'yellow'
# if alien_color_2 == "green":
#     print(" ")


# 5-4 外星人颜色 ：像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
# 编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执行else 代码块。
# alien_color = 'green'
# if alien_color == "green":
#     print("获得5个点")
# else:
#     print("获得10个点")


# alien_color = 'red'
# if alien_color == "green":
#     print("获得5个点")
# else:
#     print("获得10个点")


# 5-5 外星人颜色  ：将练习5-4中的if-else 结构改为if-elif-else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
# 如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
# 编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
# alien_color = 'green'
# if alien_color == "green":
#     print("获得5个点")
# elif alien_color == "yellow":
#     print("获得10个点")
# else:
#     print("获得15个点")

# alien_color = 'yellow'
# if alien_color == "green":
#     print("获得5个点")
# elif alien_color == "yellow":
#     print("获得10个点")
# else:
#     print("获得15个点")

# alien_color = 'red'
# if alien_color == "green":
#     print("获得5个点")
# elif alien_color == "yellow":
#     print("获得10个点")
# else:
#     print("获得15个点")



# 5-6 人生的不同阶段 ：设置变量age 的值，再编写一个if-elif-else 结构，根据age 的值判断处于人生的哪个阶段。
# 如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
# 如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。
# 如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。
# 如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
# 如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
# 如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。
# age = int(input("请输入你的年龄："))
# if age < 2:
#     print("你是一个婴儿")
# elif age < 4:
#     print("你正蹒跚学步")
# elif age < 13:
#     print("你是一个儿童")
# elif age < 20:
#     print("你是青少年")
# elif age < 65:
#     print("你是成年人")
# else:
#     print("你是老年人")





#5.4使用使if语句处理列表
#5.4.1 检查特殊元素
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     print(requested_topping)

#5.4.2 确定列表不是空的
# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(requested_topping)    
# else:
#     print("列表是空的")

#5.4.3 使用多个列表
# names = ["zhangsan", "lisi", "wangwu", "zhaoliu"]
# names_b = ["zhangsan", "wangwu", "xusong"]
# for names_c in names_b:
#     if names_c in names:
#         print(names_c)
#     else:
#         print("没有"+" "+names_c)


# 创建一个至少包含5个用户名的列表，且其中一个用户名为'admin' 。
# 想象你要编写代码，在每位用户登录网站后都打印一条问 候消息。遍历用户名列表，并向每位用户打印一条问候消息。 
# 如果用户名为'admin' ，就打印一条特殊的问候消息，如“Hello admin, would you liketo seeastatus report?”。 
# 否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。

# names = ["root", "gtdq", "sa", "admin", "zhangsan"]
# for names_b in names:
#     if names_b == "admin":
#         print(names_b + " " + "Hello admin, would you liketo seeastatus report?")
#     else:
#         print(names_b + " " + "Hello Eric, thank you for logging in again")


#添加一条if 语句，检查用户名列表是否为空。 
# 如果为空，就打印消息“We need to find some users!”。 删除列表中的所有用户名，确定将打印正确的消息

# names = []
# if names:
#     for names_b in names:
#         if names_b == "admin":
#             print(names_b + " " + "Hello admin, would you liketo seeastatus report?")
#         else:
#             print(names_b + " " + "Hello Eric, thank you for logging in again")
# print("We need to find some users!")

#创建一个至少包含5个用户名的列表，并将其命名为current_users 。
#  再创建一个包含5个用户名的列表，将其命名为new_users ，并确保其中有一两个用户名也包含在列表current_users 中。
#  遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使用。
# 如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指 出这个用户名未被使用。
#  确保比较时不区分大小写；换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN'
current_users = ["root", "gtdq", "sa", "admin", "zhangsan", "John"]
new_users = ["zhangsan", "JOHN", "lisi", "wangwu", "xusong"]
#先将current_users列表内容转换为小写
for i in range(len(current_users)):
    current_users[i] = current_users[i].lower()

#遍历new_users列表
for new_users_1 in new_users:
    if new_users_1.lower() in current_users:  #将new_users列表取出的值转换为小写再与current_users列表对比
        print(new_users_1 + " " + "这个名字已经使用")
    else:
        print(new_users_1 + " " + "这个名字可以使用")

