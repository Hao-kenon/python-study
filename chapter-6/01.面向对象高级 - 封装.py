"""
面向对象高级 - 封装:
    将属性 (数据) 和操作数据的方法 (函数) 结合成一个独立的单元 (类)。
    通过封装，可以隐藏对象的内部实现细节，只暴露必要的接口给外部使用。
    封装可以提高代码的可维护性和可扩展性，同时也可以提高代码的安全性，防止外部直接修改对象的内部状态。

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

    def __control_fuel(self):
        """私有方法，控制燃油。"""
        print(f"{self.brand} {self.model}正在控制燃油")

    def get_owner(self):
        """获取脱敏后的车主姓名。

        Returns:
            车主姓名的第一个字加**，例如：张**
        """
        return self.__owner[0:1] + '**'

if __name__ == '__main__':
    car = Car('Audi', 'A6', '白色', '张三')
    print(car.brand)
    print(car.model)
    print(car.color)

    print(car.get_owner())

    car.start()
    car.run()
    car.stop()
