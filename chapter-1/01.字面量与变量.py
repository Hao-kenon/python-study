#字面量写法
# print(100)#整数(int)
# print(3.14)#浮点数(float)
# print(True)#布尔值(bool)
# print(False)#布尔值(bool)
# print('Hello Python')#字符串(str)
# print(None)#空值(NoneType)
#
# #布尔类型本质也是整数(True - 1,False - 0)
# print(True + 1)#2
# print(False - 1)#-1



#变量----Python是动态类型语言，一个变量可以存储不同的数据,但是在开发中，推荐变量只存储一种类型的数据
# num = 100
# print(num)
#
# num = num + 1
# print(num)
#
# num = 'OK'
# print(num)
#
# a  = True
# print(a)


#案列
# base = 20.1
# incr = 50
# print("未来第一个月数据",base + incr)
# print("未来第二个月数据",base + incr + incr)
#
# #案列 - pro  一次性定义多个变量
# base, incr = 20.1, 50
# print("未来第一个月数据",base + incr)
# print("未来第二个月数据",base + incr + incr)



#标识符
# true = 1
# print(true)
#
# name6 = ("Python")
# print(name6)


#交换变量值
# a = 10
# b = 20
#
# #错误
# # a = b
# # b = a
# # print(a,b)
#
# c = a
# a = b
# b = c
# print(a,b)

#交换变量值 - pro
a = 100
b = 200
c = 300

d = a
a = b
b = c
c = d
print(a,b,c)