# Generated by Django 4.1.7 on 2023-03-14 03:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("commerce", "0020_remove_purchasehistory_sent_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="last_update",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 3, 14, 12, 3, 23, 371415)
            ),
        ),
        migrations.AlterField(
            model_name="purchasehistory",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
