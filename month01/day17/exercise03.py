"""
    参照demo01,完成员工管理器的迭代
"""
class EmployeeManager:  # 可迭代对象

    def __init__(self):
        self.list_employees = []

    def add_employee(self, emp):
        self.list_employees.append(emp)

    def __iter__(self):
        for item in self.list_employees:
            yield item

manager = EmployeeManager()
manager.add_employee("程序员")
manager.add_employee("测试员")
manager.add_employee("销售")

for item in manager:
    print(item)
