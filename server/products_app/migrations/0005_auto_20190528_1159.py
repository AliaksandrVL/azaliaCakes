# Generated by Django 2.1.1 on 2019-05-28 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0004_auto_20190528_1158'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductFeedbacks',
            new_name='ProductFeedback',
        ),
    ]
