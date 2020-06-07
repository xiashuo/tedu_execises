'''
参照下列代码,定义函数,计算社保缴纳费用.
    salary_before_tax = float(input("请输入税前工资："))
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    print("个人需要缴纳社保费用：" + str(social_insurance))
'''


def calculate_social_security_contributions(salary_before_tax):
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    return social_insurance


social_insurance = calculate_social_security_contributions((18000))
print("个人需要缴纳社保费用：" + str(social_insurance))
