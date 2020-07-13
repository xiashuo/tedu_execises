from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField("书名", max_length=50, unique=True, default='')
    pub = models.CharField("出版社", max_length=50, default='')
    price = models.DecimalField('定价', max_digits=7, decimal_places=2, default=0.0)
    desc = models.CharField("描述", max_length=50, default='')

    class Meta:
        db_table = 'book'


class Author(models.Model):
    name = models.CharField("姓名", max_length=50, default='')
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("邮箱", max_length=50, null=True)

    class Meta:
        db_table = 'author'
