# 1.字符串：就是一系列字符。

# 2.使用方法修改字符串大小写：
# 2.1方法lower()将字符串转换为小写
var = "HELLO PYTHON"
print(var.lower())

# 2.2方法upper()将字符串转换为大写
var_1 = "hello python"
print(var_1.upper())

# 2.3方法title()将字符串首字母转换为大写
var_1 = "hello python"
print(var_1.title())

#3.合并字符串：使用+号来拼接
name = "Tom"
message = "HELLO python"
message_1 = name + message
print(message_1)

# 3.1使用+来合并name 、空格和message，并且以小写输出
name = "Tom"
message = "HELLO python"
print(name.lower() + " " + message.lower())

message_1 = name + " " + message
print(message_1.lower())

#4.使用制表符或换行符来添加空白
#4.1使用\t：
name = "hello\tworld"
name_1 = "\thello\tpython"
print(name)
print(name_1)

#4.2使用\n：
name_3 = "hello\nworld\nhai"
print(name_3)

#5.删除空白
#5.1使用rstrip()方法去除末尾的空白
name_4 = "hello python   "
print(name_4.rstrip())

#5.1使用lstrip()方法去除开头的空白
name_5 = "   hello  world"
print(name_5.lstrip())