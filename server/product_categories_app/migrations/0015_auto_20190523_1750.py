# Generated by Django 2.1.1 on 2019-05-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_categories_app', '0014_auto_20190523_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Наименование'),
        ),
    ]