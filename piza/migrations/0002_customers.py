# Generated by Django 3.2.7 on 2022-09-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО клиент')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефон')),
                ('adress', models.CharField(max_length=250, verbose_name='Адресс')),
                ('ingridiend_id', models.IntegerField(verbose_name='Ингридиенд')),
                ('status', models.IntegerField(choices=[(1, 'Активна'), (2, 'Отключена')], verbose_name='Статус')),
            ],
        ),
    ]
