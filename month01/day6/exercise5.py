'''
在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
    提示:使用字典
'''
dict_RGBA={"R":"红色","G":"绿色","B":"蓝色","A":"透明度"}
RGBA=input("输入颜色（RGBA）：")
print(dict_RGBA.get(RGBA,"颜色不存在"))
