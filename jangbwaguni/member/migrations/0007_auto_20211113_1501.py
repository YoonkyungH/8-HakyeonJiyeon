# Generated by Django 3.2.9 on 2021-11-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_user_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cus_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cus_id',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='이메일'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=64, verbose_name='비밀번호'),
        ),
        migrations.AddField(
            model_name='user',
            name='register_data',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='생성일자'),
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]