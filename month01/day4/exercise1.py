"""
    根据应纳税所得额计算税率与速算扣除数
"""
money = float(input('请输入应纳税所得额'))
if money <= 36000:
    tax_rate = 0.03
    deduction = 0
elif money <= 144000:
    tax_rate = 0.1
    deduction = 2520
elif money <= 300000:
    tax_rate = 0.2
    deduction = 16920
elif money <= 420000:
    tax_rate = 0.25
    deduction = 31920
elif money <= 660000:
    tax_rate = 0.3
    deduction = 52920
elif money <= 960000:
    tax_rate = 0.35
    deduction = 85920
else:
    tax_rate = 0.45
    deduction = 181920
print(f'税率是{tax_rate * 100}%速算扣除数是{deduction}')
