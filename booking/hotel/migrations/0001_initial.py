# Generated by Django 5.1.2 on 2024-10-29 08:08

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_role', models.CharField(choices=[('simpleUser', 'simpleUser'), ('ownerUser', 'ownerUser')], default='simpleUser', max_length=12)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(110)])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=32)),
                ('hotel_name_ru', models.CharField(max_length=32, null=True)),
                ('hotel_name_en', models.CharField(max_length=32, null=True)),
                ('hotel_description', models.TextField()),
                ('hotel_description_ru', models.TextField(null=True)),
                ('hotel_description_en', models.TextField(null=True)),
                ('country', models.CharField(max_length=32)),
                ('country_ru', models.CharField(max_length=32, null=True)),
                ('country_en', models.CharField(max_length=32, null=True)),
                ('city', models.CharField(max_length=32)),
                ('city_ru', models.CharField(max_length=32, null=True)),
                ('city_en', models.CharField(max_length=32, null=True)),
                ('address', models.CharField(max_length=32)),
                ('stars', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('hotel_video', models.FileField(blank=True, null=True, upload_to='hotel_video/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_image', models.ImageField(upload_to='hotel_images/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_image', to='hotel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='hotel.hotel')),
                ('parent_review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.review')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.PositiveSmallIntegerField()),
                ('room_type', models.CharField(choices=[('люкс', 'люкс'), ('семейный', 'семейный'), ('одноместный', 'одноместный'), ('двухместный', 'двухместный')], max_length=32)),
                ('room_status', models.CharField(choices=[('свободен', 'свободен'), ('занят', 'занят'), ('забронирован', 'забронирован')], default='свободен', max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('all_inclusive', models.BooleanField(default=False)),
                ('room_description', models.TextField()),
                ('room_description_ru', models.TextField(null=True)),
                ('room_description_en', models.TextField(null=True)),
                ('hotel_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('status_book', models.CharField(choices=[('отменено', 'отменено'), ('потверждено', 'потверждено')], max_length=32)),
                ('user_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hotel_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
                ('room_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_images', models.ImageField(upload_to='room_images/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_images', to='hotel.room')),
            ],
        ),
    ]
