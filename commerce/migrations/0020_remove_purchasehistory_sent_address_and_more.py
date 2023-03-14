# Generated by Django 4.1.7 on 2023-03-14 02:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("commerce", "0019_cartitem_price_with_tax_alter_cart_last_update"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="purchasehistory",
            name="sent_address",
        ),
        migrations.AlterField(
            model_name="cart",
            name="last_update",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 3, 14, 11, 40, 54, 660346)
            ),
        ),
        migrations.AlterField(
            model_name="purchasehistory",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
