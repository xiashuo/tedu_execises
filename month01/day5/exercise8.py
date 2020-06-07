'''
在终端中录入3个疫情省份的确诊人数
    最后打印最大值、最小值、平均值.（使用内置函数实现）
    内置函数:
    --max(x)	返回序列的最大值元素
    --min(x)	返回序列的最小值元素
    --sum(x)	返回序列中所有元素的和(元素必须是数值类型)
'''
list1 = list(map(int, input("输入3个疫情省份的确诊人数：").split()))
print(f"最大值：{max(list1)}")
print(f"最小值：{min(list1)}")
print(f"平均值：：{sum(list1) / len(list1):.0f}")
