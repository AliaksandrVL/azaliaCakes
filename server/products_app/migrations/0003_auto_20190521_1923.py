# Generated by Django 2.2.1 on 2019-05-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0002_auto_20190521_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='characteristic',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='product',
            name='consist',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='full_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
