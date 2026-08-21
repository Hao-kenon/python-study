"""
面向对象高级-封装:
    将数据(属性)和操作数据的方法绑定在一起，形成一个独立的单元，即对象。
    通过封装，可以隐藏对象的内部实现细节，只暴露必要的接口给外部使用。
    这样可以提高代码的可维护性和可扩展性，同时也可以提高代码的安全性，防止外部直接修改对象的内部状态。

    1. 私有属性：在属性名前加__，表示该属性是私有的，不能在类的外部访问。
    2. 私有方法：在方法名前加__，表示该方法是私有的，不能在类的外部调用。
"""

class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand              #品牌
        self.model = model              #型号
        self.color = color              #颜色

        self.__owner = owner              #所有者 __表示私有属性

    def start(self):
        print(f"{self.brand} {self.model}正在启动")

    #私有属性不对外暴露，但可通过内部方法访问
    def run(self):
        print(f"{self.__owner} : {self.brand} {self.model}正在运行")


    def stop(self):
        print(f"{self.brand} {self.model}正在停止")


    def get_owner(self):
        return self.__owner[0:1]+'**'

    def charge(self):
        print(f"{self.brand} {self.model}正在补充燃料")

#子类在重写父类方法时，需要调用父类的方法，可以通过父类名.方法名(self)/super().方法名()
class FuelCar(Car):
    def charge(self):

        # Car.charge(self)
        super().charge()
        print(f"{self.brand} {self.model}正在充电")

class ElectricCar(Car):
    def charge(self):
        # 方式一: super().方法名()
        # super().charge()

        #方式二: 类名.方法名(self)
        Car.charge(self)
        print(f"{self.brand} {self.model}正在加油")


if __name__ == '__main__':
    c1 = ElectricCar('BWM','x5','黑色','张三')
    c1.charge()

    c2 = FuelCar('Audi','A6','黑色','李四')
    c2.charge()