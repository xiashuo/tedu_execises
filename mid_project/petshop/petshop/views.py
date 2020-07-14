from django.shortcuts import render


def index_view(request):
    return render(request,'index.html')


def page404_view(request):
    return render(request,'404page.html')