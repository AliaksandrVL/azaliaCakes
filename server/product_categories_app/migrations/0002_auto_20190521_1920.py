# Generated by Django 2.2.1 on 2019-05-21 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_categories_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['-name', '-created', '-modified']},
        ),
    ]
