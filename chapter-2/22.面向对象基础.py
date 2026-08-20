
# #定义类
# class Car:
#     # __init__ 方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
#     def __init__(self, c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型对象初始化完毕")
#
# #创建对象
# c1 = Car("red","BWM","X7",800000)
# print(c1.__dict__)
#
#
# c2 = Car("black","奔驰","e300",800000)
# print(c2.__dict__)


# ---------------------定义类 实例方法----------------------------

# class Car:
#     def __init__(self, c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#
#     #定义实例方法
#     def running(self):
#         print(f"{self.brand}{self.name} 正在高速行驶！")
#
#     def total_cost(self,discount,rate):
#         """
#         计算提车的总费用，包含两个部分:价格和税费
#         :param discount:折扣
#         :param rate:税率
#         :return:总费用
#         """
#         total_cost = self.price * discount + rate * self.price
#         return total_cost
#
#     #魔法方法
#     def __str__(self):
#         return f"{self.color} {self.brand} {self.name} {self.price}"
#     def __eq__(self,other):
#         return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
#     def __lt__(self,other):
#         return self.price < other.price
#
# #测试
# c1 = Car("red","BWM","X7",800000)
# print(c1)
# c2 = Car("black","奔驰","e300",1000000)
# print(c1==c2)
# print(c1<c2)
# c1.running()
# c1.running()
# total = c1.total_cost(0.9,0.1)
# print(total)


# ---------------------定义类 实例属性----------------------------
class Car:
    #类属性(所有实例对象共享)
    wheel = 4
    tax_rate = 0.1

    def __init__(self, c_color,c_brand,c_name,c_price):
        #实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

    #定义实例方法
    def running(self):
        print(f"{self.brand}{self.name} 正在高速行驶！")

    def total_cost(self,discount,rate):
        total_cost = self.price * discount + rate * self.price
        return total_cost

c1 = Car("red","BWM","X7",800000)
print(c1.brand)
print(c1.wheel) #通过实例对象，查找属性时，会先查找实例属性；实例属性不存在，再查找类属性

#通过类名访问类属性
print(Car.wheel)