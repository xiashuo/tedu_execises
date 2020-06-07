"""
    闭包应用
        (理论)核心价值：逻辑连续
        从得到1000元到购买各种商品的逻辑，可以连续，不会中断。

        要素
            有外有内:外负责得钱(一次)，内负责花钱(多次)
            内使用外:购买行为需要外部的钱(封闭保存下来的钱)
            外返回内：以后可以慢慢买商品

        (真正)应用价值：装饰器
"""


def give_gife_money(money):
    print(f"得到了{money}元压岁钱")

    def child_buy(commodity, price):
        nonlocal money
        money -= price
        print(f"孩子买{commodity}，花了{price}钱，还剩下{money}元")

    return child_buy


# 调用外部函数(获得压岁钱)，得到了内部函数(购买行为)
action = give_gife_money(1000)

action("变形金刚", 350)
action("自行车", 600)
