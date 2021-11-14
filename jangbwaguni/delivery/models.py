from django.db import models
from django.db.models.fields import DateTimeField
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

class orders(models.Model):
    # 주문자 이름, 주소, 주문 항목, 요청 시간, 안심번호, 요청사항,

    # cus_name = models.ForeignKey('', verbose_name='주문자', on_delete=models.CASCADE) # CASECADE: 이와 연결된 모든 N쪽 데이터 삭제 -> 생각해보니 member쪽에서 해야함
    cus_name = models.CharField(max_length=20, verbose_name='주문자', blank=False)      # blank=False: 필드가 폼에서 빈 채로 저장되는 것을 비허용
    cus_address = models.CharField(max_length=250, verbose_name='주문자 주소', blank=False)

    PRODUCT_CHOICES = ( # 목록 추후 수정
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
        max_choices = 2,               # 선택 요소가 많아지면 수정
        verbose_name='주문 목록',
        ) 

    created = models.DateTimeField(auto_now_add=True, verbose_name='주문 요청 시간')
    # cus_call = models.CharField(max_length=11, verbose_name='안심번호')          # 01012345678
    cus_call = PhoneNumberField(unique=True, blank=False, verbose_name = '안심번호')    # 이 필드는 CharField 공간을 기반으로 하며 문자열 형태로 숫자 저장
    order_message = models.TextField(max_length=1000, verbose_name='요청사항')          # 요청사항 (추가 품목도 담겨있음)

    class Meta:
        db_table = 'orders'


class rider(models.Model): # 배달원
    # 아이디, 비밀번호, 배달원 성명, 소개, 지역 선택, 배달 수단, 최소 주문 금액, 통장 사본 유무?, 운전 면허증 유무?, 추천인 코드(선택)
    # 스피드, 신선도, 정확도

    rider_id = models.CharField(max_length=10, verbose_name='라이더 아이디', blank=True)
    rider_pw = models.CharField(max_length=20, verbose_name='라이더 비밀번호', blank=True)
    rider_name = models.CharField(max_length=20, verbose_name='라이더 이름', blank=True)        # 배달원 이름 필수값
    rider_intro = models.TextField(max_length=100, verbose_name='라이더 소개', blank=True)
    
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
        blank=True
    )

    VEHICLE_CHOICES = (
        ('NL', '뚜벅이'),
        ('CR', '차'),
        ('BC', '자전거'),
        ('AB', '오토바이'),
    )
    rider_vehicle = MultiSelectField(   # 다중 선택(~2개)
        choices=VEHICLE_CHOICES,
        max_choices = 2,
        verbose_name='배달 수단',
        blank=True
    )

    min_delivery_amount = models.IntegerField(verbose_name='최소 주문 금액', blank=True) # 최소 주문 금액은 필수값
    
    # 통장 사본 유무와 면허증 유무를 어떻게 받아야할지 몰라서 임시로
    EXISTENCE = (    # 통장 사본 유무
        ('Y', 'Yes'),
        ('N', 'No'),        
    )
    bankbook = models.CharField(    # 단일 선택
        choices=EXISTENCE,
        max_length=1,
        # max_choices = 1,
        verbose_name='통장 사본 유무',
        blank=True
    )
    license = models.CharField(     # 단일 선택
        choices=EXISTENCE,
        max_length=1,
        # max_choices = 1,
        verbose_name='면허증 여부',
        blank=True
    )

    recommended_person = models.CharField(max_length=20, verbose_name='추천인', blank=True)     # 선택, 사용자 이름을 20자로 받기 때문에 max 20

    # 수정요망
    # SCORE = (   # 별점, 단일 선택
    #     (1, '1'),
    #     (2, '2'),
    #     (3, '3'),
    # )
    # speed = models.CharField(max_length=1, choices=SCORE, verbose_name='스피드')
    # fresh = models.CharField(max_length=1, choices=SCORE, verbose_name='신선도')
    # accuracy = models.CharField(max_length=1, choices=SCORE, verbose_name='정확도')

    class Meta:
        db_table = 'rider'