"""
在log.txt文件上完成，写一个程序
          input输入一个接口名称
          得到该接口描述中的 address is 的地址值

          提示 ： 每段之间一定有空行
                 每段的首单词就是接口名称
                 地址 三组每组4个16进制数
"""
import re

# 生成每一段内容
def get_info():
    # 能否提取出一段内容
    f = open("log.txt")
    # 每次ｗｈｉｌｅ获取一段内容
    while True:
        # 获取一段内容
        info = ""
        for line in f:
            if line == '\n':
                break # 获取一段跳出ｆｏｒ
            info += line

        #　info 为空字符串，文件结尾
        if not info:
            f.close()
            return
        else:
            yield info  # 提供给使用者一段内容

def main():
    # 输入接口名称
    name = input(">>")
    # 每次通过生成器获取一段内容
    for info in get_info():
        # 是否为想要的段落
        obj = re.match(r"\S+",info) # 在一段内容中匹配首单词
        # 是目标段落执行if 否则继续for循环
        if name == obj.group():
            pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            result = re.search(pattern,info) # 匹配地址
            if result:
                print(result.group())
            else:
                # 没有匹配到
                print("Unknown")
            return
    print("没有该接口名称")

main()






