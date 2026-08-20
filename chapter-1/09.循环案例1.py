
while True:
    # 1.接受用户名和密码
    user_name = input("please input your name: ")
    user_password = input("please input your password: ")

    # 2. 校验 用户名和密码不能为空
    if user_name == "" or user_password == "":
        print("用户名和密码不能为空！")
        continue
    # 3. 判断用户名和密码的正确性
    if user_name == "admin" and user_password == "666888":
        print("登录成功")
        break
    elif user_name == "zhangsan" and user_password == "123456":
        print("登录成功")
        break
    elif user_name == "konghao" and user_password == "121212":
        print("登录成功")
        break
    else:
        print("用户名或密码错误")

