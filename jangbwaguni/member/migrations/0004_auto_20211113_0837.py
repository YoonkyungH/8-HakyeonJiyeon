# Generated by Django 3.2.9 on 2021-11-13 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_user_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cus_call',
        ),
        migrations.AlterField(
            model_name='user',
            name='cus_pw',
            field=models.CharField(max_length=20, verbose_name='고객 비밀번호'),
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]