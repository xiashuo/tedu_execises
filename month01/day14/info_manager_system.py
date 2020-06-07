"""
    MVC 架构
"""

class StudentModel:
    """
        学生模型:封装数据
    """

    def __init__(self, name="", sex="", age=0, score=0, sid=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score
        self.sid = sid  # 对信息的唯一标识

class StudentView:
    """
        # 学生视图:负责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.controller = StudentController()

    def display_menu(self):
        print("1) 添加学生信息")
        print("2) 显示所有学生信息")
        print("3) 删除学生信息")

    def select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.input_student()
        elif item == "2":
            pass
        elif item == "3":
            pass

    def input_student(self):
        stu = StudentModel()
        stu.name = input("请输入姓名:")
        stu.age = int(input("请输入年龄:"))
        stu.sex = input("请输入性别:")
        stu.score = int(input("请输入成绩:"))
        self.controller.add_student(stu)

class StudentController:
    """
        学生逻辑控制:负责处理核心业务逻辑
    """

    def __init__(self):
        self.list_students = []
        self.start_id = 1001

    def add_student(self, stu):
        stu.sid = self.start_id
        self.start_id += 1  # 学生编号自增长
        self.list_students.append(stu)


# 入口
view = StudentView()
view.display_menu()
view.select_menu()
