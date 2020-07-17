from django.db import models

# Create your models here.
class Author(models.Model):
    '''作家模型类'''
    name = models.CharField('作家', max_length=50)

class Wife(models.Model):
    '''作家妻子模型类'''
    name = models.CharField("妻子", max_length=50)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)  # 增加一对一属性
