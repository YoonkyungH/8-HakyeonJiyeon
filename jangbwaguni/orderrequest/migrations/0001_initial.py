# Generated by Django 3.2.9 on 2021-11-18 08:43

from django.db import migrations, models
import django.db.models.deletion
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
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sig_date_rider', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date signup rider')),
                ('introduction', models.TextField(max_length=200, null=True, verbose_name='소개')),
                ('address_rider', models.CharField(max_length=30, null=True)),
                ('nickname', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rider_nickname', to='orderrequest.customer')),
            ],
        ),
    ]
