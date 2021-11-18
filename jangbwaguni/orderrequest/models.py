from django.db import models
from django.utils import timezone
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from member.models import Rider, Customer

# now = timezone.localtime()

class Customer(models.Model):
    sig_date_cus = models.DateTimeField('date signup customer', auto_now_add=True, null=True) # 가입일 / 자동기입
    id_unique = models.CharField(unique=True, max_length=20, null=True) # 아이디 / 최대 20자리 / 중복 금지
    password = models.CharField(max_length=200, null=True) # 비밀번호 / 최대 25자리 / 암호화 했을 때 길이 길어지므로 200으로 설정
    nickname = models.CharField(max_length=10, null=True) # 닉네임 / 최대 10자리 / 중복 금지
    phone_num = PhoneNumberField(unique=True, null=True, blank=False) # 휴대폰 번호

class OrderApply(models.Model):
    orderer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)

class Rider(models.Model):
    sig_date_rider = models.DateTimeField('date signup rider', auto_now_add=True, null=True) # 라이더 가입일 / 자동기입 
    nickname = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='rider_nickname', null=True) # Customer 클래스와 일대일 관계
    introduction = models.TextField('소개', max_length=200, null=True) # 소개 / 최대 200자리
    address_rider = models.CharField(max_length=30, null=True) # 라이더 주소 / 최대 30자리
    # 주소
    # 배달 내역
    # 소개
    # 이동수단
    # 최소 주문금액
    

#class OrderApply(models.Model):
    # pub_date = models.DateTimeField('date order', auto_now_add=True) # 주문일 / 자동기입
    #product = models.ForeignKey(Customer, on_delete=models.CASCADE, defalut=datetime.datetime.now())#datetime.datetime(2021, 11, 12, 3, 0, 50, 586398, tzinfo=<Asia/Seoul>)) # Customer 클래스와 다대일 관계
    # 선택한 배달원
    # 인기품목
    # 주문 품목
    # 수량
    # 가격

    # 주문자
    # 배송지명
    # 주문자 연락처
    # 주소
    # 요청사항

    # 배달 상태
    # 포인트

# class EvalRider(models.Model):
#     # 스피드
#     # 신선도
#     # 정확도

# class EvalCustomer(models.Model):
#     # 좋아요
#     # 보통이에요
#     # 싫어요   
