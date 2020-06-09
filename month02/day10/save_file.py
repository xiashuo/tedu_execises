import pymysql
from tools.mysql_tool import MysqlTool

MysqlTool.connect_database("stu")
# 将图片以二进制形式存入数据库
with open('touxiang.jpg', 'rb') as f:
    data = f.read()
# 修改数据
# if MysqlTool.update("cls", "image", data, "id", 8):
#     print("修改数据成功！")
#
# # 将图片从数据库中取出来，并保存为图片。
# res = MysqlTool.query_by("cls", "id", 7)
# with open("img2.jpg", "wb") as f:
#     f.write(res[0][5])
# 删除数据
# if MysqlTool.delete("cls","id",10):
#     print("删除数据成功！")

# 插入数据
if MysqlTool.insert("cls",name='孙七',age=22,sex='w',score=98):
    print("插入数据成功")
MysqlTool.close()
