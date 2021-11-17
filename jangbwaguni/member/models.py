from django.contrib.auth.forms import UsernameField
from django.db import models


# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     # username = UsernameField(max_length=10, verbose_name='이름', default=True)
#     # password = models.CharField(max_length=20, verbose_name='비밀번호', default=True)
#     address = models.TextField(max_length=100, verbose_name='고객 주소', default=True)

from django.contrib.auth.models import User
from django.contrib import auth


class User(models.Model):
    # 아이디, 비밀번호, 이름, 배송받을 주소,

    cus_id = models.CharField(max_length=10, verbose_name='고객 아이디', blank=True)
    cus_pw = models.CharField(max_length=20, verbose_name='고객 비밀번호', blank=True)
    cus_name = models.CharField(max_length=20, verbose_name='고객 이름', blank=True)
    cus_address = models.TextField(max_length=100, verbose_name='고객 주소', blank=True)

    def __str__(self):  # 객체가 설정한 [cus_name]으로 보여짐
        return self.cus_name

    # class Meta:
    #     db_table = 'member_user'
