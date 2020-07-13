from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Book


def add_book(request):
    res = Book.objects.create(title='javascript', pub='人民出版社', price=23, market_price=28)
    return HttpResponse(f'{res}<br>插入成功')


def all_book(request):
    books = Book.objects.all()
    return render(request, 'bookstore/all_book.html', {'booklist': books})


def edit_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        print(e)
    if request.method == 'GET':
        return render(request, 'bookstore/edit_book.html', locals())
    elif request.method == 'POST':
        book.price = request.POST.get('price')
        book.market_price = request.POST.get('market_price')
        book.save()
        return HttpResponseRedirect('/bookstore/allbook')
