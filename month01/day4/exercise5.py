'''
(选做)一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)
    -- 全过程总共移动多少米?
   提示:
       数据/操作
'''

distance, height, count = 100, 100, 0
while height > 0.01:
    height /= 2
    count += 1
    distance += height * 2  # 累加起落距离
    # print(f"第{count}次弹起来的高度是{height}米,总共移动{distance}米")
print("总共弹起{count}次")
print("总共走了{distance}米")
