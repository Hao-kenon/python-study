#定义列表 - list

# s = [1,2,3,4,5,"YES","NO"]
#
# print(type(s))
#
# #访问列表元素
# #获取
# print(s[0]) #正向索引
# print(s[-7]) #反向索引
#
# print(s[2])
# print(s[-5])
# #修改
#
# s[5] = "TRUE"
# print(s[5])
# print(s)
#
# #删除
#
# del s[1]
# print(s)
#
# #遍历
#
# for item in s:
#     print(item)


# --------------------- list 切片 ----------------------------
# s = ["A","B","C","D","E","F","G","H","I","J"]
#
# #切片操作[开始索引:结束索引:步长]
# print(s[0:5:1]) #不包含结束索引
# print(type(s[0:5:2])) # list
#
#
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[0:5:2])
# print(s[:5:2])
# print(s[:-2:])

# --------------------- list 常用方法 ----------------------------
#列表定义

# s = [56,90,88,90,65,100,209,72,145]
# print(s)
#
# # append(): 列表尾部追加元素
# s.append(188)
# print(s)
#
# #insert(): 在指定元素之前插入元素
# s.insert(2,80)
# print(s)
#
# #remove():移除列表中第一个匹配到的元素
# s.remove(90)
# print(s)
#
# #pop(): 删除指定索引的元素,若无指定值默认删除最后一个元素
# e = s.pop(1)
# print(e)
#
# #sort():对列表元素排序，必须是同一类型元素
# s.sort()
# print(s)
#
# #reverse():列表反转
# s.reverse()
# print(s)

# --------------------- list 案例 ----------------------------

# #输入10个元素存储到列表中，并排序，输出最大值和最小值以及平均值
# s = []
# for i in range(10):
#     num = int(input("请输入一个数字:"))
#     s.append(num)
# print(s)
#
# s.sort()
# print(f"排序后的列表:{s}")
#
# #sum() 求和函数    len() 获取列表长度
# print(f"最大值是:{s[9]},最小值是:{s[0]}")
# print(f"平均值是:{sum(s)/len(s)}")

#合并列表,并去除重复元素

# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
#
# # 1.合并
# # for num in num_list2:
# #     num_list1.append(num)
# # print(f"合并后的list:{num_list1}")
#
# #简化
# #num_list = [*num_list1,*num_list2]
# num_list = num_list1 + num_list2
# print(f"合并后的list:{num_list}")
#
#
# # 2.去除重复元素
# new_list = [] #存储去重后的list
#
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
#     # if num in new_list:
#     #     continue
#     # new_list.append(num)
# print(f"去重后的list:{new_list}")


#生成 1 - 20平方
#法一:
num_list1 = []
for i in range(1,21):
    num_list1.append(i ** 2)
print(num_list1)

#法二:
num_list2 = [i**2 for i in range(1,21)]
print(num_list2)

#提取列表中所有偶数，计算平方并组成新列表
#法一:
num_list3 = [1,2,3,4,5,6,7,8,9,10]
print(num_list3)
new_list = []
for num in num_list3:
    if num % 2 == 0:
        new_list.append(num ** 2)
print(new_list)

#法二:
# new_list = [num**2 for num in num_list3 if num % 2 == 0]
# print(new_list)