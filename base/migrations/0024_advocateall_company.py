# Generated by Django 5.0.1 on 2024-01-06 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_remove_advocateall_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocateall',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.company'),
        ),
    ]
