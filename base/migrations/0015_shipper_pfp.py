# Generated by Django 5.0.6 on 2024-10-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_order_shipper_shipper_pfp_alter_shipper_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipper',
            name='pfp',
            field=models.ImageField(blank=True, null=True, upload_to='pfp/'),
        ),
    ]