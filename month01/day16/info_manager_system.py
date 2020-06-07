"""
    练习1:以封装思想,重构下列代码
        实现打印所有商品的功能.
    练习2:实现根据编号删除商品功能
"""
from typing import List


class CommodityModel:
    """
        商品模型
    """

    def __init__(self, cid=0, name="", price=0.0):
        self.cid = cid
        self.name = name
        self.price = price


class CommodityView:
    """
        商品视图:负责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        print("1) 添加商品信息")
        print("2) 显示所有商品信息")
        print("3) 删除商品信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称:")
        commodity.price = int(input("请输入商品单价:"))
        self.__controller.add_commodity(commodity)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_commoditys(self):
        for commodity in self.__controller.list_commoditys:
            print(f"{commodity.name}的编号是{commodity.cid},单价是{commodity.price}")

    def __delete_commodity(self):
        cid = int(input("请输入商品编号:"))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")


class CommodityController:
    """
        商品逻辑控制:负责处理核心业务逻辑
    """

    def __init__(self):
        self.__list_commoditys = []  # type:List[CommodityModel]
        self.__start_id = 1001

    @property
    def list_commoditys(self):
        return self.__list_commoditys

    def add_commodity(self, commodity):
        commodity.cid = self.__start_id
        self.__start_id += 1
        self.__list_commoditys.append(commodity)

    def remove_commodity(self, cid):
        for i in range(len(self.list_commoditys)):
            if self.list_commoditys[i].cid == cid:
                del self.list_commoditys[i]
                return True
        return False


# 入口
view = CommodityView()
view.main()