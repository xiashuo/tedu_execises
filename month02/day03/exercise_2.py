"""
重点代码
练习2：
使用input输入一个系统中的普通文件路径，将这个文件拷贝到
练习代码所在目录。

提示 ： 文件是二进制文件还是文本文件不确定  用什么方式打开？
       文件可能很大   很大的文件不能一次性read？
       从源文件中获取内容 --》 写入到一个新文件中

"""

def copy(old_file):
    """
    拷贝一个文件到当前目录下
    :param old_file: 要拷贝的文件
    :return: None
    """
    new_file = old_file.split('/')[-1] # 提取文件名字
    fr = open(old_file,'rb') # 不确定文件类型
    fw = open(new_file,'wb') # 写的方式打开新文件

    # 边读边写
    while True:
        data = fr.read(1024) # 从源文件读取内容
        # 到文件结尾再读data为空
        if not data:
            break
        fw.write(data) # 写入新文件
    fr.close()
    fw.close()

# __name__校验  如果这个py模块被别人导入则if中的内容不会执行
# 如果作为主模块自己运行的时候就会执行
if __name__ == '__main__':
    file = input("要拷贝的文件:")
    copy(file) # file可能包含路径







