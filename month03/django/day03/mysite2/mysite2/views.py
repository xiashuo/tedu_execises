from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def test_html(request):
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)
    dic = {}
    dic['script'] = '<script> alert(11)</script>'
    dic['int'] = 11
    dic['list']=['xiashuo','lisi','毛六']
    # dic['list']=[]
    return render(request, 'test_html.html', dic)


def mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    if request.method == 'POST':
        try:
            x = int(request.POST.get('x'))
            y = int(request.POST.get('y'))
        except:
            return render(request,'mycal.html',{"res":"请输入数字！"})
        op = request.POST.get('op')
        if op == 'add':
            res = x + y
        elif op == 'sub':
            res = x - y
        elif op == 'mul':
            res = x * y
        elif op == 'div':
            if y==0:
                res="除数不能为0！"
            else:
                res = x / y
        return render(request,'mycal.html',{"res":res,"x":x,"y":y,"op":op})

def base_view(request):
    return render(request,'base.html',)

def music_view(request):
    return render(request,'music.html')