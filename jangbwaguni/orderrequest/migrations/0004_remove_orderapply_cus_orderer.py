# Generated by Django 3.2.9 on 2021-11-18 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderrequest', '0003_alter_orderapply_cus_orderer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderapply',
            name='cus_orderer',
        ),
    ]
