# Generated by Django 5.0.2 on 2024-02-25 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_cmenue_category_category_menue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='menue',
        ),
        migrations.AddField(
            model_name='cmenue',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
