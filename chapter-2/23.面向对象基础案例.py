
# 学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名:{self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{self.english}"
    #修改学生成绩

    def update_score(self, chinese = None, math = None, english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

#管理类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []
    #添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名:")

        #判断学生是否存在，若存在，则添加失败(不能重复添加)
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在")
                return

        chinese = int(input("请输入学生语文成绩:"))
        math = int(input("请输入学生数学成绩:"))
        english = int(input("请输学生英语成绩:"))

        #判断成绩是否合理
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
        else:
            print("成绩无效")


    #修改学生成绩
    def update_student(self):
        name = input("请输入学生姓名:")

        #根据学生姓名找到学生信息
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩:{s}")

                chinese = int(input("请输入修改后学生语文成绩:"))
                math = int(input("请输入修改后的学生数学成绩:"))
                english = int(input("请输入修改后的学生英语成绩:"))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("成绩修改成功")
                    print(f"修改后的成绩:{s}")
                    return
                else:
                    print("成绩无效")
                    return

        print("不存在该学生")
    #删除学生成绩

    def delete_student(self):
        name = input("请输入学生姓名:")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("不存在该学生")
    #查询学生成绩
    def query_student(self):
        name = input("请输入学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息:{s}")
                return
        print("不存在该学生")

    #展示所有学生成绩
    def show_student(self):
        for s in self.student_list:
            print(s)

    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系 V{EduManagement.system_version}")
        while True:
            print()
            print("#" * 10)
            print("1.添加学生   2.修改学生  3.删除学生  4.查询指定学生    5.查询所有学生    6.退出系统")
            print("#" * 10)
            print()
            choice = input("请输入要执行的操作(1-6):")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.show_student()
                case "6":
                    print("Bye!")
                    break
                case _ :
                    print("输入有误，请重新输入")

#测试
if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()