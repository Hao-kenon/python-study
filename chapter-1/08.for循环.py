# msg = input("输入字符串:")
#
# for i in msg:
#     print(f"元素:{i}")
# else:
#     print("遍历结束")
#

#案例 1.计算100以内所有奇数之和

# total = 0
# for i in range(101):
#     if i % 2 == 1:
#         total += i
# print(f"total: {total}")


#简化
# total = 0
# for i in range(1,101,2):
#     total += i
# print(f"total: {total}")
#案例 2.计算100 - 500之间3倍数的数字之和

# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
# print(f"total: {total}")

#嵌套循环
#打印长方形
#shift + 回车快速新建行

# m = int(input("请输入长度:"))
# n = int(input("请输入宽度:"))
#
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")
#     print()

#打印九九乘法口诀

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} x {i} = {i*j}\t",end=" ")
    print()
