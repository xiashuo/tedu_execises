from django.http import HttpResponse, HttpResponseRedirect


def page1_view(request):
    return HttpResponse("这是page1页面")


def operator_view(request, a, op, b):
    if op == 'add':
        res = a + b
    elif op == 'sub':
        res = a - b
    elif op == 'mul':
        res = a * b
    else:
        res = "your op is wrong!"
    return HttpResponse(f"结果：{res}")


def birthday_view(request, year, month, day):
    return HttpResponse(f"生日为：{year}年{month}月{day}日")
    # return HttpResponseRedirect("/5/add/1")


def test_get_post(request):
    # return HttpResponse(f"{request.GET.get('a')},{request.GET.get('b')}<br>{request.GET.getlist('b')[0]}")
    if request.method == 'GET':
        return HttpResponse('''
        <form method='post' action="/test_get_post">
            姓名:<input type="text" name="username">
            <input type='submit' value='登陆'>
        </form>
        ''')
    if request.method=='POST':
        return HttpResponse(f"用户名为：{request.POST.get('username')}")
