"""
    业务逻辑层
"""
import collections

from dal import HouseDao


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self):
        return self.__list_houses

    def get_house_by_max_price(self):
        return max(self.__list_houses, key=lambda house: house.total_price)

    def get_house_by_min_area(self):
        return min(self.__list_houses, key=lambda house: house.area)

    def get_house_type(self):
        # dict_house_type = {}
        # for house in self.__list_houses:
        #     # 如果是已经通过过的房源
        #     if house.house_type in dict_house_type:
        #         dict_house_type[house.house_type] += 1  # 增加1
        #     else:
        #         dict_house_type[house.house_type] = 1  # 新
        # return dict_house_type
        # collections 是内置模块
        # Counter 计数器
        #　collections.Counter(["a","a","b","c","c"])  --> {"a":2,"b":1,"c":2}
        return collections.Counter(map(lambda house: house.house_type, self.__list_houses))
