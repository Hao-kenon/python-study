"""
面向对象高级 - 继承 - 重载:
    方法重载（Override）是指子类重新定义父类的方法，以实现不同的功能。
    通过方法重载，子类可以提供与父类不同的实现，或者扩展父类的功能。
    在重载方法中，可以通过 super() 或 父类名。方法名 (self) 来调用父类的方法。

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

    def charge(self):
        """充电/加油方法，基类中默认实现。"""
        print(f"{self.brand} {self.model}正在补充能源")

# 注意：当重写父类方法时，如果需要调用父类的方法，可以通过 父类名.方法名 (self)/super().方法名 ()
class FuelCar(Car):
    """燃油车类，继承自汽车类。"""

    def charge(self):
        """加油方法，扩展父类的补充能源方法。"""
        # Car.charge(self)
        super().charge()
        print(f"{self.brand} {self.model}正在加油")

class ElectricCar(Car):
    """电动车类，继承自汽车类。"""

    def charge(self):
        """充电方法，扩展父类的补充能源方法。"""
        # 方式一：super().方法名 ()
        # super().charge()

        # 方式二：父类名.方法名 (self)
        Car.charge(self)
        print(f"{self.brand} {self.model}正在充电")


if __name__ == '__main__':
    c1 = ElectricCar('BWM', 'x5', '白色', '张三')
    c1.charge()

    c2 = FuelCar('Audi', 'A6', '白色', '李四')
    c2.charge()
