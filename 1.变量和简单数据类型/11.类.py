



# class Dog():
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title() + " " + "is now sitting")
#
#     def roll_over(self):
#         print(self.name.title() + " " +  "rolld over")
#
# my_dog = Dog('tt',5)
# my_dog.sit()
# my_dog.roll_over()
# print(my_dog.name)
# print(my_dog.age)








# 9-1 创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name 和cuisine_type 。
# 创建一个名 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，
# 而后者打印一条消息，指出餐馆正在营业。 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，
# 再调用前述两个方法。 

# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(self.restaurant_name.title() + " " + self.cuisine_type.title())
#
#     def open_restaurant(self):
#         print(self.restaurant_name.title() + " " + self.cuisine_type.title() + " " "正在营业!")

# restaurant = Restaurant("wwww", "ttt")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# 9-2 三家餐馆 三 ：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。

# a = Restaurant("aaaa", "a1")
# a.describe_restaurant()
# b = Restaurant("bbbb", "b1")
# b.describe_restaurant()
# c = Restaurant("cccc", "c1")
# c.describe_restaurant()

# 9-3 用户用 ：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。
# 在类User 中定义一个名 为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，
# 它向用户发出个性化的问候。 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法

# class User():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def describe_user(self):
#         print(self.first_name.title() + self.last_name.title())
#
#     def greet_user(self):
#         print("你好！" + self.first_name.title() + self.last_name.title())

# a = User("李", "海")
# b = User("张", "涛")
# c = User("罗", "c")
# a.describe_user()
# a.greet_user()
# b.describe_user()
# b.greet_user()
# c.describe_user()
# c.greet_user()

# 9-4 就餐人数：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant的实例；
# 打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。 添加一个名为set_number_served() 的方法，
# 它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就 餐人数。

# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name.title() + " " + self.cuisine_type.title())
#
#     def set_number_served(self, num):
#         if num >= self.number_served:
#             self.number_served = num
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_number_served(self,new_num):
#         self.number_served += new_num
#
#     def open_restaurant(self):
#         print(self.restaurant_name.title() + " " + self.cuisine_type.title() + " " "正在营业!")
#
# restaurant = Restaurant("wwww", "ttt")
# restaurant.set_number_served(20)
# restaurant.increment_number_served(10)
# print(restaurant.number_served)

# 9-5 尝试登录次数：在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts() 的方法， 它将属性login_attempts 的值加1。
# 再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。
# 根据User类创建一个实例，再调用方法increment_login_attempts()多次。
# 打印属性login_attempts的值，确认它被正确地递增；然后，调用方法reset_login_attempts() ，
# 并再次打印属性login_attempts的值，确认它被重置为0。

# class User():
#     def __init__(self, first_name, last_name, login_attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = login_attempts
#
#     def increment_login_attempts(self,num):
#         self.login_attempts += num
#
#     def reset_login_attempts(self,new_num):
#         self.login_attempts = new_num
#
#     def describe_user(self):
#         print(self.first_name.title() + self.last_name.title())
#
#     def greet_user(self):
#         print("你好！" + self.first_name.title() + self.last_name.title())
#
# a = User("li", "sk", 0)
# a.increment_login_attempts(1)
# print(a.login_attempts)
# a.increment_login_attempts(1)
# print(a.login_attempts)
# a.increment_login_attempts(1)
# print(a.login_attempts)
# a.increment_login_attempts(1)
# print(a.login_attempts)
# a.reset_login_attempts(0)
# print(a.login_attempts)


