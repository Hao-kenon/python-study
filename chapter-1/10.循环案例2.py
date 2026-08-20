import random
random_number = random.randint(1,100)

while True:
    num = int(input("请输入1 - 100以内的数:"))

    if num > random_number:
        print("猜大了！")
    elif num < random_number:
        print("猜小了！")
    else:
        print("猜对了")
        break
print(f"随机数是{random_number}")