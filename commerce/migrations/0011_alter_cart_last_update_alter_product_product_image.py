# Generated by Django 4.1.7 on 2023-03-12 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0010_delete_purchase_product_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 14, 6, 10, 368721)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default='C:\\Users\\yusuk\\dev\\projects\\portfolio_site\\static\\images\\commerce\\noimage.jpg', upload_to='product_image/%Y/%m/%d/'),
        ),
    ]
