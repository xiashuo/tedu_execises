from common.iterable_tools import IterableHelper

list01 = [3, 43, 4, 56, 6, 76, 87, 9]

# 在list01中找出所有大于10的数字
print(list(IterableHelper.find_all(list01, lambda val: val > 10)))
# 在list01中找出第一个偶数
print(IterableHelper.find_single(list01, lambda val: val % 2 == 0))
# 在list01中找出最大的数字
print(IterableHelper.find_max(list01,lambda val:val))
# 对list01进行升序排列
print(list(IterableHelper.ascending_order_by(list01, lambda val:val)))