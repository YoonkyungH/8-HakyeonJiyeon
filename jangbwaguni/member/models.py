
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # 아이디, 비밀번호, 이름, 배송받을 주소,

    cus_name = models.CharField(max_length=20, verbose_name='고객 이름', blank=True)
    cus_address = models.TextField(max_length=100, verbose_name='고객 주소', blank=True)

    REQUIRED_FIELDS = []

    def __str__(self):  # 객체가 설정한 [cus_name]으로 보여짐
        return self.cus_name + ", " + self.username

    # class Meta:
    #     db_table = 'member_user'
