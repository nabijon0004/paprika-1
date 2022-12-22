# Generated by Django 3.2 on 2022-11-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piza', '0050_menu_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_info',
            old_name='adress',
            new_name='adres',
        ),
        migrations.RenameField(
            model_name='contact_info',
            old_name='name',
            new_name='fio',
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.IntegerField(choices=[(1, 'Пицца'), (2, 'Бургер'), (3, 'Стрипсы'), (4, 'Напитки'), (5, 'Соус'), (6, 'Картофель'), (7, 'Десерты')], verbose_name='Категория'),
        ),
    ]
