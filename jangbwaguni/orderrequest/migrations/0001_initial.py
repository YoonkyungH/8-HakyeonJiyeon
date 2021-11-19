# Generated by Django 3.2.9 on 2021-11-19 11:27

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sig_date_cus', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date signup customer')),
                ('id_unique', models.CharField(max_length=20, null=True, unique=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('nickname', models.CharField(max_length=10, null=True)),
                ('phone_num', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_product', multiselectfield.db.fields.MultiSelectField(choices=[('N', 'Null'), ('E', 'Egg'), ('M', 'Milk'), ('R', 'Rice'), ('W', 'Water')], max_length=9, verbose_name='주문 목록')),
                ('price', models.CharField(max_length=200, verbose_name='가격')),
                ('sale_store', models.CharField(blank=True, max_length=15, null=True, verbose_name='구매장소')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='주문 요청 시간')),
                ('rider_selected', models.CharField(blank=True, max_length=20, verbose_name='라이더 이름')),
                ('order_additional', models.TextField(blank=True, verbose_name='요청사항')),
                ('cus_orderer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ord', to='orderrequest.customer', verbose_name='주문자 아아디')),
            ],
            options={
                'verbose_name': '주문서',
                'verbose_name_plural': '주문서 목록',
            },
        ),
    ]
