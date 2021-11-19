

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cus_nickname', models.CharField(blank=True, max_length=20, verbose_name='고객 별명')),
                ('cus_address', models.TextField(blank=True, max_length=100, verbose_name='고객 주소')),
                ('cus_post_no', models.IntegerField(blank=True, null=True, verbose_name='우편번호')),
                ('cus_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='폰번호')),
                ('recommended_person', models.CharField(blank=True, max_length=20, verbose_name='추천인')),
                ('cus_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='고객 프로필 사진')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '고객 가입 정보',
                'verbose_name_plural': '고객 가입 정보',
                'db_table': 'customer',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(blank=True, max_length=20, verbose_name='라이더 이름')),
                ('rider_intro', models.TextField(blank=True, max_length=100, verbose_name='라이더 소개')),
                ('rider_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='라이더 프로필 사진')),
                ('rider_area', models.CharField(blank=True, choices=[('GG', '경기도'), ('SL', '서울시'), ('CC', '충청도'), ('GS', '경상도'), ('GW', '강원도'), ('JL', '전라도'), ('JJ', '제주도')], max_length=2, verbose_name='배달 지역')),
                ('rider_vehicle', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('NL', '도보'), ('AB', '모터사이클'), ('CR', '자동차'), ('ET', '기타')], max_length=11, verbose_name='배달 수단')),
                ('min_delivery_amount', models.IntegerField(blank=True, null=True, verbose_name='최소 주문 금액')),
                ('bankbook', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='통장 사본')),
                ('license', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='면허증 사본')),
                ('speed', models.IntegerField(blank=True, null=True, verbose_name='스피드')),
                ('fresh', models.IntegerField(blank=True, null=True, verbose_name='신선도')),
                ('accuracy', models.IntegerField(blank=True, null=True, verbose_name='정확도')),
                ('rider_nickname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '라이더 가입 정보',
                'verbose_name_plural': '라이더 가입 정보',
                'db_table': 'rider',
            },
        ),
    ]
