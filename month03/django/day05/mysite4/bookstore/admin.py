from django.contrib import admin
from . import models


# Register your models here.


class BookManager(admin.ModelAdmin):
    list_display = ['id','title','pub','price','market_price']
    list_display_links = ['title']
    list_filter = ['pub']
    search_fields = ['title']
    list_editable = ['pub','market_price']


admin.site.register(models.Book, BookManager)
