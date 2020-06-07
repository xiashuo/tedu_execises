"""
现在有两个文本文件（自己指定），编写一个程序，将两个文件合并为一个

思路： 参考文件拷贝，只不过是拷贝两个文件
"""

def copy(fw,old_file):
    fr = open(old_file,'rb') # 不确定文件类型
    # 边读边写
    while True:
        data = fr.read(1024) # 从源文件读取内容
        # 到文件结尾再读data为空
        if not data:
            break
        fw.write(data) # 写入新文件
    fr.close()

def link_file(file):
    fw = open(file,'wb')  # 打开拼接后的文件
    # 拼几个文件调用几次函数
    copy(fw,"/home/tarena/FTP/2.txt")
    copy(fw,"/home/tarena/FTP/file")
    fw.close()

if __name__ == '__main__':
    link_file('myfile.txt')