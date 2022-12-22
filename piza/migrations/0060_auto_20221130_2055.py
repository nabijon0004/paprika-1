# Generated by Django 3.2 on 2022-11-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piza', '0059_alter_courier_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryinfo',
            name='delivery_etime',
            field=models.DateTimeField(default=1, max_length=15, verbose_name='Время доставки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='delivery_time',
            field=models.CharField(max_length=50, null=True, verbose_name='Срок доставки'),
        ),
    ]
