# Generated by Django 5.0.2 on 2024-02-25 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_cmenue_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmenue',
            name='Category',
        ),
        migrations.AddField(
            model_name='category',
            name='menue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.cmenue'),
        ),
    ]
