# Generated by Django 4.1.7 on 2023-03-12 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0013_alter_cart_last_update_alter_stock_remaining_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 15, 8, 16, 773591)),
        ),
    ]
