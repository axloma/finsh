# Generated by Django 4.2.7 on 2023-12-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
