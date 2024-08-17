# Generated by Django 5.1 on 2024-08-15 11:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=13)),
                ('date', models.CharField(max_length=150)),
                ('time', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='categories/%y/%m/%d')),
                ('icon', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Table',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('feedback', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='reviews')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('image', models.ImageField(upload_to='dishes/%y/%m/%d')),
                ('ingredients', models.TextField()),
                ('details', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
            options={
                'verbose_name_plural': 'Dish Table',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profiles/%y/%m/%d')),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile Table',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('invoice_id', models.CharField(blank=True, max_length=100)),
                ('payer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('ordered_on', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dish')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.profile')),
            ],
            options={
                'verbose_name_plural': 'Order Table',
            },
        ),
    ]