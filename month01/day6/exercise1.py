'''
画出下列代码内存图
    -- (1)
        data01 = ["鱼香肉丝", "宫保鸡丁", "水煮鱼"]
        data02 = data01
        data03 = data01[2]
        data04 = data01[:2]

        data02.append("醋溜木须")
        data03 = "红烧肉"
        del data04[0]

        print(data01)
        print(data02)
        print(data03)
        print(data04)
    -- (2)
        list_devices01 = ["存储器", "控制器", "运算器"]
        list_devices01[0] = ["内存", "硬盘"]

        list_devices02 = ["控制器", "运算器", "存储器"]
        # 切片修改,左右容器长度可以不一致
        list_devices02[0:1] = ["内存", "硬盘"]
        list_devices02[1:] = ["cpu"]

        print(list_devices01)
        print(list_devices02)
'''
list_devices01 = ["存储器", "控制器", "运算器"]
list_devices01[0] = ["内存", "硬盘"]

list_devices02 = ["控制器", "运算器", "存储器"]
# 切片修改,左右容器长度可以不一致
list_devices02[0:1] = ["内存", "硬盘"]
print(list_devices02)
list_devices02[1:] = ["cpu"]

print(list_devices01)
print(list_devices02)