# 10. 将函数存储在模块中：
# 函数的优点之一是，使用它们可将代码块与主程序分离。
# 通过给函数指定描述性名称，可让主程序容易理解得多。
# 还可以更进一步，将函数存储在被称为模块的独立文件中。
# 再将模块导入到主程序中。import 语句允许在当前运行的程序文件中使用模块中的代码。

# 10.1 导入模块：
# 要让函数是可导入的，得先创建模块。
# 模块模是扩展名为.py的文件，包含要导入到程序中的代码。

# 创建一个pizza.py文件

# def make_pizza(size,*toppings):
#     print(size)
#     for topping in toppings:
#         print(topping)


# 新建一个making_pizzas.py文件
# 导入pizza.py文件中的函数使用
# import pizza
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 可以使用模块中的所有函数

# 10.2 导入特定的函数：
# 如果只需要使用其中某一个函数可以用下面的方法：
# from pizza import make_pizza,make_pizza_1,...
#      模块名        函数名

# from pizza import make_pizza
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 10.3 使用as给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长。
# 可指定简短而独一无二的别名。
# from pizza import make_pizza as hp
# hp(12, 'mushrooms', 'green peppers', 'extra cheese')
