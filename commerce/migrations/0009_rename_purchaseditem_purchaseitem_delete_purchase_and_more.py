# Generated by Django 4.1.7 on 2023-03-12 04:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_alter_cart_last_update_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PurchasedItem',
            new_name='PurchaseItem',
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='purchased_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='sent_address',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 13, 42, 59, 848717)),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='purchase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.purchasehistory'),
        ),
    ]
