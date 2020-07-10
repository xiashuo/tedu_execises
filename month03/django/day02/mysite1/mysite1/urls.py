"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/1',views.page1_view),
    path('<int:a>/<str:op>/<int:b>',views.operator_view),
    path('test_get_post',views.test_get_post),
    re_path(r'birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})',views.birthday_view),
    re_path(r'birthday/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})',views.birthday_view),

]
