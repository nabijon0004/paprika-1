# Generated by Django 3.2.7 on 2022-09-15 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piza', '0015_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='icon/%Y/%m/%d', verbose_name='Значок'),
        ),
    ]
