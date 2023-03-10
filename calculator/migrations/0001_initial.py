# Generated by Django 3.2.16 on 2022-12-15 13:33

import cloudinary.models
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
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_and_model', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('vibration_magnitude', models.FloatField()),
                ('test_date', models.DateField()),
                ('equipment_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_user', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_category', to='calculator.categories')),
            ],
            options={
                'ordering': ['category', 'make_and_model'],
            },
        ),
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('exposure_duration_hours', models.IntegerField(default=0)),
                ('exposure_duration_minutes', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59)])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calculator_user', to=settings.AUTH_USER_MODEL)),
                ('make_and_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_make_and_model', to='calculator.equipment')),
            ],
            options={
                'ordering': ['make_and_model'],
            },
        ),
    ]
