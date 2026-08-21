"""
面向对象高级 - 继承:
    继承是面向对象的三大特性之一，允许子类继承父类的属性和方法。
    通过继承，可以实现代码的复用，减少冗余代码。
    子类可以访问父类的非私有成员，也可以重写父类的方法。

    1. 私有属性：在属性名前加__表示该属性是私有的，不能在类外部直接访问。
    2. 私有方法：在方法名前加__表示该方法是私有的，不能在类外部直接调用。
"""

class Car:
    """汽车类，封装了汽车品牌、型号、颜色等信息。"""

    def __init__(self, brand, model, color, owner):
        """初始化汽车对象。

        Args:
            brand: 汽车品牌
            model: 汽车型号
            color: 汽车颜色
            owner: 车主姓名（私有属性）
        """
        self.brand = brand              # 品牌
        self.model = model              # 型号
        self.color = color              # 颜色

        self.__owner = owner            # 车主姓名 __表示私有属性

    def start(self):
        """启动汽车。"""
        print(f"{self.brand} {self.model}已经启动")

    # 私有属性不能对外暴露，只能通过内部方法访问
    def run(self):
        """汽车行驶，显示车主信息。"""
        print(f"{self.__owner} : {self.brand} {self.model}正在行驶")

    def stop(self):
        """停止汽车。"""
        print(f"{self.brand} {self.model}已经停止")

    def get_owner(self):
        """获取脱敏后的车主姓名。

        Returns:
            车主姓名的第一个字加**，例如：张**
        """
        return self.__owner[0:1] + '**'


class FuelCar(Car):
    """燃油车类，继承自汽车类。"""
    pass

class ElectricCar(Car):
    """电动车类，继承自汽车类。"""
    pass


if __name__ == '__main__':
    c1 = FuelCar('BWM', 'x5', '白色', '张三')
    c1.start()
    c1.run()
    c1.stop()

    print(c1.brand)
    print(c1.get_owner())
    print(c1.model)
    print(c1.color)
