'''
使用封装数据的思想
    创建员工类/部门类,修改实现下列功能.
        (1). 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
        (2). 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
        (3). 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
        (4). 定义函数,查找薪资最少的员工
        (5). 定义函数,根据薪资对员工列表升序排列

# 员工列表
list_employees = [
    {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
    {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
    {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
    {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
    {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
]

# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
]
'''


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


class Department:
    def __init__(self, did, title):
        self.did = did
        self.title = title


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000)
]

# 部门列表
list_departments = [
    Department(9001, "教学部"),
    Department(9002, "销售部")
]

print("(1). 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.")


def print_all_employees(list_employees):
    for employee in list_employees:
        print(f"{employee.name}的员工编号是{employee.eid},部门编号是{employee.did},月薪{employee.money}元.")


print_all_employees(list_employees)

print("\n(2). 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.")


def print_all_money_more_than_2w(list_employees):
    for employee in list_employees:
        if employee.money > 20000:
            print(f"{employee.name}的员工编号是{employee.eid},部门编号是{employee.did},月薪{employee.money}元.")


print_all_money_more_than_2w(list_employees)

print("\n(3). 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.")


def print_all_departments_employees(list_employees, list_departments):
    for employee in list_employees:
        for department in list_departments:
            if department.did == employee.did:
                print(f"{employee.name}的部门是{department.title},月薪{employee.money}元.")


print_all_departments_employees(list_employees, list_departments)

print("\n(4). 定义函数,查找薪资最少的员工")


def find_min_money_employee(list_employees):
    min_money_employee = list_employees[0]
    for i in range(1, len(list_employees)):
        if list_employees[i].money < min_money_employee.money:
            min_money_employee = list_employees[i]
    return min_money_employee


min_money_employee = find_min_money_employee(list_employees)
print(f"薪资最少的员工是：{min_money_employee.name}，工资为：{min_money_employee.money}")

print("\n(5). 定义函数,根据薪资对员工列表升序排列")


def sort_list_employees_by_money(list_employees):
    for i in range(len(list_employees) - 1):
        for j in range(i + 1, len(list_employees)):
            if list_employees[j].money < list_employees[i].money:
                list_employees[i], list_employees[j] = list_employees[j], list_employees[i]
    return list_employees


sorted_list_employees = sort_list_employees_by_money(list_employees)
for employee in sorted_list_employees:
    print(employee.__dict__)
