# Generated by Django 5.0.2 on 2024-02-25 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_category_menue_cmenue_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Category_M',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.cmenue'),
        ),
    ]
