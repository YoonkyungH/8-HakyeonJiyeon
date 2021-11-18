import sys
from django.contrib.auth.forms import UsernameField
from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     # username = UsernameField(max_length=10, verbose_name='이름', default=True)
#     # password = models.CharField(max_length=20, verbose_name='비밀번호', default=True)
#     address = models.TextField(max_length=100, verbose_name='고객 주소', default=True)

from django.contrib.auth.models import User
from django.contrib import auth


class Customer(models.Model):
    # 아이디, 비밀번호, 이름, 배송받을 주소,

    cus_id = models.CharField(max_length=10, verbose_name='고객 아이디', blank=True, unique=True)
    cus_pw = models.CharField(max_length=200, verbose_name='고객 비밀번호', blank=True)
    cus_nickname = models.CharField(max_length=20, verbose_name='고객 별명', blank=True, unique=True)
    cus_address = models.TextField(max_length=100, verbose_name='고객 주소', blank=True)
    cus_sig_data = models.DateTimeField('date signup costomer', auto_now_add=True, null=True)
    recommended_person = models.CharField(max_length=20, verbose_name='추천인', blank=True)

    def __str__(self):  # 객체가 설정한 [cus_name]으로 보여짐
        return self.cus_nickname

    class Meta:
        db_table = 'customer'
        verbose_name = '고객 가입 정보'


class Rider(models.Model):  # 배달원
    # 아이디, 비밀번호, 배달원 성명, 소개, 지역 선택, 배달 수단, 최소 주문 금액, 통장 사본 유무?, 운전 면허증 유무?, 추천인 코드(선택)
    # 스피드, 신선도, 정확도

    # rider_id = models.CharField(max_length=10, verbose_name='라이더 아이디', blank=True)
    # rider_pw = models.CharField(max_length=20, verbose_name='라이더 비밀번호', blank=True)
    rider_name = models.CharField(
        max_length=100, verbose_name='라이더 이름', blank=True)        # 배달원 이름 필수값
    rider_intro = models.TextField(
        max_length=100, verbose_name='라이더 소개', blank=True)

    AREA_CHOICES = (
        ('GG', '경기도'),
        ('SL', '서울시'),
        ('CC', '충청도'),
        ('GS', '경상도'),
        ('GW', '강원도'),
        ('JL', '전라도'),
        ('JJ', '제주도'),

    )
    rider_area = models.CharField(  # 단일 선택
        choices=AREA_CHOICES,
        max_length=2,
        # max_choices = 1,
        verbose_name='배달 지역',
        blank=True,
    )

    VEHICLE_CHOICES = (
        ('NL', '뚜벅이'),
        ('CR', '차'),   # 자동차
        ('BC', '자전거'),
        ('AB', '오토바이'),
    )
    rider_vehicle = MultiSelectField(   # 다중 선택(~2개) -> 단일 선택으로 바뀜
        choices=VEHICLE_CHOICES,
        max_choices=2,
        verbose_name='배달 수단',
        blank=True
    )

    min_delivery_amount = models.IntegerField(
        verbose_name='최소 주문 금액', blank=True)  # 최소 주문 금액은 필수값

    bankbook = models.ImageField(upload_to='images/', verbose_name='통장 사본', blank=True, null=True)
    license = models.ImageField(upload_to='images/', verbose_name='면허증 사본', blank=True, null=True)

    # 통장 사본 유무와 면허증 유무를 어떻게 받아야할지 몰라서 임시로
    # EXISTENCE = (    # 통장 사본 유무
    #     ('Y', 'Yes'),
    #     ('N', 'No'),
    # )
    # bankbook = models.CharField(    # 단일 선택
    #     choices=EXISTENCE,
    #     max_length=1,
    #     # max_choices = 1,
    #     verbose_name='통장 사본 유무',
    #     blank=True
    # )
    # license = models.CharField(     # 단일 선택
    #     choices=EXISTENCE,
    #     max_length=1,
    #     # max_choices = 1,
    #     verbose_name='면허증 여부',
    #     blank=True
    # )

    recommended_person = models.CharField(
        max_length=20, verbose_name='추천인', blank=True)     # 선택, 사용자 이름을 20자로 받기 때문에 max 20

    # 수정요망
    SCORE = (   # 별점, 단일 선택
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    speed = models.CharField(max_length=3, choices=SCORE, verbose_name='스피드', null=True)
    fresh = models.CharField(max_length=3, choices=SCORE, verbose_name='신선도', null=True)
    accuracy = models.CharField(max_length=3, choices=SCORE, verbose_name='정확도', null=True)

    class Meta:
        db_table = 'rider'
