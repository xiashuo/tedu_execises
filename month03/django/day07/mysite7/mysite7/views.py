import time

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(60)
def test_cathe(request):
    time.sleep(3)
    t1 = time.time()
    return HttpResponse(f'{t1}')


def test_mw(request):
    return HttpResponse('test_mw ok')


def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')

    elif request.method == 'POST':
        return HttpResponse('post is ok')
