# Generated by Django 4.1.7 on 2023-03-12 07:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0014_productcategory_category_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productprice',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='commerce.productprice'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 16, 21, 1, 335783)),
        ),
    ]