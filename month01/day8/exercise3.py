'''
参照下列代码,定义函数,计算加速度.
    distence = float(input("距离为:"))
    initial_velocity = float(input("速度为"))
    time = float(input("时间为"))
    accelerated_speed = 2 * (distence - initial_velocity * time) / time ** 2
    print("加速度为" + str(accelerated_speed))
'''


def get_accelerated_speed(distence,initial_velocity,time):
    accelerated_speed = 2 * (distence - initial_velocity * time) / time ** 2
    return accelerated_speed

accelerated_speed=get_accelerated_speed(100,3,12)
print(f"加速度为:{accelerated_speed:.2f}" )