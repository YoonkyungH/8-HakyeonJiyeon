# Generated by Django 3.2.9 on 2021-11-19 20:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='수량')),
                ('product', models.CharField(blank=True, max_length=15, verbose_name='상품명')),
                ('price', models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='가격')),
                ('sale_store', models.CharField(blank=True, max_length=15, null=True, verbose_name='구매장소')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='주문 요청 시간')),
                ('order_name', models.CharField(blank=True, max_length=10, verbose_name='주문자명')),
                ('order_phone', models.CharField(blank=True, max_length=13, verbose_name='주문 연락처')),
                ('order_additional', models.TextField(blank=True, verbose_name='주문 요청사항')),
                ('order_address', models.CharField(blank=True, max_length=200, verbose_name='주문 주소')),
                ('order_post', models.PositiveIntegerField(blank=True, default=31253, validators=[django.core.validators.MinValueValidator(1)], verbose_name='주문 우편번호')),
                ('cus_orderer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ord', to=settings.AUTH_USER_MODEL, verbose_name='주문자 아아디')),
                ('rider_selected', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.rider', verbose_name='라이더 이름')),
            ],
            options={
                'verbose_name': '주문서',
                'verbose_name_plural': '주문서 목록',
            },
        ),
        migrations.CreateModel(
            name='EvalRider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eval_date', models.DateTimeField(auto_now=True, verbose_name='평가 날짜')),
                ('speed', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)], verbose_name='스피드')),
                ('fresh', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)], verbose_name='신선도')),
                ('accuracy', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)], verbose_name='정확도')),
                ('evaluator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='평가 고객')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.rider', verbose_name='평가 라이더')),
            ],
        ),
        migrations.CreateModel(
            name='EvalCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eval_date', models.DateTimeField(auto_now=True, verbose_name='평가 날짜')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], verbose_name='평가 점수')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='평가 고객')),
                ('evaluator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.rider', verbose_name='평가 라이더')),
            ],
        ),
    ]
