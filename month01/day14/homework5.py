'''
参照info_manager_system.py的框架结构
   完成商品信息管理系统
'''
from typing import List


class CommodityModel:
    """
        商品类
    """

    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.cid == other.cid


class CommodityView:
    def __init__(self):
        self.controller = CommodityController()

    def display_menu(self):
        print("1) 添加商品信息")
        print("2) 显示所有商品信息")
        print("3) 删除商品信息")
        print("4) 退出系统")

    def select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.input_commodity()
        elif item == "2":
            self.show_all_commodities()
        elif item == "3":
            self.delete_commodity()
        elif item == "4":
            exit()
        else:
            print("指令错误!")
        self.select_menu()

    def input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称:")
        commodity.price = input("请输入商品价格:")
        self.controller.add_commodity(commodity)
        print("商品添加成功!")

    def show_all_commodities(self):
        self.controller.show_all_commodies()

    def delete_commodity(self):
        cid_delete = int(input("输入要删除的商品编号:"))
        self.controller.delete_commodity(cid_delete)


class CommodityController:
    def __init__(self):
        self.list_commodity = []  # type:List[CommodityModel]
        self.start_id = 1001

    def add_commodity(self, commodity: CommodityModel):
        commodity.cid = self.start_id
        self.start_id += 1  # 商品编号自增长
        self.list_commodity.append(commodity)

    def show_all_commodies(self):
        for commodity in self.list_commodity:
            print(commodity.__dict__)

    def delete_commodity(self, cid_delete):
        if CommodityModel(cid_delete) in self.list_commodity:
            self.list_commodity.remove(CommodityModel(cid_delete))
            print(f"成功删除编号为{cid_delete}的商品")
        else:
            print("该商品不存在!")


if __name__ == '__main__':
    view = CommodityView()
    view.display_menu()
    view.select_menu()
