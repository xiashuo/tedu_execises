'''
使用列表存储1970年到2050年之间所有闰年
'''
# leap_years = []
# for year in range(1970, 2051):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         leap_years.append(year)
leap_years=[year for year in range(1970,2051) if year % 4 == 0 and year % 100 != 0 or year % 400 == 0]
print(leap_years)
