
#不可修改，有序性，可迭代性
# s = "Hello-Python"

# print(s[4])
# print(s[-8])


#字符串不允许修改
# s[4] = "X"
# print(s[4])

#遍历

# for i in s:
#     print(i, end="")

#切片

# print(s[0:5:1])
# print(s[0:5:])
# print(s[:5:])
# print(s[:5])
#
# print(s[6:12:1])
# print(s[6::1])
#
# print("-------------------------------")
# #步长 --->整数: 从前往后  负数: 从后往前
# #开始索引和结束索引要和步长方向一致
# print(s[-1:-7:-1])
# print(s[::-1])

#常用方法

s = "Hello-Python-Hello-World"

# # find()查找指定字符串第一次出现的位置
# index = s.find("-")
# print(index)
#
# # count() 统计子字符串在字符串中出现的次数
# c = s.count("o")
# print(c)
#
# # upper() 转大写
# s1 = s.upper()
# print(s1)
#
# # lower() 转小写
# s2 = s.lower()
# print(s2)
#
# # split() 将字符串按指定格式切割,以列表格式返回
# slist = s.split("-")
# print(slist)
#
# # strip() 去除字符串两端空格
# ss = s.strip()
# print(ss)
#
# # replace() 把字符串中指定子串替换为指定字符
# sr = s.replace("-", "_")
# print(sr)
#
# # startswith() / endswith() 判断字符串是否已指定内容开始或结尾，返回布尔值
# print(s.startswith("Hello"))
# print(s.endswith("Python"))

# ---------------------------------------------
#案例 1: 邮箱格式判断(包含至少一个@和一个.)

# #法一
# # 1. 接收邮箱
# mail = input("请输入邮箱:")
#
# #2. 判断邮箱格式
# if mail.count("@") == 1 and mail.count(".")>= 1:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")



#法二 in 运算符
# 1. 接收邮箱
mail = input("请输入邮箱:")

#2. 判断邮箱格式
if mail.count("@") == 1 and "." in mail:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")
