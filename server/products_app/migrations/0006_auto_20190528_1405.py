# Generated by Django 2.1.1 on 2019-05-28 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products_app', '0005_auto_20190528_1159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productfeedback',
            options={'ordering': ['-product', '-user', '-created']},
        ),
        migrations.AddField(
            model_name='productfeedback',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
