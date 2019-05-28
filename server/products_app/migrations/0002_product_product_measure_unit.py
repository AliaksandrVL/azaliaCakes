# Generated by Django 2.1.1 on 2019-05-27 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_measure_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products_app.ProductMeasureUnit', verbose_name='Единица измерения'),
            preserve_default=False,
        ),
    ]