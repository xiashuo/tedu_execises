from django.urls import path
from . import views
urlpatterns = [
    path('addbook',views.add_book),
    path('allbook',views.all_book),
    path('editbook/<int:book_id>',views.edit_book),
]