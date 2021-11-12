from django.db import models

class user(models.Model):
    # 아이디, 비밀번호, 이름, 배송받을 주소,

    cus_id = models.CharField(max_length=10, verbose_name='고객 아이디', blank=False)
    cus_pw = models.CharField(max_length=20, verbose_name='고객 비밀번호', blank=False)
    cus_name = models.CharField(max_length=20, verbose_name='고객 이름', blank=False)
    cus_address = models.TextField(max_length=100, verbose_name='고객 주소', blank=False)

