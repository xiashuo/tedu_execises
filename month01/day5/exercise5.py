'''
八大行星：
	"水星" "金星" "地球" "火星" "木星" "土星" "天王星" "海王星"
    -- 创建列表存储4个行星："水星" "金星" "火星" "木星"
    -- 插入"地球"、分别追加"土星" "天王星" "海王星"
    -- 打印距离太阳最近、最远的行星(第一个和最后一个元素)
    -- 打印太阳到地球之间的行星(前两个行星)
    -- 删除"海王星",删除第四个行星
    -- 倒序打印所有行星(一行一个)
'''
list1 = ["水星", "金星", "火星", "木星"]
list1.insert(2, "地球")
list1.append("土星")
list1.append("天王星")
list1.append("海王星")
print(f"距离太阳最近、最远的行星分别是：{list1[0]}，{list1[-1]}")
print(f"阳到地球之间的行星是：{list1[0]}，{list1[1]}")
print("倒序打印所有行星：")
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
list1.remove("海王星")
print(list1)
del list1[3]
print(list1)
