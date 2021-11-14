from django.db import models
from django.db.models.fields import DateTimeField
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

class orders(models.Model):
    # 주문자 이름, 주소, 주문 항목, 요청 시간, 안심번호, 요청사항,

    # cus_name = models.ForeignKey('', verbose_name='주문자', on_delete=models.CASCADE) # CASECADE: 이와 연결된 모든 N쪽 데이터 삭제 -> 생각해보니 member쪽에서 해야함
    # blank=False: 필드가 폼에서 빈 채로 저장되는 것을 비허용
    cus_name = models.CharField(max_length=20, verbose_name='주문자', blank=False)
    cus_address = models.CharField(
        max_length=250, verbose_name='주문자 주소', blank=False)

    PRODUCT_CHOICES = (  # 목록 추후 수정
        ('N', 'Null'),  # 선택 안함
        ('E', 'Egg'),   # 'DB에 저장할 실제 값', 'display용 이름'
        ('M', 'Milk'),
        ('R', 'Rice'),
        ('W', 'Water'),
        # (1, 'Null'),  # 선택 안함
        # (2, 'Egg'),   # 'DB에 저장할 실제 값', 'display용 이름'
        # (3, 'Milk'),
        # (4, 'Rice'),
        # (5, 'Water'),
    )
    order_product = MultiSelectField(   # 다중선택(~10개)이 가능하도록 multiselectfield 사용
        # max_length = 2,
        choices=PRODUCT_CHOICES,
        max_choices=2,               # 선택 요소가 많아지면 수정
        verbose_name='주문 목록',
    )

    created = models.DateTimeField(auto_now_add=True, verbose_name='주문 요청 시간')
    # cus_call = models.CharField(max_length=11, verbose_name='안심번호')          # 01012345678
    # 이 필드는 CharField 공간을 기반으로 하며 문자열 형태로 숫자 저장
    cus_call = PhoneNumberField(unique=True, blank=False, verbose_name='안심번호')
    order_message = models.TextField(
        max_length=1000, verbose_name='요청사항')          # 요청사항 (추가 품목도 담겨있음)

    def __str__(self):  # 객체가 설정한 [cus_name]으로 보여짐
        return self.cus_name

    class Meta:
        db_table = 'orders'
