# Generated by Django 3.2.9 on 2021-11-19 17:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderrequest', '0003_evalcustomer_evalrider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evalrider',
            name='accuracy',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)], verbose_name='정확도'),
        ),
        migrations.AlterField(
            model_name='evalrider',
            name='fresh',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)], verbose_name='신선도'),
        ),
        migrations.AlterField(
            model_name='evalrider',
            name='speed',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)], verbose_name='스피드'),
        ),
    ]