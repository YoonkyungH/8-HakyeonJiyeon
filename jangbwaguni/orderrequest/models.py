from django.db import models
from member.models import Rider, Customer

# from django.utils import timezone
# import datetime
# from phonenumber_field.modelfields import PhoneNumberField
# from multiselectfield import MultiSelectField

# phone_num = PhoneNumberField(unique=True, null=True, blank=False) # 휴대폰 번호

class OrderApply(models.Model):
    product = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    introduction = models.CharField(max_length=30, null=True)
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

# class Orderer(models.Model):
#     # 주문자 이름, 주소, 주문 항목, 요청 시간, 안심번호, 요청사항,

#     cus_name = models.ForeignKey('', verbose_name='주문자', on_delete=models.CASCADE)
#     cus_name = models.CharField(max_length=20, verbose_name='주문자', blank=False)      # blank=False: 필드가 폼에서 빈 채로 저장되는 것을 비허용
#     cus_address = models.CharField(max_length=250, verbose_name='주문자 주소', blank=False)
#     phone_num = PhoneNumberField(unique=True, null=True, blank=False) # 휴대폰 번호

#     PRODUCT_CHOICES = ( # 목록 추후 수정
#         ('N', 'Null'),  # 선택 안함
#         ('E', 'Egg'),   # 'DB에 저장할 실제 값', 'display용 이름'
#         ('M', 'Milk'),
#         ('R', 'Rice'),
#         ('W', 'Water'),
#         # (1, 'Null'),  # 선택 안함
#         # (2, 'Egg'),   # 'DB에 저장할 실제 값', 'display용 이름'
#         # (3, 'Milk'),
#         # (4, 'Rice'),
#         # (5, 'Water'),
#     )
#     order_product = MultiSelectField(   # 다중선택(~10개)이 가능하도록 multiselectfield 사용
#         # max_length = 2,
#         choices=PRODUCT_CHOICES,
#         max_choices = 2,               # 선택 요소가 많아지면 수정
#         verbose_name='주문 목록',
#         ) 

#     created = models.DateTimeField(auto_now_add=True, verbose_name='주문 요청 시간')
#     # cus_call = models.CharField(max_length=11, verbose_name='안심번호')          # 01012345678
#     cus_call = PhoneNumberField(unique=True, blank=False, verbose_name = '안심번호')    # 이 필드는 CharField 공간을 기반으로 하며 문자열 형태로 숫자 저장
#     order_message = models.TextField(max_length=1000, verbose_name='요청사항')          # 요청사항 (추가 품목도 담겨있음)

#     class Meta:
#         db_table = 'orders'


# # now = timezone.localtime()



# class Rider(models.Model):
#     sig_date_rider = models.DateTimeField('date signup rider', auto_now_add=True, null=True) # 라이더 가입일 / 자동기입 
#     nickname = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='rider_nickname', null=True) # Customer 클래스와 일대일 관계
#     introduction = models.TextField('소개', max_length=200, null=True) # 소개 / 최대 200자리
#     address_rider = models.CharField(max_length=30, null=True) # 라이더 주소 / 최대 30자리
#     # 주소
#     # 배달 내역
#     # 소개
#     # 이동수단
#     # 최소 주문금액
    

# #class OrderApply(models.Model):
#     # pub_date = models.DateTimeField('date order', auto_now_add=True) # 주문일 / 자동기입
#     #product = models.ForeignKey(Customer, on_delete=models.CASCADE, defalut=datetime.datetime.now())#datetime.datetime(2021, 11, 12, 3, 0, 50, 586398, tzinfo=<Asia/Seoul>)) # Customer 클래스와 다대일 관계
#     # 선택한 배달원
#     # 인기품목
#     # 주문 품목
#     # 수량
#     # 가격

#     # 주문자
#     # 배송지명
#     # 주문자 연락처
#     # 주소
#     # 요청사항

#     # 배달 상태
#     # 포인트

# # class EvalRider(models.Model):
# #     # 스피드
# #     # 신선도
# #     # 정확도

# # class EvalCustomer(models.Model):
# #     # 좋아요
# #     # 보통이에요
# #     # 싫어요   
