# Generated by Django 5.0.6 on 2024-06-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='latitude',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='order',
            name='longitude',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='order',
            name='screen_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
