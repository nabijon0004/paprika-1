# Generated by Django 3.2 on 2022-10-17 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piza', '0038_deliveryinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryinfo',
            name='date',
        ),
        migrations.RemoveField(
            model_name='deliveryinfo',
            name='product',
        ),
        migrations.RemoveField(
            model_name='deliveryinfo',
            name='time_delivery',
        ),
    ]
