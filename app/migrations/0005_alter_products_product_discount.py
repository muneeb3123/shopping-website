# Generated by Django 4.1.3 on 2022-12-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_products_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_discount',
            field=models.IntegerField(),
        ),
    ]