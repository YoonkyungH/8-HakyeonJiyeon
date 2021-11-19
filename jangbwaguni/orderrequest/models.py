from django.db import models
from django.utils import timezone
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from member.models import Rider, Customer

from django.core.validators import MaxValueValidator, MinValueValidator

# now = timezone.localtime()

# class Customer(models.Model):
#     sig_date_cus = models.DateTimeField('date signup customer', auto_now_add=True, null=True) # 가입일 / 자동기입
#     id_unique = models.CharField(unique=True, max_length=20, null=True) # 아이디 / 최대 20자리 / 중복 금지
#     password = models.CharField(max_length=200, null=True) # 비밀번호 / 최대 25자리 / 암호화 했을 때 길이 길어지므로 200으로 설정
#     nickname = models.CharField(max_length=10, null=True) # 닉네임 / 최대 10자리 / 중복 금지
#     phone_num = PhoneNumberField(unique=True, null=True, blank=False) # 휴대폰 번호


# phone_num = PhoneNumberField(unique=True, null=True, blank=False) # 휴대폰 번호

class OrderApply(models.Model):
    ### 구매정보
    # quantity = models.PositiveSmallIntegerField(verbose_name = "수량", blank=True, null=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]) # 1이상 100이하
    quantity = models.PositiveSmallIntegerField(verbose_name = "수량", blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(100)]) # 1이상 100이하
    product = models.CharField(verbose_name = "상품명", max_length=15, blank=True)
    # product = ArrayField(models.CharField(verbose_name = "상품명", max_length=15, blank=True))

    # PRODUCT_CHOICES = ( # 목록 추후 수정
    #     ('N', 'Null'),  # 선택 안함
    #     ('E', 'Egg'),   # 'DB에 저장할 실제 값', 'display용 이름'
    #     ('M', 'Milk'),
    #     ('R', 'Rice'),
    #     ('W', 'Water'),
    # )
    # order_product = MultiSelectField(   # 다중선택(~10개)이 가능하도록 multiselectfield 사용
    #     choices=PRODUCT_CHOICES,
    #     max_choices = 2,               # 선택 요소가 많아지면 수정
    #     verbose_name='주문 목록',
    # ) 

    # price = models.CharField(verbose_name = "가격", max_length=200)
    # price = models.PositiveSmallIntegerField(verbose_name = "가격", null=True, default=1, validators=[MinValueValidator(1)]) # 1이상
    sale_store = models.CharField(verbose_name="구매장소", max_length=15, null=True, blank=True)
    # created_at = models.DateTimeField(verbose_name="등록시간", null=True, blank=True) #auto_now_add=True,
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='주문 요청 시간', null=True, blank=True)

    #### 라이더 정보
    rider_selected = models.ForeignKey(Rider, on_delete=models.CASCADE, verbose_name='라이더 아이디', blank=True, related_name='ord')

    #### 주문자 정보 (Customer랑 연동 X)
    cus_orderer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='주문자 아아디', blank=True, related_name='ord')
    order_additional = models.TextField(verbose_name='요청사항',blank=True)

    class Meta:
        verbose_name = '주문서'
        verbose_name_plural = f'{verbose_name} 목록'
        # ordering = ['-pk']

    # 장바구니에 담긴 각 상품의 합계
    # def sub_total(self):
    #     return self.price
    # def sub_total(self):
    # 	# 템플릿에서 사용하는 변수로 장바구니에 담긴 각 상품의 합계
    #     return self.product.price * self.quantity

    # def __str__(self):
    #     return self.product.orderer

 

###################################################################################### 추후에 null = True 삭제
# class Product(models.Model):
#     # drink = models.CharField(max_length=10)
#     price = 1000

#     PRODUCT_CHOICES = [
#         ('A', '파워에이드'),
#         ('B', '허쉬초코우유'),
#         ('C', '초콜렛'),
#         ('D', '청국장'),
#         ('E', '부대찌개'),
#     ]
#     products = models.CharField(max_length=1, choices=PRODUCT_CHOICES, blank=True)






#     # def __str__(self):
#     #     return str(self.orderer) + ' ' + str(self.product)
    
#     class Meta:
#         db_table = "Ordering"
#         verbose_name = "주문서"
#         verbose_name_plural = "주문서"
###################################################################################### 추후에 null = True 삭제

# class Product (OrderApply):
    
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
