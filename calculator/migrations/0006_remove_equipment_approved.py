# Generated by Django 3.2.16 on 2022-12-15 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_remove_calculator_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='approved',
        ),
    ]
