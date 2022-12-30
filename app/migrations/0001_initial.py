# Generated by Django 4.1.3 on 2022-12-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_link', models.CharField(max_length=50)),
                ('banner_des', models.CharField(max_length=50)),
                ('banner_name', models.CharField(max_length=50)),
                ('banner_image', models.ImageField(upload_to='topsell')),
                ('banner_discount', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='moving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moving_first', models.CharField(max_length=100)),
                ('moving_second', models.CharField(max_length=100)),
                ('moving_third', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_link', models.CharField(max_length=50)),
                ('slider_des', models.CharField(max_length=50)),
                ('slider_name', models.CharField(max_length=50)),
                ('slider_image', models.ImageField(upload_to='slider')),
                ('slider_deal', models.CharField(max_length=50)),
                ('slider_discount', models.CharField(max_length=50)),
            ],
        ),
    ]
