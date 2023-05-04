# 修改字符串大小写：
# title() 以首字母大写的方式显示每个单词
# var = "heLlo pytHon"
# print(var.title())

# upper()以大写的方式显示每个单词
# lower()以小写的方式显示每个单词
# var = "heLlo pytHon"
# print(var.upper())
# print(var.lower())

# 拼接字符串：
# var = "hello python"
# var1 = "hello word"
# var3 = var + " " + var1
# print(var + " "  + var1)
# print(var3)

# 将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Tom, would you like to learn some Python today?”。
# name = "Tom"
# message = "would you like to learn some Python today?"
# print("Hello"  " " + name + "," " " + message)

# 调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
# name = "tOm"
# print(name.lower(), name.upper(), name.title(), sep="\n")

# 名言： 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
message_2 = "Albert Einstein once said, “A person who never made a mistake never tried anything new.”"
print(message_2)

# 名言2：将名人的姓名存储在变量famous_person 中，再创建要显示的消息，并将其存储在变量message 中，然后打印这条消息。
famous_person = "Albert Einstein"
message_3 = "A person who never made a mistake never tried anything new."
print(famous_person + " " "once said," " " "“ " + message_3  + "”")


# 2-7 剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。

