# Generated by Django 4.1.3 on 2022-12-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_product_qty_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_discount',
            field=models.IntegerField(blank=True),
        ),
    ]
