# Generated by Django 3.2.7 on 2022-09-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piza', '0026_auto_20220921_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='position',
            field=models.IntegerField(blank=True, null=True, verbose_name='Позиция'),
        ),
    ]