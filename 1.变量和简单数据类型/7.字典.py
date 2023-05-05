# #7.字典:
# #在Python中，字典字是一系列键—-值对值。每个键都与一个值相关联，可以使用键来访问与之相关联的值。
# #与键相关联的值可以是数字、字符串、列表乃至字典。可将任何Python对象用作字典中的值。 
# #在Python中，字典用放在花括号{}中的一系列键--值对表示。

# #7.1创建字典：
# alien = {'color': 'green', 'num': 5}

# #7.2访问字典中的值：
# print(alien['color'])
# print(alien['num'])

# #7.3添加键--值对:
# #字典是一种动态结构，可随时在其中添加键--值对。要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
# alien["x"] = 10
# alien["y"] = 20
# print(alien)

# #7.4修改字典中的值：
# #要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值
# alien["x"] = 30
# alien["y"] = 50
# print(alien)

# #7.5删除键--值对：
# #可使用del语句将相应的键—值对彻底删除。使用del语句时，必须指定字典名和要删除的键
# del alien["x"]
# print(alien)

# #7.6长列表写法：
favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby',
    'phil': 'python', 
    }

# print(favorite_languages)

# #7.7遍历所有的键--值对：
# #使用for循环来遍历，需要声明两个变量，用于存储键—值对中的键和值
# #方法items()返回一个键--值对列表
# for key, value in favorite_languages.items():
#     print(key + ":" + value)

# #7.8遍历字典中的所有键
# #在不需要使用字典中的值时，使用方法keys()
# for name in favorite_languages.keys():
#     print(name)

# #确定某个键是否存在
# if 'a' not in favorite_languages.keys():
#     print("a不存在")

# #7.9按顺序遍历字典中的所有键
# #使用函数sorted()获得按特定顺序排列的键列表的副本
# for name in sorted(favorite_languages.keys()):
#     print(name)

# #7.1.0遍历字典所有值：
# #使用方法values() ，它返回一个值列表，而不包含任何键
# for a in favorite_languages.values():
#     print(a)

# #去重：
# #剔除重复项，可使用集合（set）
for a in set(favorite_languages.values()):
    print(a)