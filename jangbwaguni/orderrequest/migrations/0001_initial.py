

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            ],
            options={
                'verbose_name': '주문서',
                'verbose_name_plural': '주문서 목록',
            },
        ),
    ]
