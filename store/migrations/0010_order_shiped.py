# Generated by Django 5.0.2 on 2024-05-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shiped',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
