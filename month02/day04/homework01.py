import re
with open("log.txt", "r") as f:
    str_content = f.read()
    str_content = re.split(r"\n\n", str_content)[1:]
    input_interface = input("输入接口名称：")
    has_interface=False
    for val in str_content:
        if input_interface == re.match(r"\S+",val).group():
            address = re.search(r"address is [0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}", val).group()
            print(address) if address else print("未找到ip地址")
            has_interface=True
            break

    if not has_interface:
        print("没有该接口")
