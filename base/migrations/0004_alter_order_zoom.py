# Generated by Django 5.0.6 on 2024-06-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_order_zoom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zoom',
            field=models.FloatField(default=0.0),
        ),
    ]
