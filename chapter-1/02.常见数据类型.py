# print("hello")
# print(type("hello"))
#
#
# print(type(10))
# print(type(3.14))
# print(type(True))
# print(type(None))

# num = -100
# print(type(num))
#
# #常见数据类型 --->isinstance(数据，类型)-->bool值 --> 判定数据是否是指定类型，结果为True or False
# print(isinstance(num,int)) #True
# print(isinstance(num,float)) #False
# print(isinstance(num,bool)) #False


#字符串
#定义字符串的三种方式
# s1 = 'Hello' #单引号定义
# s2 = "World" #双引号定义
# s3 = """
# Hello:
#     My name is kong hao!
# """ #三引号定义多行字符串
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))

#定义字符串 --->
#转义字符 \' \" \n \t
# msg = 'It\'s very good'
#
# msg2 = "It's very good"
#
# msg3 = "Hello 的意思就是\"你好\""
#
# msg4 = 'Hello 的意思就是"你好"'
# print(msg)
# print(msg2)
# print(msg3)
# print(msg4)


#字符串拼接
# s1 = "加油" "别放弃" ",OK"
# print(s1)
#
# msg1 = "加油"
# msg2 = "别放弃"
# print("你说：" + msg1 + " ," + msg2)

# name = "孔浩"
# age = 25
# major = "软件工程"
# hobby = "Python"
# print("大家好，我是" + name + ",今年" + str(age) + "岁，学习的专业是" + major + ",爱好是" + hobby)

#字符串格式化 --->法一:  %s 占位符
name = "孔浩"
age = 25
major = "软件工程"
hobby = "Python"
print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好是%s" % (name, age, major, hobby))

#字符串格式化 --->法二:  f"...{变量名/表达式}..."   #推荐
name = "孔浩"
age = 25
major = "软件工程"
hobby = "Python"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{major},爱好是{hobby}")