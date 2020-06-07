"""
    定义员工管理器
        1. 记录所有员工
        2. 计算员工总工资
        程序员：底薪 + 项目分红
        测试员:底薪 + bug数 × 5元
        增加新岗位:
            销售:底薪 + 销售额 * 5%
    写出体现的面向对象特征与原则
    三大特征
        封装:根据需求创建员工管理器类,程序员类,测试员类.
        继承:创建员工类,统一程序员类,测试员类,隔离员工管理器类与具体员工的变化.
        多态:员工管理器类调用员工类,程序员类和测试员类重写计算薪资方法,
              向员工管理器添加程序员对象和测试员对象
    六大原则
        开闭原则:增加新岗位,员工管理器不改变.
        单一职责:
            员工管理器负责管理所有员工
            程序员负责计算程序员的薪资
            测试员负责计算测试员的薪资
        依赖倒置:员工管理器调用员工,不调用具体员工(程序员,测试员)
        组合复用:员工管理器与员工计算薪资算法是组合关系
"""


class EmployeeManager:

    def __init__(self):
        self.list_employees = []

    def add_employee(self, emp):
        self.list_employees.append(emp)

    def calculate_total_salary(self):
        total_salary = 0
        for emp in self.list_employees:
            # 调用的是员工类
            # 执行的是程序员/测试员
            total_salary += emp.get_salary()
        return total_salary


class Employee:
    def get_salary(self):
        """
            计算薪资方法
        :return: 该员工的薪资
        """
        pass


# ------------------------------------------------
class Programmer(Employee):

    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def get_salary(self):
        return self.base_salary + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def get_salary(self):
        return self.base_salary + self.bug_count * 5


manager = EmployeeManager()
manager.add_employee(Programmer(10000, 100000))
manager.add_employee(Tester(8000, 100))
print(manager.calculate_total_salary())
