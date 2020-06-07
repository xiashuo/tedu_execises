class CommodityModel:
    """
        商品类
    """

    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    @property
    def cid(self):
        return self.__cid

    @cid.setter
    def cid(self, value):
        self.__cid = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __eq__(self, other):
        return self.__cid == other.cid

    def __lt__(self, other):
        pass
