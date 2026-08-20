# score = 680
# if score >= 680:
#     print("欢迎来到清华读书！")
#
# print("---------------------")
from unicodedata import digit

# 案例实现账号登录成功 账号: 18344757695 密码: 666888
ack_account = "18344757695"
ack_password = "666888"

# # 1. 接受账号和密码
# account = input("请输入账号:")
# password = input("请输入密码:")
#
# # 2. 判断账号和密码是否正确
# if account == ack_account and password == ack_password:
#     print("密码正确, 欢迎登录")
# # 3. 账号和密码有错误
# if account != ack_account or password != ack_password:
#     print("账号或密码错误！")


#-------------------------------------------------------------
# if else

# account = input("请输入账号:")
# password = input("请输入密码:")
#
# if account == ack_account and password == ack_password:
#     print("密码正确, 欢迎登录")
# else:
#     print("账号或密码错误,登录失败")

#-------------------------------------------------------------
# 判断平年和闰年

# year = int(input("year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

#-------------------------------------------------------------
# #例 1
# num = int(input("num:"))
#
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")
#
# #例 2
# age = int(input("age:"))
#
# if age >= 18:
#     print(f"{age} is old")
# else:
#     print(f"{age} is young")
#
# #例 3
# digit = int(input("digit:"))
#
# if digit > 0:
#     print(f"{digit} is positive")
# elif digit < 0:
#     print(f"{digit} is negative")
# else:
#     print(f"{digit} is zero")
#
# #例 4
# score = int(input("score:"))
# if score >= 60:
#     print(f"{score} is good")
# else:
#     print(f"{score} is bad")

#综合案列  三角形判别
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("等边三角形")
    elif a == b or b == c or a == c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("不是三角形")
