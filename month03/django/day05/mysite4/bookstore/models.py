from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField("书名", max_length=50, unique=True)
    pub = models.CharField("出版社", max_length=50)
    price = models.DecimalField('定价', max_digits=6, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=6, decimal_places=2)

    def __str__(self):
        return f"title：{self.title} pub：{self.pub} price：{self.price} market_price：{self.market_price}"

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField("姓名", max_length=50)
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("邮箱", max_length=50, null=True)
