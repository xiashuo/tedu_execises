"""
    可迭代对象的工具箱
"""


class IterableHelper:
    """
        可迭代对象助手类:负责定义对可迭代对象的常用操作
    """

    @staticmethod
    def find_all(list_target, func):
        """

        :param list_target:
        :param func:
        :return:
        """
        for item in list_target:
            if func(item):
                yield item

    @staticmethod
    def find_single(list_target, func):
        for item in list_target:
            if func(item):
                return item

    @staticmethod
    def get_count(list_target, func):
        count = 0
        for item in list_target:
            if func(item):
                count += 1
        return count

    @staticmethod
    def get_all_by_condition(list_target, func):
        for item in list_target:
            yield func(item)

    @staticmethod
    def find_min(list_target, func):
        min_value = list_target[0]
        for i in range(1, len(list_target)):
            if func(list_target[i]) < func(min_value):
                min_value = list_target[i]
        return min_value

    @staticmethod
    def find_max(list_target, func):
        max_value = list_target[0]
        for i in range(1, len(list_target)):
            if func(list_target[i]) > func(max_value):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def sort_by(list_target, func):
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func(list_target[j]) < func(list_target[i]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]
        return list_target
