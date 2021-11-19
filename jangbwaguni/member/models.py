
from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
# from django.utils import timezone
# import datetime

###################################################################################### 추후에 null = True 삭제
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    # 평가 추가 : 좋아요 / 보통이에요 / 별로에요
    cus_nickname = models.CharField(max_length=20, verbose_name='고객 별명', blank=True, unique=True) # 중복금지
    cus_address = models.TextField(max_length=100, verbose_name='고객 주소', blank=True)
    cus_post_no = models.IntegerField(verbose_name='우편번호', null=True, blank=True)
    cus_phone = PhoneNumberField(verbose_name='폰번호', null=True, blank=True)
    recommended_person = models.CharField(max_length=20, verbose_name='추천인', blank=True)     # 선택, 사용자 이름을 20자로 받기 때문에 max 20
    cus_img = models.ImageField(upload_to='images/', verbose_name='고객 프로필 사진', blank=True, null=True)

    def __str__(self):  # 객체가 설정한 [cus_name]으로 보여짐
        return self.cus_nickname + self.username

    class Meta:
        db_table = 'customer'
        # ordering = ['cus_nickname']
        verbose_name = '고객 가입 정보'
        verbose_name_plural = "고객 가입 정보" # 뒤에 붙는 s 없앰

class Rider(models.Model): # 배달원
    # X : 아이디, 비밀번호
    # 배달원 성명, 소개, 지역 선택, 배달 수단, 최소 주문 금액, 통장 사본, 운전 면허증
    # 주소 / 배달 내역
    # 스피드, 신선도, 정확도
    
    rider_nickname = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='info') # Customer 클래스와 일대일 관계
    rider_name = models.CharField(max_length=20, verbose_name='라이더 이름', blank=True)        # 배달원 이름 필수값
    rider_intro = models.TextField(max_length=100, verbose_name='라이더 소개', blank=True)
    rider_img = models.ImageField(upload_to='images/', verbose_name='라이더 프로필 사진', blank=True, null=True)

    AREA_CHOICES = [
        ('GG', '경기도'),
        ('SL', '서울시'),
        ('CC', '충청도'),
        ('GS', '경상도'),
        ('GW', '강원도'),
        ('JL', '전라도'),
        ('JJ', '제주도'),
    ]
    rider_area = models.CharField(  # 단일 선택
        choices=AREA_CHOICES,
        max_length=2,
        # max_choices = 1,
        verbose_name='배달 지역',
        blank=True
    )

    VEHICLE_CHOICES = [
        ('NL', '도보'),
        ('AB', '모터사이클'),
        ('CR', '자동차'),
        ('ET', '기타'),
    ]
    rider_vehicle = MultiSelectField(   # 다중 선택(~2개)
        choices=VEHICLE_CHOICES,
        max_choices = 2,
        verbose_name='배달 수단',
        blank=True
    )

    min_delivery_amount = models.IntegerField(verbose_name='최소 주문 금액', blank=True) # 필수
    
    bankbook = models.ImageField(upload_to='images/', verbose_name='통장 사본', blank=True, null=True)
    license = models.ImageField(upload_to='images/', verbose_name='면허증 사본', blank=True, null=True)

    class Meta:
        db_table = 'rider'
        verbose_name = '라이더 가입 정보'
        verbose_name_plural = "라이더 가입 정보" # 뒤에 붙는 s없앰

    speed = models.IntegerField(verbose_name='스피드')
    fresh = models.IntegerField(verbose_name='신선도')
    accuracy = models.IntegerField(verbose_name='정확도')
