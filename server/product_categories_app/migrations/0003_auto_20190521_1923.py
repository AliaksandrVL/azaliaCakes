# Generated by Django 2.2.1 on 2019-05-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_categories_app', '0002_auto_20190521_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]