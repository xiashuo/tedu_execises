from django.db import models


# Create your models here.
class User(models.Model):
    sex_choices=[
        ('m','男'),
        ('f','女'),
        ('o','其他')
    ]

    user_name = models.CharField('昵称', max_length=50, unique=True)
    password = models.CharField('密码', max_length=50)
    phone_number = models.CharField('手机号', max_length=50)
    register_time = models.DateField('注册时间', auto_now_add=True,null=True)
    email = models.EmailField('邮箱', max_length=50, null=True)
    real_name = models.CharField('真实姓名', max_length=50, null=True)
    id_card = models.CharField('身份证', max_length=50, null=True)
    sex = models.CharField('性别', max_length=50, choices=sex_choices)
    birthday=models.DateField('生日',null=True)
