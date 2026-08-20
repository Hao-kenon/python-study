

shopping_cart = {}
menu = """
############## 购物车系统 ##############
#              1.添加购物车            #
#              2.修改购物车            #
#              3.删除购物车            #
#              4.查询购物车            #
#              5.退出购物车            #
######################################
"""

while True:
    print(menu)
    order = input("请选择要执行的操作(1 - 5):")
    match order:
        case "1":#添加购物车
            goods_name = input("输入商品名称:")
            if goods_name in shopping_cart:
                print("该商品已存在")
                continue
            else:
                goods_price = float(input("输入商品价格:"))
                goods_count = int(input("输入商品数量:"))
                shopping_cart[goods_name] = {"goods_price": goods_price, "goods_count": goods_count}

        case "2":#修改购物车
            goods_name = input("输入待修改商品的名称:")
            if goods_name not in shopping_cart:
                print("该商品不存在")
                continue
            goods_price = float(input("更新商品价格:"))
            goods_count = int(input("更新商品数量:"))
            shopping_cart[goods_name] = {"goods_price": goods_price, "goods_count": goods_count}
        case "3":#删除购物车
            goods_name = input("输入待删除商品的名称:")
            if goods_name not in shopping_cart:
                print("该商品不存在")
                continue
            del shopping_cart[goods_name]
            print("删除成功")
        case "4":#查询购物车
            print("商品名称\t商品价格\t商品数量")
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"{goods_name}\t{goods_info['goods_price']}\t{goods_info['goods_count']}")
        case "5":
            print("bye")
            break
        case _ :
            print("命令错误,请重新输入:")