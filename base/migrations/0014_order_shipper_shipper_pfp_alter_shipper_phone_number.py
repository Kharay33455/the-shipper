# Generated by Django 5.0.6 on 2024-10-10 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_order_carrier_order_ship_date_order_shipped_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipper',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.shipper'),
            preserve_default=False,
        ),

        migrations.AlterField(
            model_name='shipper',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
