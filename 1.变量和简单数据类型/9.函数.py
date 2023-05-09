# 1. 函数：
# 函数是带名字的代码块，用于完成具体的工作。 要执行函数定义的特定任务，可调用该函数。
# 需要在程序中多次执行同一项任务时，无需反复编写完成该任务的代码，而只需调用执行该任务的函数，让Python运行其中的代码。
# 通过使用函数，程序的编写、阅读、测试和修复都将更容易。

# 1.1 定义函数：
# 定义:
# def hello_world():
#     print("hello world!")

# 调用：
# hello_world()

# 1.2 向函数传递消息：
# def hello_world(user):
#     print("hello" + " " + user.title() + "!")

# name_lists = ["zhangsan", "lisi", "wangwu", "zhaoliu"]

# for name in name_lists:
#     hello_world(name)



# 1.3 实参和形参：
# 形参：函数定义中hello_world(user)中的user是一个形参
# 实参：函数调用时hello_world(name)中的name是一个实参

# 2. 传递实参:
# 2.1 位置实参：
# def hello(name,age):
#     print("hello" + " " + name + ".")
#     print("hello" + " " + age + ".")

# hello("tom","23")
# hello("23","tom")

# 使用位置实参时需注意参数顺序

# 2.2 关键字实参：
# 键字实参是传递给函数的名称—值对，无需考虑位置
# def hello(name,age):
#     print("hello" + " " + name + ".")
#     print("hello" + " " + age + ".")

# hello(age="23",name="tom")

# 2.3 默认值：
# 编写函数时，可给每个形参指定默认值，如果没有指定参数将使用默认值
# def happy(name,age="23"):
#     print("hello" + " " + name)
#     print("happy" + " " + age)
# happy(name="tom")

# def names(f_name,l_name):
#     full_name = f_name + " " + l_name
#     return full_name.title()

# while True:
#     a_name = input("请输入姓，输入q退出：")
#     if a_name == "q":
#         break
#     b_name = input("请输入名，输入q退出：")
#     if b_name == "q":
#         break
#     full_name = names(a_name,b_name)
#     print(full_name)

# 2.4 传递列表：
# name_lists = ["zhangsan", "lisi", "wangwu", "zhaoliu"]

# def get_user(names):
#     for name in names:
#         print("hello" + " " + name)

# get_user(name_lists)

# 2.5 在函数中修改列表：
# 看一家为用户提交的设计制作3D打印模型的公司。
# 需要打印的设计存储在一个列表中，打印后移到另一个列表中

# 未使用函数：
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
# completed_models = []
# # 模拟打印每个设计，直到没有未打印的设计为止 
# # 打印每个设计后，都将其移到列表completed_models中
# while unprinted_designs:
#     del_design = unprinted_designs.pop()
#     print("已打印" + del_design)
#     completed_models.append(del_design)
# for completed_model in completed_models:
#     print("打印" + completed_model)


# 使用函数:
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
# completed_models = []

# def print_unprinted(unprinted_designs,completed_models):
#     while unprinted_designs:
#         del_design = unprinted_designs.pop()
#         completed_models.append(del_design)

# def print_completed(completed_models):
#     for completed_model in completed_models:
#         print("已打印" + " " + completed_model)

# print_unprinted(unprinted_designs,completed_models)
# print_completed(completed_models)


# 2.6 保留原列表数据
# 函数传递参数时用切片表示法[:] 创建列表的副本。
# print_unprinted(unprinted_designs[:],completed_models)

# 3. 传递任意数量的实参：
# 形参名*name中的星号让Python创建一个名为name的空元组，
# 并将收到的所有值都封装到这个元组中。
# def names(*name):
#     for p_name in name:
#         print(p_name)

# names('iphone case', 'robot pendant', 'dodecahedron')

# 3.1 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
# def names(name,*toppings):
#     print(name)
#     for p_name in toppings:
#         print(p_name)

# names('iphone case', 'robot pendant', 'dodecahedron')  


