from bll import CommodityController
from model import CommodityModel


class CommodityView:
    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        print("1) 添加商品信息")
        print("2) 显示所有商品信息")
        print("3) 删除商品信息")
        print("4) 退出系统")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.input_commodity()
        elif item == "2":
            self.show_all_commodities()
        elif item == "3":
            self.delete_commodity()
        elif item == "4":
            exit()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称:")
        commodity.price = input("请输入商品价格:")
        self.__controller.add_commodity(commodity)
        print("商品添加成功!")

    def show_all_commodities(self):
        print("所有商品信息如下：")
        self.__controller.show_all_commodies()

    def delete_commodity(self):
        cid_delete = int(input("输入要删除的商品编号:"))
        if self.__controller.delete_commodity(cid_delete):
            print(f"成功删除编号为{cid_delete}的商品")
        else:
            print("删除失败，该商品不存在！")
