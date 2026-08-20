# i = 0
# while i < 10:
#    print("hello world")
#    i += 1
# else:
#     print("goodbye")


#案例 计算100以内偶数之和

i = 0
total = 0
while i <= 100:
    if i % 2 == 0:
        total = total + i
    i = i + 1
print(f"total: {total}")