'''
 参照下列代码,定义函数,计算孩子身高.
    father_height = float(input("请输入父亲的身高（厘米）:"))
    mother_height = float(input("请输入母亲的身高（厘米）:"))
    son_height = (father_height + mother_height) * 0.54
    print("预测儿子的身高是:" + str(son_height) + "厘米")
'''


def predict_son_height(father_height, mother_height):
    son_height = (father_height + mother_height) * 0.54
    return son_height


son_height = predict_son_height(175, 165)
print(f"预测儿子的身高是：{son_height:.0f}")
