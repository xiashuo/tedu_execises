from typing import List

from model import CommodityModel


class CommodityController:
    def __init__(self):
        self.__list_commodity = []  # type:List[CommodityModel]
        self.__start_id = 1001

    def add_commodity(self, commodity: CommodityModel):
        commodity.cid = self.__start_id
        self.__start_id += 1  # 商品编号自增长
        self.__list_commodity.append(commodity)

    def show_all_commodies(self):
        for commodity in self.__list_commodity:
            print(commodity.__dict__)

    def delete_commodity(self, cid_delete):
        if CommodityModel(cid_delete) in self.__list_commodity:
            self.__list_commodity.remove(CommodityModel(cid_delete))
            return True
        return False
