"""
    参照demo01,完成员工管理器的迭代
"""


class EmployeeIterator:  # 迭代器
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        try:
            self.index += 1
            return self.data[self.index]
        except IndexError:
            raise StopIteration()


class EmployeeManager:  # 可迭代对象

    def __init__(self):
        self.list_employees = []

    def add_employee(self, emp):
        self.list_employees.append(emp)

    def __iter__(self):
        # 返回新迭代器对象
        return EmployeeIterator(self.list_employees)


manager = EmployeeManager()
manager.add_employee("程序员")
manager.add_employee("测试员")
manager.add_employee("销售")

for item in manager:
    print(item)
