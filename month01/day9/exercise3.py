'''
# 员工列表 eid表示员工编号 did 表示部门编号
dict_employees = [
    {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
    {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
    {"eid": 1003, "did": 1002, "name": "猪八戒", "money": 20000},
    {"eid": 1004, "did": 1001, "name": "沙僧", "money": 30000},
    {"eid": 1005, "did": 1001, "name": "小白龙", "money": 15000},
]

# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
]
# （1）. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# （2）. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# （3）. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
# （4）. 查找薪资最少的员工
# （5）. 根据薪资对员工列表升序排列
'''

dict_employees = [
    {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
    {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
    {"eid": 1003, "did": 1002, "name": "猪八戒", "money": 20000},
    {"eid": 1004, "did": 1001, "name": "沙僧", "money": 30000},
    {"eid": 1005, "did": 1001, "name": "小白龙", "money": 15000},
]
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 1001, "title": "市场部"},
    {"did": 1002, "title": "研发部"},
]

print("（1）. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.")


def print_all_employees(dict_employees):
    for employee in dict_employees:
        print(f"{employee['name']}的员工编号是{employee['eid']}，部门编号是{employee['did']}，月薪{employee['money']}元。")


print_all_employees(dict_employees)

print()
print("（2）. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.")


def print_money_more_than_2w(dict_employees):
    for employee in dict_employees:
        if employee['money'] > 20000:
            print(f"{employee['name']}的员工编号是{employee['eid']}，部门编号是{employee['did']}，月薪{employee['money']}元。")


print_money_more_than_2w(dict_employees)

print()
print("（3）. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.")


def print_all_employees_did(dict_employees, list_departments):
    for employee in dict_employees:
        for department in list_departments:
            if department['did'] == employee['did']:
                print(f"{employee['name']}的部门是{department['title']},月薪{employee['money']}元.")


print_all_employees_did(dict_employees, list_departments)

print()
print("（4）. 查找薪资最少的员工")


def get_min_salary_employee(dict_employees):
    min_salary_employee = dict_employees[0]
    for i in range(1, len(dict_employees)):
        if dict_employees[i]['money'] < min_salary_employee['money']:
            min_salary_employee = dict_employees[i]
    return min_salary_employee


min_salary_employee = get_min_salary_employee(dict_employees)
print(
    f"薪资最少的员工是{min_salary_employee['name']}，员工编号是{min_salary_employee['eid']}，部门编号是{min_salary_employee['did']}，月薪{min_salary_employee['money']}元。")

print()
print("（5）. 根据薪资对员工列表升序排列")


def sort_employee_by_salary(dict_employees):
    for i in range(len(dict_employees) - 1):
        for j in range(i + 1, len(dict_employees)):
            if dict_employees[j]['money'] < dict_employees[i]['money']:
                dict_employees[i], dict_employees[j] = dict_employees[j], dict_employees[i]
    return dict_employees


print(sort_employee_by_salary(dict_employees))
