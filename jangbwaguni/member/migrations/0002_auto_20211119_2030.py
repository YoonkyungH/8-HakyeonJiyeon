# Generated by Django 3.2.9 on 2021-11-19 11:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cus_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='폰번호'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cus_post_no',
            field=models.IntegerField(blank=True, null=True, verbose_name='우편번호'),
        ),
    ]
