#元组
#Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
#当需要创建一系列不可修 改的元素，元组可以满足这种需求。
#元组看起来跟列表类似，但使用圆括号来标识。

#1.定义元组
dimensions = (200, 50)
# print(dimensions)
# print(dimensions[1])

#2.遍历元组中的所有值
# for dimension in dimensions:
#     print(dimension)

#3.修改元组变量
#虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组
dimensions = (400, 200)
print(dimensions)
