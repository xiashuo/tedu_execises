'''
参照下列代码,定义函数,计算税率和速算扣除数.
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
        # print('税率是%.0f%%速算扣除数是%d' % (tax_rate * 100, deduction))
        print(f'税率是{tax_rate * 100}%速算扣除数是{deduction}')
'''


def calculate_tax_rate_and_deduction(money):
    dict_tax_rate_deduction = {
        36000: (0.03, 0),
        144000: (0.1, 2520),
        300000: (0.2, 16920),
        420000: (0.25, 31920),
        660000: (0.3, 52920),
        960000: (0.35, 85920)
    }
    for k, v in dict_tax_rate_deduction.items():
        if money <= k:
            return v
    return 0.45, 181920


tax_rate, deduction = calculate_tax_rate_and_deduction(50000)
print(f'税率是{tax_rate * 100}%，速算扣除数是{deduction}')
