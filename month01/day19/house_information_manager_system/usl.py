from bll import HouseManagerController


class HouseManagerView:
    """
        # 学生视图:负责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.__controller = HouseManagerController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1) 显示所有房源")
        print("2) 显示最贵的房源")
        print("3) 显示最小的房源")
        print("4) 获取所有户型种类")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__display_houses()
        elif item == "2":
            self.__display_house_by_max_price()
        elif item == "3":
            self.__display_house_by_min_area()
        elif item == "4":
            self.__display_house_type()

    def __display_houses(self):
        for house in self.__controller.list_houses:
            # 定义打印房源的格式
            print(house.__dict__)

    def __display_house_by_max_price(self):
        house = self.__controller.get_house_by_max_price()
        # {'id': 8571, 'title': '中关村创业大街对过 有名的公司入驻其中正规写字楼', 'community': '银科大厦', 'years': '低楼层(共22层)2004年建塔楼', 'house_type': '1室0卫', 'area': 2623.28, 'floor': '低楼层(共22层)2004年建塔楼', 'description': '距离10号线苏州街站898米房本满五年', 'total_price': 120001943.60000001, 'unit_price': 45745.0, 'follow_info': '1人关注 / 共0次带看 / 2个月以前发布'}
        print(house.__dict__)

    def __display_house_by_min_area(self):
        house = self.__controller.get_house_by_min_area()
        # {'id': 15260, 'title': '智德北巷（北河沿大街）+小户型一居+南向', 'community': '智德北巷', 'years': '中楼层(共6层)1985年建板楼', 'house_type': '1室0厅', 'area': 15.29, 'floor': '中楼层(共6层)1985年建板楼', 'description': '距离5号线灯市口站1113米', 'total_price': 2200001.65, 'unit_price': 143885.0, 'follow_info': '56人关注 / 共2次带看 / 8天以前发布'}
        print(house.__dict__)

    def __display_house_type(self):
        dict_house_type = self.__controller.get_house_type()
        for k, v in dict_house_type.items():
            print("户型是%s,数量是%d" % (k, v))
