# Generated by Django 3.2 on 2022-11-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piza', '0048_slide_prioritet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='prioritet',
        ),
        migrations.AddField(
            model_name='slide',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='Приоритет'),
        ),
    ]