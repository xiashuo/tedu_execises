from django.http import HttpResponse


def operator_view(request, a, op, b):
    if op == 'add':
        res = a + b
    elif op == 'sub':
        res = a - b
    elif op == 'mul':
        res = a * b
    else:
        res="your op is wrong!"
    return HttpResponse(f"结果：{res}")

def birthday_view(request,year,month,day):
    return HttpResponse(f"生日为：{year}年{month}月{day}日")
