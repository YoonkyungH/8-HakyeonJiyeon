from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from member.models import Rider, Customer
from django.core.validators import MaxValueValidator, MinValueValidator

class OrderApply(models.Model):
    ### 구매정보
    # quantity = models.PositiveSmallIntegerField(verbose_name = "수량", blank=True, null=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]) # 1이상 100이하
    quantity = models.PositiveSmallIntegerField(verbose_name = "수량", blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(100)]) # 1이상 100이하
    product = models.CharField(verbose_name = "상품명", max_length=15, blank=True)
    # product = ArrayField(models.CharField(verbose_name = "상품명", max_length=15, blank=True))

    # price = models.CharField(verbose_name = "가격", max_length=200)
    price = models.PositiveSmallIntegerField(verbose_name = "가격", null=True, default=0, validators=[MinValueValidator(1)]) # 1이상
    sale_store = models.CharField(verbose_name="구매장소", max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="주문 등록시간", null=True, blank=True) #auto_now_add=True,

    #### 라이더 정보
    rider_selected = models.ForeignKey(Rider, on_delete=models.CASCADE, verbose_name='라이더 아이디', blank=True, related_name='ord')
 
    #### 주문자 정보
    cus_orderer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='주문자 아아디', blank=True, related_name='ord')
    order_name = models.CharField(verbose_name="주문자명", max_length=10, blank=True)
    order_phone = models.CharField(verbose_name="주문 연락처", max_length=13, blank=True)
    order_additional = models.TextField(verbose_name='주문 요청사항', blank=True)
    order_address = models.CharField(verbose_name="주문 주소", max_length=200, blank=True)
    order_post = models.PositiveIntegerField(verbose_name="주문 우편번호", blank=True, default=31253, validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = '주문서'
        verbose_name_plural = f'{verbose_name} 목록'
        # ordering = ['-pk']

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
