# Generated by Django 3.2 on 2022-11-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piza', '0055_alter_deliveryinfo_delivery_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryinfo',
            name='delivery_time',
            field=models.CharField(max_length=50, null=True, verbose_name='Время доставки'),
        ),
    ]
