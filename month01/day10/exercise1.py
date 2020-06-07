'''
画出下列代码内存图
'''


class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color


# 1
list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]

# 2
for item in list_phones:
    if item.color == "白色":
        item.price = 0
print(list_phones[0].price)  # ?
print(list_phones[-1].price)  # ?


# 3
def find():
    for item in list_phones:
        if item.brand == "华为2":
            return item


result = find()
print(result.brand, result.price, result.color)  # ?
